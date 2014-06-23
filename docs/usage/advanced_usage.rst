.. _advanced-usage:

Advanced Usage
==============

This section will cover how to use the ``Lassie`` class to maintain settings across all ``fetch`` calls.


Class Level Attributes
----------------------

Constructing a ``Lassie`` class and calling ``fetch`` will use all the default params that are available to ``fetch``.

.. code-block:: python

    >>> from lassie import Lassie
    >>> l = Lassie()

    >>> l.fetch('https://github.com/michaelhelmick')
    {
        'images': [{
            'src': u'https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png',
            'type': u'og:image'
        }, {
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/michaelhelmick',
        'description': u'michaelhelmick has 22 repositories written in Python, Shell, and JavaScript. Follow their code on GitHub.',
        'videos': [],
        'title': u'michaelhelmick (Mike Helmick) \xb7 GitHub'
    }
    >>> l.fetch('https://github.com/ashibble')
    {
        'images': [{
            'src': u'https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png',
            'type': u'og:image'
        }, {
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/ashibble',
        'description': u'Follow ashibble on GitHub and watch them build beautiful projects.',
        'videos': [],
        'title': u'ashibble (Alexander Shibble) \xb7 GitHub'
    }

If you decide that you don't want to filter for Open Graph data, instead of declaring ``open_graph=False`` in every ``fetch`` call:

.. code-block:: python

    >>> import lassie
    >>> l = Lassie()
    >>> l.fetch('https://github.com/michaelhelmick', open_graph=False)
    >>> l.fetch('https://github.com/ashibble', open_graph=False)

You can use the ``Lassie`` class and set attibutes on the class.

.. code-block:: python

    >>> from lassie import Lassie
    >>> l = Lassie()
    >>> l.open_graph = False

    >>> l.fetch('https://github.com/michaelhelmick')
    {
        'images': [{
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/michaelhelmick',
        'description': u'michaelhelmick has 22 repositories written in Python, Shell, and JavaScript. Follow their code on GitHub.',
        'videos': [],
        'title': u'michaelhelmick (Mike Helmick) \xb7 GitHub'
    }
    >>> l.fetch('https://github.com/ashibble')
    {
        'images': [{
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/ashibble',
        'description': u'Follow ashibble on GitHub and watch them build beautiful projects.',
        'videos': [],
        'title': u'ashibble (Alexander Shibble) \xb7 GitHub'
    }

You'll notice the data for the Open Graph properties wasn't returned in the last responses. That's because passing ``open_graph=False`` tells Lassie to not filter for those properties.

In the edge case that there is a time or two you want to override the class attribute, just pass the parameter to ``fetch`` and Lassie will use that parameter.

.. code-block:: python

    >>> from lassie import Lassie
    >>> l = Lassie()
    >>> l.open_graph = False

    >>> l.fetch('https://github.com/michaelhelmick')
    {
        'images': [{
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/michaelhelmick',
        'description': u'michaelhelmick has 22 repositories written in Python, Shell, and JavaScript. Follow their code on GitHub.',
        'videos': [],
        'title': u'michaelhelmick (Mike Helmick) \xb7 GitHub'
    }
    >>> l.fetch('https://github.com/ashibble', open_graph=True)
    {
        'images': [{
            'src': u'https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png',
            'type': u'og:image'
        }, {
            'src': u'https://github.com/favicon.ico',
            'type': u'favicon'
        }],
        'url': 'https://github.com/ashibble',
        'description': u'Follow ashibble on GitHub and watch them build beautiful projects.',
        'videos': [],
        'title': u'ashibble (Alexander Shibble) \xb7 GitHub'
    }


Manipulate the Request (headers, proxies, etc.)
-----------------------------------------------

There are times when you may want to turn SSL verification off, send custom headers, or add proxies for the request to go through.

Lassie uses the `requests <http://python-requests.org>`_ library to make web requests. ``requests`` accepts a few parameters to allow developers to manipulate the acutal HTTP request.

Here is an example of sending custom headers to a lassie request:

.. code-block:: python

    from lassie import Lassie

    l = Lassie()
    l.request_opts = {
        'headers': {
            'User-Agent': 'python lassie'
        }
    }
    l.fetch('http://google.com')

Maybe you want to set a request timeout, here's another example:

.. code-block:: python

    from lassie import Lassie

    l = Lassie()
    l.request_opts = {
        'timeout': 10  # 10 seconds
    }

    # If the response takes longer than 10 seconds this request will fail
    l.fetch('http://google.com')


Playing Nice with non-HTML Files
--------------------------------

Sometimes, you may want to grab information about an image or other type of file. Although only images are supported, you can retrieve a nicely structured ``dict``

Pass ``handle_file_content=True`` to ``lassie.fetch`` or set it on a ``Lassie`` instance

.. code-block:: python

    >>> from lassie import Lassie

    >>> lassie.fetch('https://camo.githubusercontent.com/d19b279de191489445d8cfd39faf93e19ca2df14/68747470733a2f2f692e696d6775722e636f6d2f5172764e6641582e676966', handle_file_content=True)
    {
        'title': '68747470733a2f2f692e696d6775722e636f6d2f5172764e6641582e676966',
        'videos': [],
        'url': 'https://camo.githubusercontent.com/d19b279de191489445d8cfd39faf93e19ca2df14/68747470733a2f2f692e696d6775722e636f6d2f5172764e6641582e676966',
        'images': [{
            'src': 'https://camo.githubusercontent.com/d19b279de191489445d8cfd39faf93e19ca2df14/68747470733a2f2f692e696d6775722e636f6d2f5172764e6641582e676966'
        }]
    }

    >>> lassie.fetch('http://2.bp.blogspot.com/-vzGgFFtW-VY/Tz-eozaHw3I/AAAAAAAAM3k/OMvxpFYr23s/s1600/The-best-top-desktop-cat-wallpapers-10.jpg', handle_file_content=True)
    {
        'title': 'The-best-top-desktop-cat-wallpapers-10.jpg',
        'images': [{
            'src': 'http://2.bp.blogspot.com/-vzGgFFtW-VY/Tz-eozaHw3I/AAAAAAAAM3k/OMvxpFYr23s/s1600/The-best-top-desktop-cat-wallpapers-10.jpg'
        }],
        'videos': [],
        'url': 'http://2.bp.blogspot.com/-vzGgFFtW-VY/Tz-eozaHw3I/AAAAAAAAM3k/OMvxpFYr23s/s1600/The-best-top-desktop-cat-wallpapers-10.jpg'
    }
