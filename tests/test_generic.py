from .base import LassieBaseTestCase

import lassie


class LassieTwitterCardTestCase(LassieBaseTestCase):
    def test_generic_all_properties(self):
        url = 'http://lassie.it/generic/all_properties.html'
        data = lassie.fetch(url)

        self.assertEqual(data['locale'], 'en_US')
        self.assertEqual(data['title'], 'Lassie Generic Test | all_properties')
        self.assertEqual(data['description'], 'Just a random description of a web page.')
        self.assertEqual(len(data['keywords']), 5)

    def test_generic_bad_locale(self):
        url = 'http://lassie.it/generic/bad_locale.html'
        data = lassie.fetch(url)

        self.assertTrue(not 'locale' in data)

    def test_generic_favicon(self):
        url = 'http://lassie.it/generic/favicon.html'
        data = lassie.fetch(url)

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]

        self.assertEqual(image['type'], 'favicon')
