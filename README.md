# SKHUFEEDS

KakaoTalk Auto Reply API based Chat bot for subscribing school news

## Dependencies

- Python 3.*
 - Django
 - mysqlclient
 - Celery
 - python-jose
 - bs4
- MySQL

## Setup

- At your KakaoTalk Plus Friend account settings, turn auto reply API on.
- set url to the address of the server that will run this django app
- create database on mysql shell

```
 CREATE USER username@localhost IDENTIFIED BY 'password';
 CREATE DATABASE skhufeedsdb CHARACTER SET UTF8;
 GRANT ALL PRIVILEGES ON skhufeeds.* TO username@localhost;
 FLUSH PRIVILEGES;
 exit
```

- setup database connection settings on `skhufeeds/skhufeeds/skhufeeds/settings.py`
- run database table operation

```
  python manage.py makemigrations settings
  python manage.py makemigrations crawlers
  python manage.py migrate
```

## Running

 - Run Celery worker process first.

```
 celery -A skhufeeds worker -l debug
```

- now, run the app

```
python manage.py runserver
```

- to bind to port 80, run this instead

```
python manage.py runserver 0.0.0.0:80
```

- you might need `sudo` on Unix or Linux based OS

```
sudo python manage.py runserver 0.0.0.0:80
```
