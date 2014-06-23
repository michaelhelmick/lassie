import mimetypes

from lassie.core import Lassie
from lassie.compat import urlparse

from mock import patch
import unittest


def _mock_retrieve_content(mock, url):
    filename = urlparse(url).path
    _file = open('./templates%s' % filename, 'r')
    content = _file.read()
    _file.close()

    return content


def _mock_retrieve_headers(mock, url):
    filename = urlparse(url).path

    headers = {
        'Content-Type': mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    }

    return headers


class LassieBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.patch = patch.object(Lassie, '_retrieve_content', _mock_retrieve_content)
        self.patch2 = patch.object(Lassie, '_retrieve_headers', _mock_retrieve_headers)

        self.patch.start()
        self.patch2.start()

    def tearDown(self):
        self.patch.stop()
        self.patch2.stop()
