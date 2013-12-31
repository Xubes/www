#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# LOCAL
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# SITE
AUTHOR = 'The Databrary Team'

# CONTENT
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'news'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SUMMARY_MAX_LENGTH = 50
DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 3

PLUGIN_PATH = '../common/plugins'
PLUGINS = ['sitemap']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'admonition', 'headerid(level=1)', 'nl2br', 'sane_lists']

SITEMAP = {
	'format': 'xml',
	'priorities': {'articles': 0.75, 'indexes': 0.5, 'pages': 1},
	'changefreqs': {'articles': 'monthly', 'indexes': 'daily', 'pages': 'monthly'}
}

# COMPILE
THEME = '../common/theme'

PATH = 'input/'
OUTPUT_PATH = 'output/'
DIRECT_TEMPLATES = ('index', 'archives')
PAGINATED_DIRECT_TEMPLATES = ('index', )

PAGE_DIR = 'pages'
PAGE_EXCLUDES = ()
ARTICLE_DIR = 'posts'
ARTICLE_EXCLUDES = ()
STATIC_PATHS = ['files', 'img', 'ico', 'js', 'css']

TYPOGRIFY = True

# URLS
ARTICLE_URL = 'post/{slug}.html'
ARTICLE_SAVE_AS = 'post/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
ARCHIVES_SAVE_AS = 'archives.html'

TAG_SAVE_AS = False
TAGS_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# FEEDS
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 25

# CUSTOM
# HEADER_PROJECTS =
