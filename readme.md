# Dino Project

Este é um projeto em django para introdução do Django Rest Framework durante o Meetup de Python realizado pela comunidade Urapython no dia 24/11/2020.

## Requisitos
- python 3.8
- Windows 10

## Setup inicial
- Os comandos a seguir devem ser digitados no terminal:
```bash
mkdir django-project
cd django-project
python3 -m venv myvenv
. myvenv/Scripts/activate
pip install django
pip install djangorestframework
pip install pillow
django-admin startproject dinoProject
cd dinoProject
python manage.py startapp dinosaurs
```
- Incluir `'rest_framework'` e `'dinosaurs'` em `INSTALLED_APPS`, no arquivo *settings.py*

## Passo a passo
- Crie seus models
- Crie seus serializers
- Crie suas views
- Registre seus apps no admin
- Crie suas urls

## Migrações e superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Teste sua aplicação
```bash
python manage.py runserver
```
- No seu navegador de internet digite *http://localhost:8000/admin*

## Referências

- Building APIs with Django and Django Rest Framework (https://books.agiliq.com/)

