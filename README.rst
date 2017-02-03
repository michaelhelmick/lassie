Lassie
======

.. image:: https://img.shields.io/pypi/v/lassie.svg?style=flat-square
  :target: https://pypi.python.org/pypi/lassie 
 
.. image:: https://img.shields.io/travis/michaelhelmick/lassie.svg?style=flat-square
  :target: https://travis-ci.org/michaelhelmick/lassie 

.. image:: https://img.shields.io/coveralls/michaelhelmick/lassie/master.svg?style=flat-square
  :target: https://coveralls.io/r/michaelhelmick/lassie?branch=master
  
.. image:: https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg
    :target: https://saythanks.io/to/michaelhelmick

Lassie is a Python library for retrieving basic content from websites.

.. image:: https://i.imgur.com/QrvNfAX.gif

Usage
-----

.. code-block:: python

    >>> import lassie
    >>> lassie.fetch('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
    {
        'description': u'Music video by Rick Astley performing Never Gonna Give You Up. YouTube view counts pre-VEVO: 2,573,462 (C) 1987 PWL',
        'videos': [{
            'src': u'http://www.youtube.com/v/dQw4w9WgXcQ?autohide=1&version=3',
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
        'keywords': [u'Rick', u'Astley', u'Sony', u'BMG', u'Music', u'UK', u'Pop'],
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
        }],
        'locale': u'en_US'
    }

Install
-------

Install Lassie via `pip <http://www.pip-installer.org/>`_

.. code-block:: bash

    $ pip install lassie

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_

.. code-block:: bash

    $ easy_install lassie

But, hey... `that's up to you <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_.

Documentation
-------------

Documentation can be found here: https://lassie.readthedocs.org/

