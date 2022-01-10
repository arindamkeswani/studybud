### Codebase and personal notes for Dennis Ivy's 7-hour Django course

## Commands used (Powershell)

- python --version
- pip install virtualenv
- Set-ExecutionPolicy Unrestricted -Force
- virtualenv env
- env\scripts\activate
- pip install django
- django-admin
- django-admin startproject studybud
- cd studybud
- python manage.py runserver
- python manage.py startapp base

## Notes

> (In studybud/settings.py) adding 'base.apps.BaseConfig' will connect the project folder to the new app that we just added (inside base folder)

>  Two URLs have been used in this project (route URLs file, and one for our specific app)

> `path('', home)` has the specfied path as the first parameter, and the associated logic in the form of a function as the second parameter

> The views (which represent the business logic in Django) should preferably not be defined in urls.py of the main project. Instead, write the views in the base app by creating a urls.py in the base folder

> The `urls.py` file inside `studybud` folder is used for the entire project, but other files, such as the one in `base` folder is for a specific app

> Paths are stored in a list, which has been done in `urlpatterns=[]`

> URLs can be accessed by their name, which can be defined in the path itself

> URLs from other apps can be used with the help of `include`, e.g. `path('', include('base.urls'))`