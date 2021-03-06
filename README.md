# FrickFeed

Presentation: https://docs.google.com/presentation/d/1J7i5hto65hBXedNJehDo9axlp2BxMuU2CFaOpW1bFJE

## Dependencies
* postgresql 
* python2.7.*

## Setup Python and Django
`git clone git@github.com:HackTheDinos/frickfeed.git`

`mkvirtualenv frickfeed`

`workon frickfeed`

`pip install -r requirements/base.txt`

`export DJANGO_SETTINGS_MODULE=frickfeed.settings.base`

## Setup Postgres DB

```
createuser -s postgres
psql -U postgres
CREATE DATABASE frickdb;
CREATE USER frick WITH PASSWORD 'frickpass';
GRANT ALL PRIVILEGES ON DATABASE  frickdb TO frick;
\q
```

## Create a Django Admin
`./manage.py createsuperuser`

Follow the prompts:

> Username (leave blank to use 'gregthompson'): frick

> Email address: 

> Password: frickpassword

> Password (again): frickpassword

> Superuser created successfully.

## Run the frick out of our scripts
`python manage.py migrate`

`python manage.py loaddata dummy_data.json`

`python manage.py loaddata auth_sites.json`

`python manage.py loaddata auth_social_accounts.json`

`./manage.py runserver`
