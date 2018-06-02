import lassie


def test_twitter_all_properties():
    url = 'http://lassie.it/twitter_card/all_properties.html'
    data = lassie.fetch(url)
    assert data['url'] == 'http://www.youtube.com/watch?v=fWNaR-rxAic'
    assert data['title'] == 'Carly Rae Jepsen - Call Me Maybe'
    assert data['description'] == \
        'Buy Now! http://smarturl.it/CallMeMaybe Music video by Carly Rae Jepsen '\
        'performing Call Me Maybe. (C) 2011 604 Records Inc. #VEVOCertified on June '\
        '8, 2012. h...'

    assert len(data['images']) == 1
    image = data['images'][0]
    assert image['src'] == 'http://i1.ytimg.com/vi/fWNaR-rxAic/maxresdefault.jpg'

    assert len(data['videos']) == 1
    video = data['videos'][0]
    assert video['src'] == 'https://www.youtube.com/embed/fWNaR-rxAic'
    assert video['width'] == 1920
    assert video['height'] == 1080


def test_twitter_no_og_title_use_twitter_title():
    url = 'http://lassie.it/twitter_card/no_og_title_use_twitter_title.html'
    data = lassie.fetch(url)

    assert data['description'] == 'A test case for Lassie!'
    assert data['title'] == 'Lassie Twitter Test | no_og_title_use_twitter_title'
