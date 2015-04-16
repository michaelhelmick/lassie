.. :changelog:

History
-------

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
