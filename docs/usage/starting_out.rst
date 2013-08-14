.. _starting-out:

Starting Out
============

This section out lines the most basic uses of Lassie

*******************************************************************************

What Lassie Returns
-------------------

Lassie aims to return the most beautifully crafted dictionary of important information about the web page.

Beginning
---------

So, let's say you want to retrieve details about a YouTube video.

Specifically: http://www.youtube.com/watch?v=dQw4w9WgXcQ

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
        }],
        'locale': u'en_US'
    }

Or what if you wanted to get information about an article?

Specifically: http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/

.. code-block:: python

    >>> import lassie
    >>> lassie.fetch('http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/')
    {
        'description': u"GitHub has surpassed the 3 million-developer mark, a milestone for the collaborative platform for application development.\xa0GitHub said it happened Monday night on the first day of the company's\xa0all-hands winter summit. Launched\xa0in April 2008, GitHub\xa0celebrated\xa0its first million users in..",
        'videos': [],
        'title': u'GitHub Passes The 3 Million Developer Mark | TechCrunch',
        'url': u'http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/',
        'locale': u'en_US',
        'images': [{
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png?w=150',
            'type': u'og:image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png',
            'type': u'twitter:image'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }]
    }

Lassie, by default, also filters for content from Twitter Cards, grab favicons and touch icons.

Priorities
----------

Open Graph values takes priority over other values (Twitter Card data, generic data, etc.)

In other words, if a website has the title of their page as ``<title>YouTube</title>`` and they have their Open Graph title set ``<meta property="og:title" content="YouTube | A Video Sharing Site" />``

The value of ``title`` when you ``fetch`` the web page will return as "YouTube | A Video Sharing Site" instead of just "YouTube".

But what if I don't want open graph data?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Then pass ``open_graph=False`` to the ``fetch`` method.

.. code-block:: python

    >>> lassie.fetch('http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/', open_graph=False)
    {
        'description': u"GitHub has surpassed the 3 million-developer mark, a milestone for the collaborative platform for application development.\xa0GitHub said it happened Monday night on the first day of the company's\xa0all-hands winter summit. Launched\xa0in April 2008, GitHub\xa0celebrated\xa0its first million users in..",
        'videos': [],
        'title': u'GitHub Passes The 3 Million Developer Mark | TechCrunch',
        'url': u'http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/',
        'locale': u'en_US',
        'images': [{
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png?w=150',
            'type': u'og:image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png',
            'type': u'twitter:image'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }]
    }

If you **don't** want Twitter cards, favicons or touch icons, use any combination of the following parameters and pass them to ``fetch``:

- Pass ``twitter_card=False`` to exclude Twitter Card data from being filtered
- Pass ``touch_icon=False`` to exclude the Apple touch icons from being added to the images array
- Pass ``favicon=False`` to exclude the favicon from being added to the images array

Obtaining All Images
--------------------

Sometimes you might want to obtain a list of all the images on a web page... simple, just pass ``all_images=True`` to ``fetch``.

.. code-block:: python

    >>> lassie.fetch('http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/', all_images=True)
    {
        'description': u"GitHub has surpassed the 3 million-developer mark, a milestone for the collaborative platform for application development.\xa0GitHub said it happened Monday night on the first day of the company's\xa0all-hands winter summit. Launched\xa0in April 2008, GitHub\xa0celebrated\xa0its first million users in..",
        'videos': [],
        'title': u'GitHub Passes The 3 Million Developer Mark | TechCrunch',
        'url': u'http://techcrunch.com/2013/01/16/github-passes-the-3-million-developer-mark/',
        'locale': u'en_US',
        'images': [{
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png?w=150',
            'type': u'og:image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png',
            'type': u'twitter:image'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/favicon.ico?m=1357660109g',
            'type': u'favicon'
        }, {
            'src': u'http://s2.wp.com/wp-content/themes/vip/tctechcrunch2/images/site-logo-cutout.png?m=1342508617g',
            'alt': u'',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/countdown5a.jpg?w=640',
            'alt': u'Main Event Page',
            'type': u'body_image'
        }, {
            'src': u'http://2.gravatar.com/avatar/b4e205744ae2f9b44921d103b4d80e54?s=60&d=identicon&r=G',
            'alt': u'',
            'type': u'body_image',
            'width': 60
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/01/github-logo.png?w=300',
            'alt': u'github-logo',
            'type': u'body_image',
            'width': 300
        }, {
            'src': u'http://crunchbase.com/assets/images/resized/0001/7208/17208v9-max-150x150.png',
            'alt': u'',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/tardis-egg.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/htc.png?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/04/apple1.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/p9130014.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/screen-shot-2013-08-13-at-8-18-25-pm.png?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/24112v5-max-250x250.jpg?w=89&h=63&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/flexible-display.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/screen-shot-2013-08-14-at-11-52-50-am.png?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/screen-shot-2013-08-14-at-10-23-20-am.png?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/google-quick-answer-hotel-1-png.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/ashton-kutcher-jobs.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/surface-14.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/peter-deng-instagram.jpg?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }, {
            'src': u'http://tctechcrunch2011.files.wordpress.com/2013/08/marketplace-flow.png?w=89&h=64&crop=1',
            'alt': '',
            'type': u'body_image'
        }]
    }

*******************************************************************************

So, now you know the basics. What if you don't want to declare params *every* time to the ``fetch`` method? Head over to the :ref:`advanced usage <advanced-usage>` section to learn about the ``Lassie`` class.
