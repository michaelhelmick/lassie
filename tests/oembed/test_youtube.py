from lassie import Lassie

from ..base import LassieBaseTestCase


class LassieOEmbedYouTubeTestCase(LassieBaseTestCase):
    def test_youtube_good(self):
        url = 'http://lassie.it/youtube/good.json'

        l = Lassie()
        data = l.fetch(url)

        self.assertEqual(len(data['videos']), 1)
        self.assertEqual(len(data['images']), 1)

    def test_bad_url(self):
        url = 'http://lassie.it/youtube/bad_url_123456.json'

        l = Lassie()
        data = l.fetch(url)

        self.assertIsNone(data.get('oembed'))

    def test_youtube_bad_html(self):
        url = 'http://lassie.it/youtube/bad_html.json'

        l = Lassie()
        data = l.fetch(url)

    def test_youtube_no_type(self):
        url = 'http://lassie.it/youtube/no_type.json'

        l = Lassie()
        data = l.fetch(url)

    def test_youtube_no_thumb(self):
        url = 'http://lassie.it/youtube/no_thumb.json'

        l = Lassie()
        data = l.fetch(url)

        self.assertEqual(len(data['videos']), 1)
        self.assertEqual(len(data['images']), 0)
