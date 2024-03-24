# TMS Project

Площадка для организации тестирования и опросов

## Описание

[Полное описание проекта](docs/index.md)

## Структура проекта

- configs - Настройки сервисов
- docs - Документация по проекту
- public - Рабочая директория проекта
- sysdumps - Хранения файлов базы данных и других сервисов

# Требования

Для корректной работы необходимо установить Docker.

https://docs.docker.com/engine/install/

# Установка

- Склонируйте себе репозитоий
```bash
git clone git@github.com:gbukhtatyi/tms-project.git .
``` 
- Для старта проекта выполните в рабочей директории:
```bash
docker-compose build
docker-compose up
``` 
- Для остановки проекта выполните в рабочей директории:
```bash
docker-compose down
``` 
