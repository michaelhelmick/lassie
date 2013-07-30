# -*- coding: utf-8 -*-

"""
lassie.api
~~~~~~~~~~

This module contains core Lassie classes and methods.

"""

from bs4 import BeautifulSoup
import requests

from .exceptions import LassieException
from .helpers import strip_tags, clean_text

import re

OG_META_PATTERN = re.compile(r"^og:(?!image)", re.I)
OG_IMAGE_META_PATTERN = re.compile(r"^og:image", re.I)

GENERIC_META_PATTERN = re.compile(r"^(description|keywords)", re.I)

OG_META_TAGS = {
    'og:url': 'url',
    'og:site_name': 'title',
    'og:description': 'description',
    'og:locale': 'locale',
    'og:image': {
        'og:image': 'src',
        'og:image:width': 'width',
        'og:image:height': 'height',
    }
}

GENERIC_META_TAGS = {
    'description': 'description',
    'keywords': 'keywords',
}

class Lassie(object):
    def __init__(self, parser='html5lib'):
        self.parser = parser

    def fetch(self, url=None, content=None, open_graph=True, all_images=False):
        """
        {
            'url': 'http://google.com',
            'title': '',
            'description': '',
            'locale': '',
            'images': [{
                'width': 0,
                'height': 0,
                'alt': '',
                'src': '',
                'type': ''
            }],
            'keywords': []
        }
        """

        if not content:
            try:
                response = requests.get(url)
            except requests.exceptions.RequestException as e:
                raise LassieException(e)
            else:
                html = clean_text(response.text)
        else:
            html = clean_text(content.read())

        soup = BeautifulSoup(html, self.parser)

        data = {
            'images': [],
        }

        if open_graph:
            data.update(self._get_open_graph_data(soup, data))

        data.update(self._get_generic_data(soup, data))

        if all_images:
            body_images = soup.findAll('img')
            for image in body_images:
                data['images'].append({
                    'src': image.get('src'),
                    'alt': image.get('alt'),
                    'type': 'body_image',
                    'width': int(image.get('width', 0)),
                    'height': int(image.get('height', 0)),
                })

        return data

    def _get_open_graph_data(self, soup, data):
        open_graph_data = soup.find_all('meta', {'property': OG_META_PATTERN})
        open_graph_image = soup.find_all('meta', {'property': OG_IMAGE_META_PATTERN})

        for line in open_graph_data:
            key = line.get('property')
            value = line.get('content')

            for og_tag in OG_META_TAGS:
                if key == og_tag:
                    data[OG_META_TAGS[og_tag]] = value

        image = {}
        for line in open_graph_image:
            key = line.get('property')
            value = line.get('content')

            for og_image_tag in OG_META_TAGS['og:image']:
                if key == og_image_tag:
                    image[OG_META_TAGS['og:image'][og_image_tag]] = value

        if image:
            image['type'] = 'og:image'
            data['images'].append(image)

        return data

    def _get_generic_data(self, soup, data):
        generic_data = soup.find_all('meta', {'name': GENERIC_META_PATTERN})

        for line in generic_data:
            key = line.get('name', '')
            value = line.get('content')

            for generic_tag in GENERIC_META_TAGS:
                general_key = GENERIC_META_TAGS[generic_tag]
                if key == generic_tag and not general_key in data:
                    if key == 'keywords':
                        value = value.split(',')

                    data[general_key] = value

        return data
