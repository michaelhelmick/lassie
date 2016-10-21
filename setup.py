#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.8.3'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'lassie',
    'lassie.filters'
]

setup(
    name='lassie',
    version=__version__,
    install_requires=open("requirements.txt").read().split("\n"),
    author='Mike Helmick',
    author_email='me@michaelhelmick.com',
    license=open('LICENSE').read(),
    url='https://github.com/michaelhelmick/lassie/tree/master',
    keywords='lassie open graph web content scrape scraper',
    description='Lassie is a Python library for retrieving basic content from websites',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    include_package_data=True,
    packages=packages,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
