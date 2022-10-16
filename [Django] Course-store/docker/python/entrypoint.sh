#!/bin/bash

/django_project/docker/python/wait-for-it.sh db:3306 -- python /django_project/manage.py migrate
/django_project/docker/python/wait-for-it.sh db:3306 -- python /django_project/manage.py loaddata seed/*

gunicorn django_project.wsgi:application --bind 0.0.0.0:8000
