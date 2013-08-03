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

    def test_twitter_all_properties(self):
        url = 'http://lassie.it/twitter_card/all_properties.html'
        data = self.api.fetch(url)
        self.assertEqual(data['url'], 'http://www.youtube.com/watch?v=fWNaR-rxAic')
        self.assertEqual(data['title'], 'Carly Rae Jepsen - Call Me Maybe')
        self.assertEqual(data['description'], 'Buy Now! http://smarturl.it/CallMeMaybe Music video by Carly Rae Jepsen performing Call Me Maybe. (C) 2011 604 Records Inc. #VEVOCertified on June 8, 2012. h...')

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]
        self.assertEqual(image['src'], 'http://i1.ytimg.com/vi/fWNaR-rxAic/maxresdefault.jpg')

        self.assertEqual(len(data['videos']), 1)
        video = data['videos'][0]
        self.assertEqual(video['src'], 'https://www.youtube.com/embed/fWNaR-rxAic')
        self.assertEqual(video['width'], 1920)
        self.assertEqual(video['height'], 1080)

    def test_twitter_no_og_title_use_twitter_title(self):
        url = 'http://lassie.it/twitter_card/no_og_title_use_twitter_title.html'
        data = self.api.fetch(url)

        self.assertEqual(data['description'], 'A test case for Lassie!')
        self.assertEqual(data['title'], 'Lassie Twitter Test | no_og_title_use_twitter_title')
