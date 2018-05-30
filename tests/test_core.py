from lassie import Lassie, LassieError
from lassie.utils import FAKE_USER_AGENT

from .base import LassieBaseTestCase


class LassieCoreTestCase(LassieBaseTestCase):
    def test_core_class_vs_method_settings(self):
        url = 'http://lassie.it/core/class_vs_method_settings.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertEqual(len(data['images']), 1)

        lassie.open_graph = False
        data = lassie.fetch(url)

        # open_graph is set to False so there shouldn't be any images in the list this
        # time around
        self.assertEqual(len(data['images']), 0)

    def test_core_class_setting_is_none(self):
        url = 'http://lassie.it/core/class_setting_is_none.html'

        # This is a really odd use-case where they'd set the class attr to None, but it
        # might happen so oh wellz.
        lassie = Lassie()
        lassie.open_graph = None
        data = lassie.fetch(url, open_graph=False)

        self.assertEqual(len(data['images']), 0)

    def test_core_no_content_raises_error(self):
        url = 'http://lassie.it/core/empty.html'

        lassie = Lassie()
        self.assertRaises(LassieError, lassie.fetch, url)

    def test_core_retrieve_all_images(self):
        url = 'http://lassie.it/core/retrieve_all_images.html'

        lassie = Lassie()
        lassie.all_images = True

        data = lassie.fetch(url)
        self.assertEqual(len(data['images']), 3)

        last_image = data['images'][2]
        self.assertEqual(last_image['width'], 550)
        self.assertEqual(last_image['height'], 365)

    def test_image_dimensions(self):
        url = 'http://lassie.it/core/image_dimensions.html'

        lassie = Lassie()
        data = lassie.fetch(url, all_images=True)

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

        lassie = Lassie()
        data = lassie.fetch(url, all_images=True)

        # lassie.utils.convert_to_int will except a TypeError or ValueError and pass
        # (not setting a width/height on the image)
        image = data['images'][0]
        self.assertTrue('width' not in image)
        self.assertTrue('height' not in image)

    def test_request_opts(self):
        lassie = Lassie()
        lassie.request_opts = {
            'headers': {
                'User-Agent': 'lassie python',
            },
            'timeout': 3
        }

        self.assertTrue({'headers', 'timeout'}.issubset(lassie.request_opts))

        # If they modify one of the keys value, make sure it actually happened
        lassie.request_opts['headers'].update({'Content-Type': 'application/json'})
        self.assertEqual(len(lassie.request_opts['headers']), 2)
        self.assertTrue(
            {'User-Agent', 'Content-Type'}.issubset(lassie.request_opts['headers'])
        )

    def test_request_opts_no_headers(self):
        lassie = Lassie()
        lassie.request_opts = {
            'headers': {},
            'timeout': 3
        }

        # headers should be set to {} then User-Agent should be added
        self.assertTrue(lassie.client.headers != {})

    def test_request_opts_default_user_agent(self):
        lassie = Lassie()
        lassie.request_opts = {
            'timeout': 3
        }

        # headers should be set to {} then User-Agent should be added
        self.assertTrue(lassie.client.headers['User-Agent'] == FAKE_USER_AGENT)

    def test_bad_request_opts(self):
        lassie = Lassie()
        lassie.request_opts = {
            'bad_key': True,
            'headers': {
                'User-Agent': 'lassie python'
            }
        }

        self.assertTrue('bad_key' not in lassie.request_opts)
        self.assertTrue('headers' in lassie.request_opts)

    def test_core_bad_keywords(self):
        url = 'http://lassie.it/core/bad_keywords.html'

        lassie = Lassie()
        data = lassie.fetch(url)
        self.assertEqual(data.get('keywords'), [])

    def test_merge_request_kwargs(self):
        lassie = Lassie()
        lassie.request_opts = {
            'timeout': 3,
        }

        request_kwargs = lassie.merge_request_kwargs()
        self.assertTrue('timeout' in request_kwargs)

    def test_prepare_request(self):
        url = 'http://lassie.it/core/bad_keywords.html'

        lassie = Lassie()
        lassie._prepare_request('HEAD', url=url, headers=lassie.client.headers)

    def test_no_html_tag(self):
        url = 'http://lassie.it/core/no_html_tag.html'

        lassie = Lassie()
        data = lassie.fetch(url)

        self.assertTrue('no_html_tag' in data['title'])
