# -*- coding: utf-8 -*-

import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG           = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    SECRET_KEY      ="stuff"
    STATIC_DIR      = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR      = os.path.join(STATIC_DIR, 'images')


