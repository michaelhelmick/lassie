# -*- coding: utf-8 -*-

"""
lassie.filters.generic
~~~~~~~~~~~~~~~~~~~~~~

This module contains data about generic type content to help Lassie filter for content.

"""

import re

from ..compat import str

GENERIC_MAPS = {
    'meta': {
        'generic': {
            'pattern': re.compile(r"^(description|keywords|title)", re.I),
            'map': {
                'description': 'description',
                'keywords': 'keywords',
                'title': 'title',
            },
            'image_key': '',
            'video_key': '',
            'key': 'name',
        },
    },
    'link': {
        'favicon': {
            'pattern': 'icon',
            'key': 'rel',
            'type': str('favicon'),
        },
        'canonical': {
            'pattern': 'canonical',
            'key': 'rel',
            'type': 'url'
        }
    },
}
