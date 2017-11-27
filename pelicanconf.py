#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'HP Chang'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'HPC@TechBar'
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
          ('twitter', 'https://twitter.com/hpc_techbar'),
          ('envelope-o', 'mailto:hpchang.tw@gmail.com'))
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
#             ('Blog', '/blogging-with-jupyter-and-pelican.html')
)
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}


PYGMENTS_STYLE = 'default'
DEFAULT_PAGINATION = 10

THEME = './pelican-themes/Flex'

STATIC_PATHS = ['res']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins']
IGNORE_FILES = ['.ipynb_checkpoints']
PLUGINS = ['ipynb.markup']
JINJA_ENVIRONMENT = {
    'extensions': ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_'],
}

#STATIC_PATHS = ['res', 'code', 'extra/CNAME']
#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}