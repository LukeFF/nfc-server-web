#!/bin/bash

sudo apt-get install -y python-pip
sudo pip install django
python manage.py migrate
python manage.py loaddata tagtypes
