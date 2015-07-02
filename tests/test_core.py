from .base import LassieBaseTestCase

from lassie import Lassie, LassieError


class LassieCoreTestCase(LassieBaseTestCase):
    def test_core_class_vs_method_settings(self):
        url = 'http://lassie.it/core/class_vs_method_settings.html'

        l = Lassie()
        data = l.fetch(url)

        self.assertEqual(len(data['images']), 1)

        l.open_graph = False
        data = l.fetch(url)

        # open_graph is set to False so there shouldn't be any images in the list this time around
        self.assertEqual(len(data['images']), 0)

    def test_core_class_setting_is_none(self):
        url = 'http://lassie.it/core/class_setting_is_none.html'

        # This is a really odd use-case where they'd set the class attr to None, but it might happen so oh wellz.
        l = Lassie()
        l.open_graph = None
        data = l.fetch(url, open_graph=False)

        self.assertEqual(len(data['images']), 0)

    def test_core_no_content_raises_error(self):
        url = 'http://lassie.it/core/empty.html'

        l = Lassie()
        self.assertRaises(LassieError, l.fetch, url)

    def test_core_retrieve_all_images(self):
        url = 'http://lassie.it/core/retrieve_all_images.html'

        l = Lassie()
        l.all_images = True

        data = l.fetch(url)
        self.assertEqual(len(data['images']), 3)

        last_image = data['images'][2]
        self.assertEqual(last_image['width'], 550)
        self.assertEqual(last_image['height'], 365)

    def test_image_dimensions(self):
        url = 'http://lassie.it/core/image_dimensions.html'

        l = Lassie()
        data = l.fetch(url, all_images=True)

        self.assertEqual(len(data['images']), 4)

        image = data['images'][0]
        self.assertEqual(image['width'], 100)
        self.assertEqual(image['height'], 100)

        image = data['images'][1]
        self.assertEqual(image['width'], 100)
        self.assertEqual(image['height'], 100)

        image = data['images'][2]
        self.assertEqual(image['width'], 100)
        self.assertEqual(image['height'], 100)

        image = data['images'][3]
        self.assertEqual(image['width'], 100)
        self.assertEqual(image['height'], 100)

    def test_bad_image_dimensions(self):
        url = 'http://lassie.it/core/bad_image_dimensions.html'

        l = Lassie()
        data = l.fetch(url, all_images=True)

        # lassie.utils.convert_to_int will except a TypeError or ValueError and pass (not setting a width/height on the image)
        image = data['images'][0]
        self.assertTrue(not 'width' in image)
        self.assertTrue(not 'height' in image)

    def test_request_opts(self):
        l = Lassie()
        l.request_opts = {
            'headers': {
                'User-Agent': 'lassie python',
            },
            'timeout': 3
        }

        self.assertTrue(set(('headers', 'timeout')).issubset(l.request_opts))

        # If they modify one of the keys value, make sure it actually happened
        l.request_opts['headers'].update({'Content-Type': 'application/json'})
        self.assertEqual(len(l.request_opts['headers']), 2)
        self.assertTrue(set(('User-Agent', 'Content-Type')).issubset(l.request_opts['headers']))

    def test_bad_request_opts(self):
        l = Lassie()
        l.request_opts = {
            'bad_key': True,
            'headers': {
                'User-Agent': 'lassie python'
            }
        }

        self.assertTrue('bad_key' not in l.request_opts)
        self.assertTrue('headers' in l.request_opts)

    def test_core_bad_keywords(self):
        url = 'http://lassie.it/core/bad_keywords.html'

        l = Lassie()
        data = l.fetch(url)
        self.assertEqual(data.get('keywords'), [])
