from lassie import Lassie

from urlparse import urlparse
import unittest


class FakeLassie(Lassie):
    def _retreive_content(self, url):
        filename = urlparse(url).path
        file = open('./templates/%s' % filename, 'r')
        html = file.read()
        file.close()

        return html


class LassieTestCase(unittest.TestCase):
    def setUp(self):
        self.api = FakeLassie()

    def test_open_graph_all_properties(self):
        data = self.api.fetch(url='http://lassie.it/open_graph/all_properties.html')
        self.assertEqual(data['url'], 'http://google.com')
        self.assertEqual(data['title'], 'Lassie OG Test')
        self.assertEqual(data['description'], 'Just a test template with OG data!')

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]
        self.assertEqual(image['src'], 'http://i.imgur.com/cvoR7zv.jpg')
        self.assertEqual(image['width'], 550)
        self.assertEqual(image['height'], 365)
        self.assertEqual(image['type'], 'og:image')

        self.assertEqual(len(data['videos']), 1)
        video = data['videos'][0]
        self.assertEqual(video['src'], 'http://www.youtube.com/v/dQw4w9WgXcQ?version=3&autohide=1')
        self.assertEqual(video['width'], 640)
        self.assertEqual(video['height'], 480)
        self.assertEqual(video['type'], 'application/x-shockwave-flash')