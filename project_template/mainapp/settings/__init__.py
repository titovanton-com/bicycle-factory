# -*- coding: utf-8 -*-

import os
import sys

from django.conf.globalpath import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.conf.globalpath import MIDDLEWARE_CLASSES as MC

from path import *
from assets import *
from constance import *
from djpath import *
from grappelli import *
from mainapp import *
from secret import *
from sorl import *


INSTALLED_APPS = (
    # 'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mainapp',

    'django_extensions',
    'sorl.thumbnail',
    'south',
    'django_assets',
    'constance',

    'bicycle.futuremessage',
    'bicycle.core',
    'bicycle.feedback',
    'bicycle.news',
    'bicycle.carousel',
)

MIDDLEWARE_CLASSES = MC + (
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bicycle.futuremessage.middleware.FutureMessageMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'mainapp.context_processors.meta_tags',
)

TEMPLATE_DIRS = (
    rel_mainapp('templates'),
    rel_project('bicycle', 'core', 'templates'),
)

STATICFILES_DIRS = (
    ('bootstrap', rel_project('libs', 'bootstrap', 'dist')),
    ('fancybox', rel_project('libs', 'fancyapps-fancyBox', 'source')),
    ('print', rel_project('libs', 'jQuery-printPage-plugin')),
    ('rc-carousel', rel_project('libs', 'jquery-ui-carousel', 'dist')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# should we link StaticSrcStorageFinder:
sss_finder = ASSETS_AUTO_BUILD
try:
    # when user runs ./manage.py assets build
    if sys.argv[1] == 'assets' and sys.argv[2] == 'build':
        sss_finder = True
except IndexError:
    pass
try:
    # when user runs ./manage.py collectstatic
    if sys.argv[1] == 'collectstatic':
        sss_finder = False
except IndexError:
    pass
if sss_finder:
    STATICFILES_FINDERS += ('bicycle.core.finders.StaticSrcStorageFinder',)

ROOT_URLCONF = 'mainapp.urls'

WSGI_APPLICATION = 'mainapp.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True
