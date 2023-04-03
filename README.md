# goojango

*I think this repo is gonna hold the Turlock Rock and Gem Show source?*

## Instructions to port to Django:

*if your files are in php, port them to HTML*

1. at the start of the file, put ```{% load static %}``` *this makes it so you can load media and style*
2. put this boilerplate: 
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width" initial="1">
<title>pogger</title>
<link href="{% static 'style.css' %}" rel="stylesheet" type="text/css" />
<link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
```
3. for any other media you want to load, use:
    - < filename > is the name of the file you want to load, place it in the static folder
```html
{% static '< filename >' %}
```

4. example tag using ```{% static %}```:

```html
<img src="{% static 'epicphoto.png' %}">
```

## That was the easy stuff, time for complicated python things!

1. All HTML files belong in the templates folder, in the main folder. Don't ask questions.
2. To add an HTML file you coded, first figure out what you want the url to it to be, something like map.html would be ```https://<url>/map```
    - Remember what you figured out, **but only the part after** ```https://<url>/```
3. Go into the views.py file, ***in the main folder, not the goojango folder***
4. Put a new line at the end, following this format:
```python
def <viewname>(request):
    return render(request, '<filename>')
```
4. Remember the ```<viewname>``` that you set

### You now have a view that you can use to load files!
#### Time to setup a url map!
1. Go into the main/urls.py file, ***not the goojango/urls.py file***
2. Add this to the top of the file:
```python
from .views import <viewname>
```
2. Find the ```urlpatterns = []``` part of the code
3. Add a line to the end of it, *make sure it's indented,* following this format:
```python
path('<urlname-from-earlier>', <viewname>, name='<viewname>'),
```
4. Now test it by asking me to run the server, then come cry to me if it doesn't work! Good job!

## Hopefully you understood all that!

If you have questions, comments, or concerns, contact me.