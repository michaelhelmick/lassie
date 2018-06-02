import pytest

from lassie import Lassie, LassieError
from lassie.utils import FAKE_USER_AGENT


def test_core_class_vs_method_settings():
    url = 'http://lassie.it/core/class_vs_method_settings.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 1

    lassie.open_graph = False
    data = lassie.fetch(url)

    # open_graph is set to False so there shouldn't be any images in the list this
    # time around
    assert len(data['images']) == 0


def test_core_class_setting_is_none():
    url = 'http://lassie.it/core/class_setting_is_none.html'

    # This is a really odd use-case where they'd set the class attr to None, but it
    # might happen so oh wellz.
    lassie = Lassie()
    lassie.open_graph = None
    data = lassie.fetch(url, open_graph=False)

    assert len(data['images']) == 0


def test_core_no_content_raises_error():
    url = 'http://lassie.it/core/empty.html'

    lassie = Lassie()
    with pytest.raises(LassieError):
        lassie.fetch(url)


def test_core_retrieve_all_images():
    url = 'http://lassie.it/core/retrieve_all_images.html'

    lassie = Lassie()
    lassie.all_images = True

    data = lassie.fetch(url)
    assert len(data['images']) == 3

    last_image = data['images'][2]
    assert last_image['width'] == 550
    assert last_image['height'] == 365


def test_image_dimensions():
    url = 'http://lassie.it/core/image_dimensions.html'

    lassie = Lassie()
    data = lassie.fetch(url, all_images=True)

    assert len(data['images']) == 4

    image = data['images'][0]
    assert image['width'] == 100
    assert image['height'] == 100

    image = data['images'][1]
    assert image['width'] == 100
    assert image['height'] == 100

    image = data['images'][2]
    assert image['width'] == 100
    assert image['height'] == 100

    image = data['images'][3]
    assert image['width'] == 100
    assert image['height'] == 100


def test_bad_image_dimensions():
    url = 'http://lassie.it/core/bad_image_dimensions.html'

    lassie = Lassie()
    data = lassie.fetch(url, all_images=True)

    # lassie.utils.convert_to_int will except a TypeError or ValueError and pass
    # (not setting a width/height on the image)
    image = data['images'][0]
    assert 'width' not in image
    assert 'height' not in image


def test_request_opts():
    lassie = Lassie()
    lassie.request_opts = {
        'headers': {
            'User-Agent': 'lassie python',
        },
        'timeout': 3
    }

    assert {'headers', 'timeout'}.issubset(lassie.request_opts)

    # If they modify one of the keys value, make sure it actually happened
    lassie.request_opts['headers'].update({'Content-Type': 'application/json'})
    assert len(lassie.request_opts['headers']) == 2
    assert {'User-Agent', 'Content-Type'}.issubset(lassie.request_opts['headers'])


def test_request_opts_no_headers():
    lassie = Lassie()
    lassie.request_opts = {
        'headers': {},
        'timeout': 3
    }

    # headers should be set to {} then User-Agent should be added
    assert lassie.client.headers != {}


def test_request_opts_default_user_agent():
    lassie = Lassie()
    lassie.request_opts = {
        'timeout': 3
    }

    # headers should be set to {} then User-Agent should be added
    assert lassie.client.headers['User-Agent'] == FAKE_USER_AGENT


def test_bad_request_opts():
    lassie = Lassie()
    lassie.request_opts = {
        'bad_key': True,
        'headers': {
            'User-Agent': 'lassie python'
        }
    }

    assert 'bad_key' not in lassie.request_opts
    assert 'headers' in lassie.request_opts


def test_core_bad_keywords():
    url = 'http://lassie.it/core/bad_keywords.html'

    lassie = Lassie()
    data = lassie.fetch(url)
    assert data.get('keywords') == []


def test_merge_request_kwargs():
    lassie = Lassie()
    lassie.request_opts = {
        'timeout': 3,
    }

    request_kwargs = lassie.merge_request_kwargs()
    assert 'timeout' in request_kwargs


def test_prepare_request():
    url = 'http://lassie.it/core/bad_keywords.html'

    lassie = Lassie()
    lassie._prepare_request('HEAD', url=url, headers=lassie.client.headers)


def test_no_html_tag():
    url = 'http://lassie.it/core/no_html_tag.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert 'no_html_tag' in data['title']
