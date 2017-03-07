#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'xdze2'
SITENAME = u'xdze2'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['physique/images', 'pdfs']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = 'themes/bluerobot'

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
    ('projets', '/pages/projets.html'),
    ('blog', '/pages/publications.html'),
    ('about', '/pages/about.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True
