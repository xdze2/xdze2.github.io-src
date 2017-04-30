#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'xdze2'
SITENAME = u'xdze2'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['physique/images', 'statistiques/images', 'static', 'images',
                'about/images']

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False

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

MENUTAGS = (
    'physique', 'statistiques', 'visualisation', 'algorithme'
)
MENUITEMS = (
    # ('all', '/'),
    # ('projets', '/pages/projets.html'),
    # ('blog', '/pages/publications.html'),
     ('[plus]', '/tags.html'),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md',) #, 'ipynb', 'rst')
#PLUGIN_PATHS = ['./plugins']
#PLUGINS = [ 'liquid_tags.notebook'] #, "representative_image"] 'ipynb.markup',

MARKUP = ('md','rst',)

PLUGIN_PATHS = ('./plugins', )
PLUGINS = ['liquid_tags.notebook', 'representative_image' ]

NOTEBOOK_DIR = ''
EXTRA_HEADER = open('my_nb_header.html').read()#.decode('utf-8')

# Config de Ipynb plugin - https://github.com/danielfrg/pelican-ipynb
#IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
#IPYNB_IGNORE_CSS = True
