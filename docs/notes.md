# Django

## Install

```bash

poerty init

poetry add Django

poetry update

poetry run django-admin startproject project-name

```

## Docker

```bash

# Сборка контейнеров
docker-compose build --no-cache

# 
docker-compose up

```

## Celery

```bash


# Run Celery Worker
celery -A app worker -l DEBUG -c 1 -Q celery -n main

# Run Celery Beat
celery -A app beat -l DEBUG
 
```

## Data

```bash

python manage.py loaddata category.json
python manage.py loaddata page.json
python manage.py loaddata post.json

python manage.py dumpdata

```

