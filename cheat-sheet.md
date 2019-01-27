# Django Cheat Sheet
I'm going to learn the **Django Framework** 
with **Pucky** on his Youtube channel 
**The New Boston** and I've decided to save every single command here to remember.


### Basic Commands to Start
|       Command     |       Description       |
|---|---|
|`django-admin startproject PROJECTNAME`|Start a new Project with name _PROJECTNAME_|
| `python mange.py runserver`| Start your localhost server|
|`python manage.py startapp APPNAME`|Create a new app in your website with name _APPNAME_|

### Parent Directory
After creating a new project make sure to `cd` into the parent directory
which is `./PROJECTNAME/` using the command
```bash
cd ./PROJECTNAME/
```

### Create The Music App
To create the first **application** in my website which is **The Music App**
```bash
python manage.py startapp music
```

### URL Mapping
The file `PROJECTNAME/urls.py` is the file we do the URL Mapping
but it would become very messy if we stored all the URLs in here.
The solution is to create a new file to map URLs in every single **app** in my website.
For Instance in the **Music** app in my Website I'll create 
a new file `music/urls.py`
using the command 
```bash
touch music/urls.py
```

Basically this will be the URL Mapping file for this part of my website 
```python
# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]
```
and then I have to mach this hook up this file 
with the parent mapping file which is `PROJECTNAME/PROJECTNAME/urls.py` after modifying it should looks
like that
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls'))
]
```

and after that, one last step remains.. 
which is adding the functions that will **Response** after **Request** these URLs
go to the `music/views.py` file and insert the functions you will request.
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")
``` 

### Database Configurations
- `music/models.py` file is the file where I can put my app's blueprint.
- `PROJECTNAME/settings.py` is the file where i match my models with the website
and it should contain this part 
    ```python
        INSTALLED_APPS = [
        'music.apps.MusicConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles'
      ]
    ```
### Database API
Django has a built-in Database API which makes database connections are easy.

| Code | Description |
|---|---|
| `from music.models import Album` | Importing the classes to operate on it |
| `var = Album(artist='Taylor', title='Red', genre='Country', logo='logo url')` | Creates a new object of `Album` class with initial data |
| `obj.save()` | Saves the object we've just created into the database. |
| `obj.delete()` | Deletes the object we've just created from database |
| `Album.objects.all()` | Returns a list of all saved objects in database of class `Album`. |
| `Album.objects.filter(id=1)` | Returns a list of all objects with `id = 1` |
| `Albums.objects.filter(artist__startswith='Mostafa')` | Returns a list of all Albums with artist that starts with `'Mostafa'`. |


### Admin
Django already have an admin application that can manage the CRUD operations.

| Command | Description |
|---|---|
| `python manage.py createsuperuser` | To Create a new Admin for your project |

To make an **Admin Interface** For a Specific class _(Album For Instance)_
go to `music/admin.py` and Import that class, then connect the class 
with the admin interface by typing 
```python
from .music import Album

admin.site.register(Album)
```
You must create a superuser at first.

