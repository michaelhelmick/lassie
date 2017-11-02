import json
import mimetypes
import unittest

from mock import patch

from lassie.compat import urlparse
from lassie.core import Lassie


def _mock_retrieve_oembed_data(mock, url):
    if '.json' not in url:
        return {}, 404

    filename = urlparse(url).path
    _file = open('./json%s' % filename, 'r')
    content = _file.read()
    _file.close()

    status_code = 200

    return json.loads(content), status_code


def _mock_retrieve_content(mock, url):
    if '.html' not in url:
        filename = '/generic/all_properties.html'
    else:
        filename = urlparse(url).path

    _file = open('./templates%s' % filename, 'r')
    content = _file.read()
    _file.close()

    status_code = 200

    return content, status_code


def _mock_retrieve_headers(mock, url):
    filename = urlparse(url).path

    headers = {
        'Content-Type': mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    }

    status_code = 200

    return headers, status_code


class LassieBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.patch = patch.object(Lassie, '_retrieve_content', _mock_retrieve_content)
        self.patch2 = patch.object(Lassie, '_retrieve_headers', _mock_retrieve_headers)
        self.patch3 = patch.object(Lassie, '_retrieve_oembed_data', _mock_retrieve_oembed_data)

        self.patch.start()
        self.patch2.start()
        self.patch3.start()

    def tearDown(self):
        self.patch.stop()
        self.patch2.stop()
        self.patch3.stop()
