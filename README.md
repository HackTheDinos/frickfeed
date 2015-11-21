# FrickFeed

## Setup Python and Django
`git clone git@github.com:HackTheDinos/frickfeed.git`

`mkvirtualenv frickfeed`

`workon frickfeed`

`pip install -r requirements/base.txt`

`export DJANGO_SETTINGS_MODULE=frickfeed.settings.base`


## Setup Postgres DB

```
sudo su - postgres
psql
CREATE DATABSE frickdb;
CREATE USER frick WITH PASSWORD 'frickpass';
GRANT ALL PRIVILEGES ON DATABASE  frickdb TO frick;
\q
```

## Run the frick out of our scripts

`./manage.py runserver`
