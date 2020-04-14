#!/bin/bash
PROJECT_DIR=/home/hnmn3/workspace/license_key_mgmt/license_key_mgmt
PROJECT_NAME=license_key_mgmt
cd $PROJECT_DIR || exit
gunicorn $PROJECT_NAME.wsgi
