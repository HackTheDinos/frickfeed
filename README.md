# FrickFeed

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
    Username (leave blank to use 'gregthompson'): frick
    Email address: 
    Password: frickpassword
    Password (again): frickpassword
    Superuser created successfully.

## Run the frick out of our scripts
`python manage.py migrate`

`./manage.py runserver`
