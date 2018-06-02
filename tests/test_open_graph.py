import lassie


def test_open_graph_all_properties():
    url = 'http://lassie.it/open_graph/all_properties.html'
    data = lassie.fetch(url)

    assert data['url'] == url
    assert data['title'] == 'Lassie Open Graph All Properies Test'
    assert data['description'] == 'Just a test template with OG data!'
    assert data['locale'] == 'en_US'
    assert data['site_name'] == 'Lassie'

    assert len(data['images']) == 1
    image = data['images'][0]
    assert image['src'] == 'http://i.imgur.com/cvoR7zv.jpg'
    assert image['width'] == 550
    assert image['height'] == 365
    assert image['type'] == 'og:image'

    assert len(data['videos']) == 1
    video = data['videos'][0]
    assert video['src'] == 'http://www.youtube.com/v/dQw4w9WgXcQ?version=3&autohide=1'
    assert video['width'] == 640
    assert video['height'] == 480
    assert video['type'] == 'application/x-shockwave-flash'


def test_open_graph_no_og_title_no_og_url():
    url = 'http://lassie.it/open_graph/no_og_title_no_og_url.html'
    data = lassie.fetch(url)

    assert data['url'] == url
    assert data['title'] == 'Lassie Open Graph Test | No og:title, No og:url'


def test_open_graph_og_image_plus_two_body_images():
    url = 'http://lassie.it/open_graph/og_image_plus_two_body_images.html'
    data = lassie.fetch(url)

    # Try without passing "all_images", then pass it

    assert len(data['images']) == 1

    data = lassie.fetch(url, all_images=True)

    assert len(data['images']) == 3

    image_0 = data['images'][0]
    image_1 = data['images'][1]
    image_2 = data['images'][2]
    assert image_0['type'] == 'og:image'
    assert image_1['type'] == 'body_image'
    assert image_2['type'] == 'body_image'


def test_open_graph_og_image_relative_url():
    url = 'http://lassie.it/open_graph/og_image_relative_url.html'
    data = lassie.fetch(url)

    assert data['images'][0]['src'] == 'http://lassie.it/open_graph/name.jpg'
