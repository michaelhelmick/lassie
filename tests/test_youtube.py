import pytest

from lassie import Lassie


@pytest.mark.usefixtures('mock_retrieve_oembed_data')
def test_youtube_good():
    url = 'http://lassie.it/youtube/good.json'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['videos']) == 1
    assert len(data['images']) == 1


def test_bad_url():
    url = 'http://lassie.it/youtube/bad_url_123456.json'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert data.get('oembed') is None


def test_youtube_bad_html():
    url = 'http://lassie.it/youtube/bad_html.json'

    lassie = Lassie()
    lassie.fetch(url)


def test_youtube_no_type():
    url = 'http://lassie.it/youtube/no_type.json'

    lassie = Lassie()
    lassie.fetch(url)


@pytest.mark.usefixtures('mock_retrieve_oembed_data')
def test_youtube_no_thumb():
    url = 'http://lassie.it/youtube/no_thumb.json'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['videos']) == 1
    assert len(data['images']) == 0
