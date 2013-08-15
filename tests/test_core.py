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
