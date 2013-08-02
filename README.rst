Lassie
======

Lassie is a Python library for retrieving basic content from websites.

Usage
-----

.. code-block:: python

    >>> import lassie
    >>> lassie.fetch('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    {
        'description': u'Music video by Rick Astley performing Never Gonna Give You Up. YouTube view counts pre-VEVO: 2,573,462 (C) 1987 PWL',
        'videos': [{
            'src': u'http://www.youtube.com/v/dQw4w9WgXcQ?version=3&autohide=1',
            'height': 480,
            'type': u'application/x-shockwave-flash',
            'width': 640
        }, {
            'src': u'https://www.youtube.com/embed/dQw4w9WgXcQ',
            'height': 480,
            'width': 640
        }],
        'title': u'Rick Astley - Never Gonna Give You Up',
        'url': u'http://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'keywords': [u'Rick', u' Astley', u' Sony', u' BMG', u' Music', u' UK', u' Pop'],
        'images': [{
            'src': u'http://i1.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg?feature=og',
            'type': u'og:image'
        }, {
            'src': u'http://i1.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg',
            'type': u'twitter:image'
        }, {
            'src': u'http://s.ytimg.com/yts/img/favicon-vfldLzJxy.ico',
            'type': u'favicon'
        }, {
            'src': u'http://s.ytimg.com/yts/img/favicon_32-vflWoMFGx.png',
            'type': u'favicon'
        }]
    }
