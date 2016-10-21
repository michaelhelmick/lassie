# -*- coding: utf-8 -*-

"""
lassie.core
~~~~~~~~~~~

This module contains a Lassie object to maintain settings across lassie.

"""

import json
from os.path import basename

import requests
from bs4 import BeautifulSoup

from .compat import str, urljoin, urlparse
from .exceptions import LassieError
from .filters import FILTER_MAPS
from .utils import clean_text, convert_to_int, normalize_image_data, normalize_locale

REQUEST_OPTS = {
    'client': ('cert', 'headers', 'hooks', 'max_redirects', 'proxies'),
    'request': ('timeout', 'allow_redirects', 'stream', 'verify'),
}

IMAGE_MIMETYPES = [
    'image/jpeg', 'image/gif', 'image/bmp', 'image/png'
]


def merge_settings(fetch_setting, class_setting):
    """Merge settings for ``fetch``, method params have priority."""
    if fetch_setting is None:
        return class_setting
    else:
        return fetch_setting


class Lassie(object):
    __attrs__ = [
        'open_graph', 'twitter_card', 'touch_icon', 'favicon',
        'canonical', 'all_images', 'parser', '_retrieve_content',
        'client'
    ]

    def __init__(self):
        """Instantiates an instance of Lassie."""
        self.open_graph = True
        self.twitter_card = True
        self.touch_icon = True
        self.favicon = True
        self.canonical = False
        self.all_images = False
        self.parser = 'html5lib'
        self.handle_file_content = False
        self._request_opts = {}
        self.client = requests.Session()

    @property
    def request_opts(self):
        return self._request_opts

    @request_opts.setter
    def request_opts(self, _dict):
        for k, v in _dict.items():
            if (k in REQUEST_OPTS['client'] or k in REQUEST_OPTS['request']):
                self._request_opts[k] = v
            if k in REQUEST_OPTS['client']:
                setattr(self.client, k, v)


    def __repr__(self):
        return '<Lassie [parser: %s]>' % (self.parser)

    def fetch(self, url, open_graph=None, twitter_card=None, touch_icon=None,
              favicon=None, all_images=None, parser=None, handle_file_content=None,
              canonical=None):
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
        :param favicon: (optional) If ``True``, retrieves any favicon images and includes them in the response ``images`` array
        :type favicon: bool
        :param canonical: (optional) If ``True``, retrieves canonical url from meta tags. Default: False
        :type canonical: bool
        :param all_images: (optional) If ``True``, retrieves images inside web pages body and includes them in the response ``images`` array. Default: False
        :type all_images: bool
        :param parser: (optional) String reference for the parser that BeautifulSoup will use
        :type parser: string
        :param handle_file_content: (optional) If ``True``, lassie will return a generic response when a file is fetched. Default: False
        :type handle_file_content: bool

        """

        # Set params, method params have priority over class params
        open_graph = merge_settings(open_graph, self.open_graph)
        twitter_card = merge_settings(twitter_card, self.twitter_card)
        touch_icon = merge_settings(touch_icon, self.touch_icon)
        favicon = merge_settings(favicon, self.favicon)
        canonical = merge_settings(canonical, self.canonical)
        all_images = merge_settings(all_images, self.all_images)
        parser = merge_settings(parser, self.parser)
        handle_file_content = merge_settings(handle_file_content, self.handle_file_content)

        data = {
            'images': [],
            'videos': [],
        }

        has_file_content = False
        content_type = None
        if handle_file_content:
            headers, status_code = self._retrieve_headers(url)
            content_type = headers.get('Content-Type')
            has_file_content = content_type and not 'text/html' in content_type

        if has_file_content and content_type:
            has_image_content = content_type in IMAGE_MIMETYPES
            if has_image_content:
                parsed_url = urlparse(url)
                data['title'] = basename(parsed_url.path.lstrip('/'))  # TODO: if the url doesn't have an extension, maybe we should match it up to the mimetype and append an ext?
                data['url'] = url
                data['images'].append({
                    'type': 'body_image',
                    'src': url,
                })
        else:
            html, status_code = self._retrieve_content(url)
            if not html:
                raise LassieError('There was no content to parse.')

            soup = BeautifulSoup(clean_text(html), parser)

            self._filter_amp_data(soup, data, url, all_images)

            if open_graph:
                self._filter_meta_data('open_graph', soup, data, url)

            if twitter_card:
                self._filter_meta_data('twitter_card', soup, data)

            self._filter_meta_data('generic', soup, data)

            if touch_icon:
                self._filter_link_tag_data('touch_icon', soup, data, url)

            if favicon:
                self._filter_link_tag_data('favicon', soup, data, url)

            if canonical:
                self._filter_link_tag_data('canonical', soup, data, url)

            if all_images:
                # Maybe filter out 1x1, no "good" way to do this if image doesn't supply width/height
                self._find_all_images(soup, data, url)

            # TODO: Find a good place for setting url, title and locale
            lang = soup.html.get('lang') if soup.html.get('lang') else soup.html.get('xml:lang')
            if lang and (not 'locale' in data):
                locale = normalize_locale(lang)
                if locale:
                    data['locale'] = locale

            if not 'url' in data:
                data['url'] = url

            if not 'title' in data and hasattr(soup.title, 'string'):
                data['title'] = soup.title.string

        data['status_code'] = status_code

        return data

    def _retrieve_headers(self, url):  # pragma: no cover
        request_kwargs = {}
        for k, v in self._request_opts.items():
            if k in REQUEST_OPTS['request']:
                # Set request specific kwarg
                request_kwargs[k] = v

        try:
            response = self.client.head(url, **request_kwargs)
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            raise LassieError(e)

        return response.headers, status_code

    def _retrieve_content(self, url):  # pragma: no cover
        try:
            request_kwargs = {}
            for k, v in self._request_opts.items():
                if k in REQUEST_OPTS['request']:
                    # Set request specific kwarg
                    request_kwargs[k] = v

            response = self.client.get(url, **request_kwargs)
        except requests.exceptions.RequestException as e:
            raise LassieError(e)

        return response.text, response.status_code

    def _filter_meta_data(self, source, soup, data, url=None):
        """This method filters the web page content for meta tags that match patterns given in the ``FILTER_MAPS``

        :param source: The key of the meta dictionary in ``FILTER_MAPS['meta']``
        :type source: string
        :param soup: BeautifulSoup instance to find meta tags
        :type soup: instance
        :param data: The response dictionary to manipulate
        :type data: (dict)

        """
        meta = FILTER_MAPS['meta'][source]
        meta_map = meta['map']

        html = soup.find_all('meta', {meta['key']: meta['pattern']})

        image = {}
        video = {}

        for line in html:
            prop = line.get(meta['key'])
            value = line.get('content')
            _prop = meta_map.get(prop)

            if prop in meta_map and _prop and not data.get(_prop):
                # this could be bad in cases where any values that the property
                # is mapped up to (i.e. "src", "type", etc) are found in ``data``
                # TODO: Figure out a smoother way to prevent conflicts ^^^^^^^^
                image_prop = meta['image_key']
                video_prop = meta['video_key']

                if prop.startswith((image_prop, video_prop)) and \
                prop.endswith(('width', 'height')):
                    if prop.endswith(('width', 'height')):
                        value = convert_to_int(value)

                if meta_map[prop] == 'locale':
                    locale = normalize_locale(value)
                    if locale:
                        data['locale'] = locale

                if prop == 'keywords':
                    if isinstance(value, str):
                        value = [v.strip() for v in value.split(',')]
                    else:
                        value = []

                if image_prop and prop.startswith(image_prop) and value:
                    # og:image URLs can be relative
                    if prop == 'og:image' and url:
                        value = urljoin(url, value)
                    image[meta_map[prop]] = value
                elif video_prop and prop.startswith(video_prop) and value:
                    video[meta_map[prop]] = value
                else:
                    data[meta_map[prop]] = value

        if image:
            image['type'] = image_prop
            data['images'].append(image)
        if video:
            data['videos'].append(video)

    def _filter_link_tag_data(self, source, soup, data, url):
        """This method filters the web page content for link tags that match patterns given in the ``FILTER_MAPS``

        :param source: The key of the meta dictionary in ``FILTER_MAPS['link']``
        :type source: string
        :param soup: BeautifulSoup instance to find meta tags
        :type soup: instance
        :param data: The response dictionary to manipulate
        :type data: (dict)
        :param url: URL used for making an absolute url
        :type url: string

        """
        link = FILTER_MAPS['link'][source]

        html = soup.find_all('link', {link['key']: link['pattern']})

        if link['type'] == 'url':
            for line in html:
                data['url'] = line.get('href')
        else:
            for line in html:
                data['images'].append({
                    'src': urljoin(url, line.get('href')),
                    'type': link['type'],
                })

    def _filter_amp_data(self, soup, data, url, all_images):
        amp_scripts = soup.find_all('script', {'type': 'application/ld+json'})
        for script in amp_scripts:
            content = script.contents
            _json = None
            try:
                _json = json.loads(content[0])
            except (IndexError, ValueError):
                continue

            if _json:
                image = _json.get('image')
                if image:
                    if isinstance(image, str):
                        data['images'].append({
                            'src': urljoin(url, image),
                        })
                    elif isinstance(image, object):
                        data['images'].append({
                            'src': urljoin(url, image.get('url')),
                            'width': convert_to_int(image.get('width')),
                            'height': convert_to_int(image.get('height')),
                        })

                data['title'] = _json.get('headline', '')
                data['url'] = _json.get('url', '')
                data['description'] = _json.get('description', '')

        if all_images:
            amp_imgs = soup.find_all('amp-img')
            for image in amp_imgs:
                item = normalize_image_data(image, url)

                data['images'].append(item)

    def _find_all_images(self, soup, data, url):
        """This method finds all images in the web page content

        :param soup: BeautifulSoup instance to find meta tags
        :type soup: instance
        :param data: The response dictionary to manipulate
        :type data: (dict)

        """
        all_images = soup.find_all('img')
        for image in all_images:
            item = normalize_image_data(image, url)

            data['images'].append(item)
