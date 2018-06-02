from lassie import Lassie


def test_all_properites():
    url = 'http://lassie.it/amp/all_properties.html'

    lassie = Lassie()
    data = lassie.fetch(url, all_images=True)

    assert len(data['images']) == 3

    title = 'Google Glass Is Dead, Long Live Snapchat Spectacles'
    assert data['title'] == title


def test_bad_json():
    url = 'http://lassie.it/amp/bad_json.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert 'amp' in data['url']


def test_str_image():
    url = 'http://lassie.it/amp/str_image.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 1


def test_list_image():
    url = 'http://lassie.it/amp/list_image.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 2


def test_list_image_list():
    url = 'http://lassie.it/amp/list_image_list.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 2


def test_list_image_str():
    url = 'http://lassie.it/amp/list_image_str.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 1


def test_list_image_empty():
    url = 'http://lassie.it/amp/list_image_empty.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 1


def test_list_json():
    url = 'http://lassie.it/amp/list_json.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert 'Pixar' in data['description']


def test_video_objects():
    url = 'http://lassie.it/amp/video_objects.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['videos']) == 1


def test_thumbnail_image():
    url = 'http://lassie.it/amp/thumbnail_image.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 2


def test_list_thumbnail_image():
    url = 'http://lassie.it/amp/list_thumbnail_image.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 2


def test_str_thumbnail_image():
    url = 'http://lassie.it/amp/str_thumbnail_image.html'

    lassie = Lassie()
    data = lassie.fetch(url)

    assert len(data['images']) == 2
