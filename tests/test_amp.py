from lassie import Lassie

from .base import LassieBaseTestCase


class LassieAMPTestCase(LassieBaseTestCase):
    def test_all_properites(self):
        url = 'http://lassie.it/amp/all_properties.html'

        lassie = Lassie()
        data = lassie.fetch(url, all_images=True)

        self.assertEqual(len(data['images']), 3)

        title = 'Google Glass Is Dead, Long Live Snapchat Spectacles'
        self.assertEqual(data['title'], title)

    def test_bad_json(self):
        url = 'http://lassie.it/amp/bad_json.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertTrue('amp' in data['url'])

    def test_str_image(self):
        url = 'http://lassie.it/amp/str_image.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(1, len(data['images']))

    def test_list_image(self):
        url = 'http://lassie.it/amp/list_image.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(2, len(data['images']))

    def test_list_image_list(self):
        url = 'http://lassie.it/amp/list_image_list.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(2, len(data['images']))

    def test_list_image_str(self):
        url = 'http://lassie.it/amp/list_image_str.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(1, len(data['images']))

    def test_list_image_empty(self):
        url = 'http://lassie.it/amp/list_image_empty.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(1, len(data['images']))

    def test_list_json(self):
        url = 'http://lassie.it/amp/list_json.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertTrue('Pixar' in data['description'])

    def test_video_objects(self):
        url = 'http://lassie.it/amp/video_objects.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(1, len(data['videos']))

    def test_thumbnail_image(self):
        url = 'http://lassie.it/amp/thumbnail_image.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(2, len(data['images']))

    def test_list_thumbnail_image(self):
        url = 'http://lassie.it/amp/list_thumbnail_image.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(2, len(data['images']))

    def test_str_thumbnail_image(self):
        url = 'http://lassie.it/amp/str_thumbnail_image.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(2, len(data['images']))
