# -*- coding: utf-8 -*-
#

import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


AUTHOR = 'Smarter Travel'
VERSION = '0.1.0'
EMAIL = ''
DESCRIPTION = ''
URL = ''
LICENSE = 'MIT'
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: System :: Installation/Setup",
    "Topic :: System :: Software Distribution"
]

REQUIREMENTS = [
    'requests',
    'artifactory'
]

with codecs.open('README.rst', 'r', 'utf-8') as handle:
    LONG_DESCRIPTION = handle.read()

setup(
    name='apy',
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author_email=EMAIL,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    url=URL,
    install_requires=REQUIREMENTS,
    zip_safe=True,
    packages=['apy'])