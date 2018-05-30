import lassie

from .base import LassieBaseTestCase


class LassieFileContentTestCase(LassieBaseTestCase):
    def test_image_file(self):
        url = 'http://lassie.it/handle_file_content/image_file.jpg'
        data = lassie.fetch(url, handle_file_content=True)

        self.assertEqual(data['url'], url)
        self.assertEqual(data['title'], 'image_file.jpg')

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]
        self.assertEqual(image['src'],
                         'http://lassie.it/handle_file_content/image_file.jpg')
        self.assertEqual(image['type'], 'body_image')
