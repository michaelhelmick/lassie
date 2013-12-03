from .base import LassieBaseTestCase

import lassie


class LassieOpenGraphTestCase(LassieBaseTestCase):
    def test_open_graph_all_properties(self):
        url = 'http://lassie.it/open_graph/all_properties.html'
        data = lassie.fetch(url)

        self.assertEqual(data['url'], url)
        self.assertEqual(data['title'], 'Lassie Open Graph All Properies Test')
        self.assertEqual(data['description'], 'Just a test template with OG data!')
        self.assertEqual(data['locale'], 'en_US')

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

    def test_open_graph_no_og_title_no_og_url(self):
        url = 'http://lassie.it/open_graph/no_og_title_no_og_url.html'
        data = lassie.fetch(url)

        self.assertEqual(data['url'], url)
        self.assertEqual(data['title'], 'Lassie Open Graph Test | No og:title, No og:url')

    def test_open_graph_og_image_plus_two_body_images(self):
        url = 'http://lassie.it/open_graph/og_image_plus_two_body_images.html'
        data = lassie.fetch(url)

        # Try without passing "all_images", then pass it

        self.assertEqual(len(data['images']), 1)

        data = lassie.fetch(url, all_images=True)

        self.assertEqual(len(data['images']), 3)

        image_0 = data['images'][0]
        image_1 = data['images'][1]
        image_2 = data['images'][2]
        self.assertEqual(image_0['type'], 'og:image')
        self.assertEqual(image_1['type'], 'body_image')
        self.assertEqual(image_2['type'], 'body_image')

    def test_open_graph_og_image_relative_url(self):
        url = 'http://lassie.it/open_graph/og_image_relative_url.html'
        data = lassie.fetch(url)

        self.assertEqual(
            data['images'][0]['src'], 'http://lassie.it/open_graph/name.jpg')