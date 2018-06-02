import json
import mimetypes

import pytest

from lassie.compat import urlparse
from lassie.exceptions import LassieError


@pytest.fixture()
def mock_retrieve_oembed_data(monkeypatch, shared_datadir):
    def mock(self, url):
        if not url.endswith('.json'):
            return {}, 404

        try:
            filename = urlparse(url).path[1:]
            with (shared_datadir / 'json' / filename).open('rt') as f:
                content = f.read()
        except Exception as e:
            raise LassieError(e)

        return json.loads(content), 200

    monkeypatch.setattr('lassie.core.Lassie._retrieve_oembed_data', mock)


@pytest.fixture(autouse=True)
def mock_retrieve_content(monkeypatch, shared_datadir):
    def mock(self, url):
        if not url.endswith('.html'):
            filename = 'generic/all_properties.html'
        else:
            filename = urlparse(url).path[1:]

        with (shared_datadir / filename).open('rt') as f:
            content = f.read()
        return content, 200

    monkeypatch.setattr('lassie.core.Lassie._retrieve_content', mock)


@pytest.fixture()
def mock_retrieve_headers(monkeypatch):
    def mock(self, url):
        filename = urlparse(url).path
        headers = {
            'Content-Type':
                mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        }
        return headers, 200
    monkeypatch.setattr('lassie.core.Lassie._retrieve_headers', mock)
