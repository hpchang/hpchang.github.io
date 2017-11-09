#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'HP Chang'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Solution-Maker'
SITENAME = u'HPC@TechBar'
SITEDESCRIPTION = '%s\'s TechBar' % AUTHOR

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FAVICON = '/res/Penguin.ico'
SITELOGO = '/res/hp_profile.png'
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/hpchang'),
          ('github', 'https://github.com/hpchang'),
          ('envelope-o', 'mailto:hpchang.tw@gmail.com'))
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}


DEFAULT_PAGINATION = 10

THEME = './pelican-themes/Flex'

STATIC_PATHS = ['res']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
