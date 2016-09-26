from lassie import Lassie

from .base import LassieBaseTestCase


class LassieAMPTestCase(LassieBaseTestCase):
    def test_all_properites(self):
        url = 'http://lassie.it/amp/all_properties.html'

        l = Lassie()
        data = l.fetch(url, all_images=True)

        self.assertEqual(len(data['images']), 3)

        title = 'Google Glass Is Dead, Long Live Snapchat Spectacles'
        self.assertEqual(data['title'], title)

    def test_bad_json(self):
        url = 'http://lassie.it/amp/bad_json.html'

        l = Lassie()
        data = l.fetch(url)

        self.assertTrue('amp' in data['url'])
