import lassie

from .base import LassieBaseTestCase


class LassieTwitterCardTestCase(LassieBaseTestCase):
    def test_generic_all_properties(self):
        url = 'http://lassie.it/generic/all_properties.html'
        data = lassie.fetch(url, canonical=True)

        self.assertEqual(data['locale'], 'en_US')
        self.assertEqual(data['title'], 'Lassie Generic Test | all_properties')
        self.assertEqual(data['description'],
                         'Just a random description of a web page.')
        self.assertEqual(data['url'], 'http://example.com/canonical/path')
        self.assertEqual(len(data['keywords']), 5)

    def test_generic_bad_locale(self):
        url = 'http://lassie.it/generic/bad_locale.html'
        data = lassie.fetch(url)

        self.assertTrue('locale' not in data)

    def test_generic_favicon(self):
        url = 'http://lassie.it/generic/favicon.html'
        data = lassie.fetch(url)

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]

        self.assertEqual(image['type'], 'favicon')

    def test_no_title(self):
        url = 'http://lassie.it/generic/no_title.html'
        data = lassie.fetch(url)

        self.assertTrue('title' not in data)

    def test_canonical(self):
        url = 'http://lassie.it/generic/canonical.html'
        data = lassie.fetch(url, canonical=True)

        self.assertEqual(data['url'], 'http://example.com/canonical/path')
