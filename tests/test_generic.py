import lassie


def test_generic_all_properties():
    url = 'http://lassie.it/generic/all_properties.html'
    data = lassie.fetch(url, canonical=True)

    assert data['locale'] == 'en_US'
    assert data['title'] == 'Lassie Generic Test | all_properties'
    assert data['description'] == 'Just a random description of a web page.'
    assert data['url'] == 'http://example.com/canonical/path'
    assert len(data['keywords']) == 5


def test_generic_bad_locale():
    url = 'http://lassie.it/generic/bad_locale.html'
    data = lassie.fetch(url)

    assert 'locale' not in data


def test_generic_favicon():
    url = 'http://lassie.it/generic/favicon.html'
    data = lassie.fetch(url)

    assert len(data['images']) == 1
    image = data['images'][0]

    assert image['type'] == 'favicon'


def test_no_title():
    url = 'http://lassie.it/generic/no_title.html'
    data = lassie.fetch(url)

    assert 'title' not in data


def test_canonical():
    url = 'http://lassie.it/generic/canonical.html'
    data = lassie.fetch(url, canonical=True)

    assert data['url'] == 'http://example.com/canonical/path'
