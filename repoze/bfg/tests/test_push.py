import unittest

from zope.component.testing import PlacelessSetup

class Test_pushpage(unittest.TestCase, PlacelessSetup):
    def setUp(self):
        PlacelessSetup.setUp(self)

    def tearDown(self):
        PlacelessSetup.tearDown(self)

    def _zcmlConfigure(self):
        import repoze.bfg
        import zope.configuration.xmlconfig
        zope.configuration.xmlconfig.file('configure.zcml', package=repoze.bfg)

    def _getTargetClass(self):
        from repoze.bfg.push import pushpage
        return pushpage

    def _makeOne(self, template):
        return self._getTargetClass()(template)

    def test_decorated_has_same_name_as_wrapped(self):
        pp = self._makeOne('pp.pt')
        wrapped = pp(to_wrap)
        self.assertEqual(wrapped.__name__, 'to_wrap')

    def test___call___passes_names_from_wrapped(self):
        self._zcmlConfigure()
        pp = self._makeOne('pp.pt')
        wrapped = pp(to_wrap)
        response = wrapped(object(), object())
        self.assertEqual(response.body, '<p>WRAPPED</p>')

def to_wrap(context, request):
    return {'wrapped': 'WRAPPED'}
