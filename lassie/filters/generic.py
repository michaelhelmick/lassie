# -*- coding: utf-8 -*-

"""
lassie.filters.generic
~~~~~~~~~~~~~~~~~~~~~~

This module contains data about generic type content to help Lassie filter for content.

"""

import re

GENERIC_MAPS = {
    'meta': {
        'generic': {
            'pattern': re.compile(r"^(description|keywords)", re.I),
            'map': {
                'description': 'description',
                'keywords': 'keywords',
            },
            'image_key': '',
            'video_key': '',
            'key': 'name',
        },
    },
    'link': {
        'favicon': {
            'pattern': 'icon',
            'key': 'icon',
            'type': u'favicon',
        },
    },
}
