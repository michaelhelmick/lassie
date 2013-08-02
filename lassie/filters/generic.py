# -*- coding: utf-8 -*-

"""
lassie.filters.generic
~~~~~~~~~~~~~~~~~~~~~~

This module contains data generic type content to help Lassie filter for content.

"""

import re

GENERIC_MAPS = {
    'generic': {
        'meta': {
            'pattern': re.compile(r"^(description|keywords)", re.I),
            'map': {
                'description': 'description',
                'keywords': 'keywords',
            },
            'image_key': '',
            'video_key': '',
            'key': 'name',
        }
    }
}
