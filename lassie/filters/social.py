# -*- coding: utf-8 -*-

"""
lassie.filters.social
~~~~~~~~~~~~~~~~~~~~~

This module contains data social related content to help Lassie filter for content.

"""

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
                'og:image:width': 'width',
                'og:image:height': 'height',

                'og:video': 'src',
                'og:video:width': 'width',
                'og:video:height': 'height',
                'og:video:type': 'type',
            },
            'image_key': u'og:image',
            'video_key': u'og:video',
            'key': 'property',
        },
        'twitter_card': {  # https://dev.twitter.com/docs/cards
            'pattern': re.compile(r"^twitter:", re.I),
            'map': {
                'twitter:url': 'url',
                'twitter:title': 'title',
                'twitter:description': 'description',
                'twitter:locale': 'locale',

                'twitter:image': 'src',
                'twitter:image:width': 'width',
                'twitter:image:height': 'height',

                'twitter:player': 'src',
                'twitter:player:width': 'width',
                'twitter:player:height': 'height',
                'twitter:player:content_type': 'type',
            },
            'image_key': u'twitter:image',
            'video_key': u'twitter:player',
            'key': 'name',
        },
    }
}
