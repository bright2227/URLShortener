#!/bin/sh
python3 -m pip install -r requirements.txt
python3 manage.py wait_for_database
python3 manage.py migrate
python3 manage.py runscript init


uwsgi -d uwsgi.log uwsgi.ini
python3 manage.py qcluster
