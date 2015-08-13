# -*- coding: utf-8 -*-

"""
lassie.filters.social
~~~~~~~~~~~~~~~~~~~~~

This module contains data social related content to help Lassie filter for content.

"""

from ..compat import str

import re

SOCIAL_MAPS = {
    'meta': {
        'open_graph': {  # http://ogp.me/
            'pattern': re.compile(r"^og:", re.I),
            'map': {
                'og:url': 'url',
                'og:title': 'title',
                'og:description': 'description',
                'og:locale': 'locale',

                'og:image': 'src',
                'og:image:url': 'src',
                'og:image:secure_url': 'secure_src',
                'og:image:width': 'width',
                'og:image:height': 'height',
                'og:image:type': 'type',

                'og:video': 'src',
                'og:video:url': 'src',
                'og:video:secure_url': 'secure_src',
                'og:video:width': 'width',
                'og:video:height': 'height',
                'og:video:type': 'type',
            },
            'image_key': str('og:image'),
            'video_key': str('og:video'),
            'key': 'property',
        },
        'twitter_card': {  # https://dev.twitter.com/docs/cards
            'pattern': re.compile(r"^twitter:", re.I),
            'map': {
                'twitter:url': 'url',
                'twitter:title': 'title',
                'twitter:description': 'description',

                'twitter:image': 'src',
                'twitter:image:width': 'width',
                'twitter:image:height': 'height',

                'twitter:player': 'src',
                'twitter:player:width': 'width',
                'twitter:player:height': 'height',
                'twitter:player:content_type': 'type',
            },
            'image_key': str('twitter:image'),
            'video_key': str('twitter:player'),
            'key': 'name',
        },
    }
}
