.. :changelog:

History
-------

0.10.0 (2017-02-03)
++++++++++++++++++
- Fix issue where a website may have malformed HTML and no <html> tag causing soup.html to be None (#60)
- Updated beautifulsoup4 to 4.5.3
- Update html5lib to 1.0b10

0.9.0 (2017-01-29)
++++++++++++++++++
- Added a default fake user agent to use instead of using python-requests/version (some websites will mark certain user agents as bot attempts)
- Updated requests to 2.13.0

0.8.7 (2016-12-21)
++++++++++++++++++
- Fix Python 3 support
- Handle empty AMP image lists

0.8.6 (2016-11-17)
++++++++++++++++++
- Handle AMP image list of strings vs list of objects

0.8.5 (2016-11-03)
++++++++++++++++++
- Handle AMP data that is contained in a list
- Retrieve videos and thumbnails (as images) from AMP VideoObjects

0.8.4 (2016-11-01)
++++++++++++++++++
- Fix issue where AMP images could be lists inside an object

0.8.3 (2016-10-21)
++++++++++++++++++
- Fix issue where some keys returned (i.e. description) would not be retrieved if the key existed with an empty value already

0.8.2 (2016-09-26)
++++++++++++++++++
- Fix issue where AMP images could be images and not objects

0.8.1 (2016-09-26)
++++++++++++++++++
- Add support for AMP "description" attribute
- Fix issue where an error would be thrown if width/height of an image weren't strings
- Fix duplicate AMP title request, should have been url

0.8.0 (2016-09-26)
++++++++++++++++++
- Add support for links that use AMP

0.7.2 (2016-08-01)
++++++++++++++++++
- Add `status_code` to response dictionary (for "file-like" responses, as well)

0.7.1 (2016-07-27)
++++++++++++++++++
- Add support for open graph `site_name`


0.7.0 (2016-07-01)
++++++++++++++++++
- Add `status_code` to response dictionary


0.6.2 (2015-11-11)
++++++++++++++++++
- Pinned `requests` library to version 2.8.1
- Pinned `beautifulsoup4` library to version 4.4.1
- Add Python 3.5 to Travis CI build matrix (officially support 3.5)


0.6.1 (2015-10-30)
++++++++++++++++++
- Catch and raise `LassieError` on HEAD requests when `handle_file_content` is passed to the Lassie API
- Pinned `requests` library to version 2.8.0


0.6.0 (2015-08-19)
++++++++++++++++++
- Support for secure url image and videos from Open Graph
- Simplified `merge_settings` and data updating internally


0.5.3 (2015-07-02)
++++++++++++++++++
- Handle when a website doesn't set a value on the "keywords" meta tag


0.5.2 (2015-04-16)
++++++++++++++++++
- Updated `requests` and `beautifulsoup4` library versions


0.5.1 (2014-08-05)
++++++++++++++++++
- Fix issue where headers didn't always have 'Content-Type' key


0.5.0 (2014-06-23)
++++++++++++++++++
- Added ability to `fetch` links that are image files (jpg, gif, png, bmp)
- Renamed `_retreive_content` to `_retrieve_content` because I evidently don't know how to spell correctly


0.4.0 (2013-09-30)
++++++++++++++++++
- Updated `requests` and `beautifulsoup4` library versions
- Added support for manipulating the request, see Advanced Usage docs
- Fixed issue where `lassie.fetch` would break if the page had no title
- Lassie is now more lenient when it comes to width and height values of images (now accepts integers (100) or integer with px (100px)
- Image URLs for all images are now absolute

0.3.0 (2013-08-15)
++++++++++++++++++

- Added support for `locale` to be returned. If `lang` is specified in the `html` tag and it normalizes to an actual locale, it will be added to the returned data.
- Fixed bug where height was not being returned for body images
- Added test coverage, we're 100% covered! :D


0.2.1 (2013-08-13)
++++++++++++++++++

- Remove spaces from the returned keywords list
- Fixed issue where favicon was not being retrieved
- Fixed priority for class level vs method level params


0.2.0 (2013-08-06)
++++++++++++++++++

- Fix package error when importing


0.1.0 (2013-08-05)
++++++++++++++++++

- Initial Release
