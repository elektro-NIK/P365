# P365 #
P365 is the web site where you can share your travel experiences.

1. Clone project
2. Create virtualenv
3. Install Django, GeoDjango
4. Install python packages
5. Setting up GoogleAPI key
6. Create DB
7. Create superuser
8. Run server

## Clone project ##

`git clone git@gitlab.com:elektro.NIK/P365.git`\
or\
`git clone https://gitlab.com/elektro.NIK/P365.git`

## Create virtualenv ##

`cd ./P365`\
`virtualenv --python=python3 .venv`\
`source .venv/bin/activate`

## Install Django, GeoDjango ##
Follow official instructions:
https://docs.djangoproject.com/en/2.1/intro/install/
https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/

For Ubuntu 18.04 and Django 2.1 you need install these packages:\
`sudo apt install binutils libproj-dev gdal-bin libsqlite3-mod-spatialite`

## Install python packages ##
`pip install -r requirements.txt`

## Setting up GoogleAPI key ##
You must get a Google API key to determine the altitudes: https://console.developers.google.com/\
`echo "ELEVATION_KEY = 'your_elevation_api_key'" > google_api/api_keys.py`

## Create DB ##
`./manage.py makemigrations`\
`./manage.py migrate`

## Create superuser ##
`./manage.py createsuperuser`

## Run dev server ##
To access the server from the same computer on which it is running, use `localhost` or `127.0.0.1`\
`./manage.py runserver <IP_address>:<port>`
