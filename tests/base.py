from lassie.core import Lassie
from lassie.compat import urlparse

from mock import patch
import unittest


def _mock_retreive_content(mock, url):
    filename = urlparse(url).path
    file = open('./templates%s' % filename, 'r')
    html = file.read()
    file.close()

    return html


class LassieBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.patch = patch.object(Lassie, '_retreive_content', _mock_retreive_content)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
