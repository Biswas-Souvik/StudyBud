#!/bin/bash

echo "BUILD STARTED."
echo "Installing Dependencies..."
python3.12 -m pip install -r requirements.txt

echo "Make and Apply Migrations..."
python3.12 manage.py makemigrations
python3.12 manage.py migrate

echo "Collect Static..."
python3.12 manage.py collectstatic --noinput --clear
echo " BUILD END"