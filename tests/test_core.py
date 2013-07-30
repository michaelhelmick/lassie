from lassie import Lassie

import unittest

class LassieTestCase(unittest.TestCase):
    def setUp(self):
        self.api = Lassie()

    def test_open_graph(self):
        template = open('./templates/open_graph/all_properties.html')
        data = self.api.fetch(content=template)

        self.assertEqual(data['url'], 'http://google.com')
        self.assertEqual(data['title'], 'Lassie OG Test')
        self.assertEqual(data['description'], 'Just a test template with OG data!')

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]
        self.assertEqual(image['src'], 'http://i.imgur.com/cvoR7zv.jpg')
        self.assertEqual(image['width'], 550)
        self.assertEqual(image['height'], 365)
        self.assertEqual(image['type'], 'og:image')
