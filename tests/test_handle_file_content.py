import pytest

import lassie


@pytest.mark.usefixtures('mock_retrieve_headers')
def test_image_file():
    url = 'http://lassie.it/handle_file_content/image_file.jpg'
    data = lassie.fetch(url, handle_file_content=True)

    assert data['url'] == url
    assert data['title'] == 'image_file.jpg'

    assert len(data['images']) == 1
    image = data['images'][0]
    assert image['src'] == 'http://lassie.it/handle_file_content/image_file.jpg'
    assert image['type'] == 'body_image'
