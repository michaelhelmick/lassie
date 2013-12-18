# -*- coding: utf-8 -*-

"""
lassie.filters.oembed
~~~~~~~~~~~~~~~~~~~~~

This module provides oembed data for audio, video, photos, products, and other services

"""

from .photos import OEMBED_PHOTOS_MAPS

OMITTED_OEMBED_KEYS = ['array', 'type', 'rel']

OEMBED_PROVIDERS_MAPS = OEMBED_PHOTOS_MAPS
