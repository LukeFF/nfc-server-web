#!/bin/bash

sudo apt-get install -y python-pip bzr
sudo pip install django
bzr branch lp:nfcpy
python manage.py migrate
python manage.py loaddata tagtypes
