#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'xdze2'
SITENAME = u'xdze2'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['physique/images', 'pdfs']

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

DEFAULT_DATE = 'fs' # filesystem

THEME = 'themes/bluerobot'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

MENUITEMS = (
    # ('all', '/'),
    # ('projets', '/pages/projets.html'),
    # ('blog', '/pages/publications.html'),
    # ('about', '/pages/about.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb', 'rst')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup' ] #, "representative_image"]


# Config de Ipynb plugin - https://github.com/danielfrg/pelican-ipynb
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True
