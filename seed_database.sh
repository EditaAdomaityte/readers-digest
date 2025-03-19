#!/bin/bash

rm db.sqlite3
rm -rf ./clientapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations clientapi
python3 manage.py migrate clientapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

