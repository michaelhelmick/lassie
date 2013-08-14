from lassie import Lassie
from lassie.compat import urlparse

import unittest


class FakeLassie(Lassie):
    def _retreive_content(self, url):
        filename = urlparse(url).path
        file = open('./templates/%s' % filename, 'r')
        html = file.read()
        file.close()

        return html


class LassieTwitterCardTestCase(unittest.TestCase):
    def setUp(self):
        self.api = FakeLassie()

    def test_generic_all_properties(self):
        url = 'http://lassie.it/generic/all_properties.html'
        data = self.api.fetch(url)

        self.assertEqual(data['language'], 'en-us')
        self.assertEqual(data['title'], 'Lassie Generic Test | all_properties')
        self.assertEqual(data['description'], 'Just a random description of a web page.')
        self.assertEqual(len(data['keywords']), 5)
