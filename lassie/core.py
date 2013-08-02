# -*- coding: utf-8 -*-

"""
lassie.core
~~~~~~~~~~~

This module contains a Lassie object to maintain settings across lassie.

"""

from bs4 import BeautifulSoup
import requests

from .compat import urljoin, str, basestring
from .exceptions import LassieException
from .filters import APPLE_TOUCH_ICON_PATTERN, FILTER_MAPS
from .utils import clean_text


class Lassie(object):
    def __init__(self, parser='html5lib'):
        """Instantiates an instance of Lassie.

        :param parser: (optional) The parsing library for BeautifulSoup to use
        :type parser: string
        """
        self.parser = parser

    def __repr__(self):
        return '<Lassie [%s]>' % (self.parser)

    def fetch(self, url, open_graph=True, twitter_card=True, touch_icon=True, favicon=True, all_images=False):
        """Retrieves content from the specified url, parses it, and returns
        a beautifully crafted dictionary of important information about that
        web page.

        Priority tree is as follows:
            1. Open Graph
            2. Twitter Card
            3. Other meta content (i.e. description, keywords)

        :param url: URL to send a GET request to
        :param open_graph: (optional) If ``True``, filters web page content for Open Graph meta tags. The content of these properties have top priority on return values.
        :type open_graph: bool
        :param twitter_card: (optional) If ``True``, filters web page content for Twitter Card meta tags
        :type twitter_card: bool
        :param touch_icon: (optional) If ``True``, retrieves Apple touch icons and includes them in the response ``images`` array
        :type touch_icon: bool
        :param: favicon: (optional) If ``True``, retrieves any favicon images and includes them in the response ``images`` array
        :type favicon: bool
        :param all_images: (optional) If ``True``, retrieves images inside web pages body and includes them in the response ``images`` array. Default: False
        :type all_images: bool

        """

        html = self._retreive_content(url)
        if not html:
            raise LassieException('There was no content to parse.')

        soup = BeautifulSoup(clean_text(html), self.parser)

        data = {
            'images': [],
            'videos': [],
        }

        if open_graph:
            data.update(self._filter_meta_data('open_graph', soup, data))

        if twitter_card:
            data.update(self._filter_meta_data('twitter_card', soup, data))

        data.update(self._filter_meta_data('generic', soup, data))

        if touch_icon:
            data.update(self._get_touch_icon(soup, data, url))

        if favicon:
            data.update(self._get_favicon(soup, data, url))

        if all_images:
            # Maybe filter out 1x1?
            data.update(self._find_all_images(soup, data))

        # TODO: Find a good place for this
        if not 'url' in data:
            data['url'] = url

        if not 'title' in data:
            print 'fasfa'
            data['title'] = soup.find('title').string

        return data

    def _retreive_content(self, url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise LassieException(e)
        else:
            return response.text

        return ''

    def _filter_meta_data(self, source, soup, data):
        meta = FILTER_MAPS[source]['meta']
        meta_map = meta['map']

        html = soup.find_all('meta', {meta['key']: meta['pattern']})

        image = {}
        video = {}

        for line in html:
            prop = line.get(meta['key'])
            value = line.get('content')

            if prop in meta_map and not meta_map[prop] in data:
                # this could be bad in cases where any values that the property
                # is mapped up to (i.e. "src", "type", etc) are found in ``data``
                # TODO: Figure out a smoother way to prevent conflicts ^^^^^^^^
                image_prop = meta['image_key']
                video_prop = meta['video_key']

                if prop.startswith((image_prop, video_prop)) and \
                prop.endswith(('width', 'height')):
                    try:
                        value = int(value)
                    except ValueError:
                        value = 0

                if prop == 'keywords':
                    value = value.split(',')



                if image_prop and prop.startswith(image_prop):
                    image[meta_map[prop]] = value
                elif video_prop and prop.startswith(video_prop):
                    video[meta_map[prop]] = value
                else:
                    print prop, value
                    data[meta_map[prop]] = value

        if image:
            image['type'] = image_prop
            data['images'].append(image)
        if video:
            data['videos'].append(video)

        return data

    def _get_touch_icon(self, soup, data, url):
        # Maybe do a filter for link rels like we are for meta?
        touch_icon_data = soup.find_all('link', {'rel': APPLE_TOUCH_ICON_PATTERN})
        for touch_icon in touch_icon_data:
            data['images'].append({
                'src': urljoin(url, touch_icon.get('href')),
                'type': u'touch_icon'
            })

        return data

    def _get_favicon(self, soup, data, url):
        favicon_data = soup.find_all('link', {'rel': 'icon'})
        for favicon in favicon_data:
            data['images'].append({
                'src': urljoin(url, favicon.get('href')),
                'type': u'favicon'
            })

        return data

    def _find_all_images(self, soup, data):
        body_images = soup.findAll('img')
        for image in body_images:
            data['images'].append({
                'src': image.get('src'),
                'alt': image.get('alt', ''),
                'type': u'body_image',
                'width': int(image.get('width', 0)),
                'height': int(image.get('height', 0)),
            })

        return data
