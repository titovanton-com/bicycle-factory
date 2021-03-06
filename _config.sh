#!/bin/bash

# Catalogs tree
WEBAPPS=/webapps
TEMPLATES=$WORKON_HOME/templates
PROJECT_TEMPLATE=$WORKON_HOME/project_template
MAINAPP=mainapp
PROJECT_NAME=$(cat $WORKON_HOME/name)
PROJECT_DIR=$WEBAPPS/django/$PROJECT_NAME
SERVER=$WEBAPPS/server/$PROJECT_NAME
LOG=$WEBAPPS/log/$PROJECT_NAME
STATIC=$WEBAPPS/django/static/$PROJECT_NAME
STATIC_SRC=$PROJECT_DIR/$MAINAPP/static_src
MEDIA=$WEBAPPS/django/media/$PROJECT_NAME
INTERNAL=$WEBAPPS/django/internal/$PROJECT_NAME
SETTINGS=$PROJECT_DIR/settings
BOOTSTRAP_SED=$PROJECT_DIR/libs/bootstrap/less/
UWSGI_PARAMS=$WEBAPPS/server/uwsgi_params
DUMMY_ROOT=$WEBAPPS/dummy/$PROJECT_NAME
LIBS=libs

PIP_PACKAGES=$PROJECT_DIR/requirements.pip
