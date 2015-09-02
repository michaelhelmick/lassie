# -*- coding: utf-8 -*-

"""
lassie.filters.generic
~~~~~~~~~~~~~~~~~~~~~~

This module contains data about generic type content to help Lassie filter for content.

"""

from ..compat import str

import re

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
