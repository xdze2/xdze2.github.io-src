#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'xdze'
SITENAME = 'xdze2'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

DEFAULT_DATE = 'fs' # from the filesystem

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


PLUGIN_PATHS = ('./plugins/', )
PLUGINS = ['liquid_tags.notebook']
NOTEBOOK_DIR = './'


THEME = 'themes/bluerobot'

EXTRA_HEADER = open('my_nb_header.html').read()#.decode('utf-8')

SUMMARY_MAX_LENGTH = 4
