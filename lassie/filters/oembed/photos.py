# -*- coding: utf-8 -*-

"""
lassie.filters.oembed.photos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains photo services that provide oembed data

"""

from ...compat import str

import re


OEMBED_PHOTOS_MAPS = [
    {
        'name': 'Flickr',
        'pattern': re.compile('http://(www\.flickr\.com/photos/.*|flic\.kr/.*)', re.I),
        'endpoint': 'http://www.flickr.com/services/oembed',
        'querystring': {'format':'json'},
        'map': [{
                'array': 'links',
                'url': 'src',
                'width': 'width',
                'height': 'height',
                'type': 'image',
                'rel': 'original',
            }, {
                'array': 'links',
                'thumbnail_url': 'src',
                'thumbnail_width': 'width',
                'thumbnail_height': 'height',
                'type': 'image',
                'rel': 'thumbnail',
            }, {
                'array': 'meta',
                'author_name': ('author', 'name',),
                'author_url': ('author', 'url',),

                'web_page_short_url': 'short_url',
                'web_page': 'url',

                'type': 'type',
            }
        ],
    },
]
