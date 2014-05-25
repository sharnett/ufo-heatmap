# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sean Harnett'
SITENAME = 'ufo-heatmap'
SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DEFAULT_PAGINATION = False

THEME = 'fresh'
PLUGIN_PATH = '/Users/srharnett/Dropbox/hacking/pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.include_code', 'liquid_tags.notebook']
EXTRA_HEADER = open('_nb_header.html').read()

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
