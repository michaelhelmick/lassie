# -*- coding: utf-8 -*-

"""
lassie.filters.providers
~~~~~~~~~~

This module contains oembed providers and a python oembed consumer.

"""

import re

import oembed

from ...utils import convert_to_int

HYPERLINK_PATTERN = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

PROVIDERS = {
    'http://www.youtube.com/oembed': [
        'https?://*.youtube.com/watch*',
        'https?://*.youtube.com/v/*',
        'https?://youtu.be/*',
        'https?://*.youtube.com/user/*',
        'https?://*.youtube.com/*#*/*',
        'https?://m.youtube.com/index*',
        'https?://*.youtube.com/profile*',
        'https?://*.youtube.com/view_play_list*',
        'https?://*.youtube.com/playlist*'
    ]
}

consumer = oembed.OEmbedConsumer()
for k, v in PROVIDERS.items():
    endpoint = oembed.OEmbedEndpoint(k, v)
    consumer.addEndpoint(endpoint)


def parse_oembed_data(oembed_data, data):
    """Parse OEmbed response data to inject into lassie's response dict.

    :param oembed_data: OEmbed response data.
    :type oembed_data: dict
    :param data: Refrence to data variable being updated.
    :type data: dict

    """
    data.update({
        'oembed': oembed_data,
    })
    _type = oembed_data.get('type')
    provider_name = oembed_data.get('provider_name')
    if not _type:
        return data

    if oembed_data.get('title'):
        data.update({
            'title': oembed_data.get('title'),
        })

    if _type == 'video':
        try:
            item = {
                'width': convert_to_int(oembed_data.get('width')),
                'height': convert_to_int(oembed_data.get('height'))
            }
            if provider_name in ['YouTube', ]:
                item['src'] = HYPERLINK_PATTERN.search(oembed_data.get('html')).group(0)

            data['videos'].append(item)
        except Exception:
            pass

        if oembed_data.get('thumbnail_url'):
            item = {
                'width': convert_to_int(oembed_data.get('thumbnail_width')),
                'height': convert_to_int(oembed_data.get('thumbnail_height')),
                'src': oembed_data.get('thumbnail_url')
            }

            data['images'].append(item)

    return data
