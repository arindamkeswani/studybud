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
- python manage.py migrate (running server would not give unapplied migrations error anymore)
- python manage.py makemigrations (followed by python manage.py migrate)
- python manage.py createsuperuser

## Notes

> (In studybud/settings.py) adding 'base.apps.BaseConfig' will connect the project folder to the new app that we just added (inside base folder)

>  Two URLs have been used in this project (route URLs file, and one for our specific app)

> `path('', home)` has the specfied path as the first parameter, and the associated logic in the form of a function as the second parameter

> The views (which represent the business logic in Django) should preferably not be defined in urls.py of the main project. Instead, write the views in the base app by creating a urls.py in the base folder

> The `urls.py` file inside `studybud` folder is used for the entire project, but other files, such as the one in `base` folder is for a specific app

> Paths are stored in a list, which has been done in `urlpatterns=[]`

> URLs can be accessed by their name, which can be defined in the path itself

> URLs from other apps can be used with the help of `include`, e.g. `path('', include('base.urls'))`

> Use template inheritance to include pieces of code in other pages, e.g. a Navbar is typically rendered as a part  of all pages, so instead of re-writing the code for it, we can simply inherit it

> Django templating is similar to Jinja2, which is used for templating in Flask

> One can create app-specific templates (i.e. templates that are not needed throughout the project) by creating a templates folder inside the app, followed by another folder inside this templates folder, which has the same name as the app name

> Instead of specifying a path inside `href`, we can use names (that have been specified in urls) for links using url tag. 
Sample syntax: `<a href="{% url 'room' room.id %}">{{room.name}}</a>`

### Database & Admin Panel

> We have some apps made by Django by default, which have databases of their own. They can be viewed in `settings.py` (INSTALLED_APPS list). So we have some tables prepared by Django that are ready to be migrated

> Django Admin Panel lets us view our database, as well as perform CRUD operations on the tables

> In the python class used for creating DB, the `null` parameter is `False` by default. Setting it to `True` would mean that that particular instance of the model can have the target field as blank. `blank` parameter is used for forms, for options similar to required fields

> `auto_now=True` means that we want to note down the time at an instance of a model of the database was last updated. This is built-in in Django

> `auto_now_add=True` notes down the timestamp of data creation

> `on_delete=models.CASCADE` on a foreign key will delete the element if its parent is deleted. If a room is deleted, the messages of that room will also be deleted

> `admin.site.register(ModelName)` will register the model so that it can be viewed in the admin panel

### CRUD

> If we do not specify action inside a form, it will send the data to the current URL 

> `{{form.as_p}}` wraps the form data in the paragraph tag

> To pre-fill a form, you may follow this syntax: `form = SomeForm(instance=some_data)` 

> Setting `href="{{request.META.HTTP_REFERER}}"` inside a link in your template will send the user back to where they came from

### Search

> To pass query parameters inside the anchor tag, you may use the following syntax: `<a href="{% url 'some_page' %}?q={{parameter_to_be_passed}}">{{display_text}}</a>`

> `filter()` method returns all the results if no parameter is passed to it

>  To refer to a schema using a foreign key (i.e. a parent schema), use double-underscore, e.g. `rooms = Room.objects.filter(topic__name=q)`

### Restricted Pages

> The `login_required` decorator acts like a middleware function that prevents a user from visiting certain pages without logging in. Syntax: `@login_required(login_required='/login')`

> `request.user.is_authenticated` checks whether a user is logged in or not

### User registration

> `commit=False` enables us to acces the form data without saving it into the database
