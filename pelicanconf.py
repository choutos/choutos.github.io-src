#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'choutos'
SITENAME = 'choutos'
THEME = 'Flex'
SITEURL = 'https://choutos.github.io'
SITESUBTITLE='STEAM: Science, Technology, Engineering, ADVENTURE and MOTORCYCLES'

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Wanderclan', 'http://wanderclan.com/'),
         ('Rally Albania', 'http://www.rallyalbania.com'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/choutos'),
          ('facebook', 'https://www.facebook.com/Choutos-174167099957564/'),
          ('instagram', 'https://www.instagram.com/choutos/'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
