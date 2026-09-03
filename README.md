###Learn Django 
***********************************************************************************
Steps :
Create Django Project Folder & Go inside that Django Project 
==>cd Django Project Folder Name

Create one Virtual Envornment in it & Activate it 
==>python -m venv Envornment Name ---Create virtual envornment
==>EnvornmentName\Scripts\activate ---Activate Virtual Envornment

Install Django inside project & create django project using django admin & Go inside that project  
==>pip install django ---Install django 
==>django-admin startproject Project Name ---Create Django Project 
==>cd Project Name

Create app in it & open it in vs code editor 
==>python manage.py startapp App Name
==>code .

In This we create project in using Django Python Framework
Eg.
cd "Django Project Folder"

python -m venv env

env\Scripts\activate

pip install django

django-admin startproject MyProject

cd MyProject

python manage.py startapp home

code .

#For Run the Django Project 
python manage.py runserver

***********************************************************************************
After Create Project We have create project Like this 

Add App Name inside setting.py file of django project in installed app list section
==>like 'AppName1','AppName2','AppNamen' in installed app list
Eg.
inside setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'AppName1',
    'AppName2',
    'AppName3',
]

***********************************************************************************

Create Template Folder inside project ( Not inside Django project & App Folder) & Create seperate folders of each app inside Template
Eg.
Project Look this Create Template Folder
MyProject/
│
├── manage.py
│
├── MyProject/              ← Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── home/                   ← App 1
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── accounts/               ← App 2
│   ├── views.py
│   ├── models.py
│   └── ...
│
└── templates/              ← Create this yourself
    ├── home/               ← Templates for home app
    │   ├── index.html
    │   └── about.html
    │
    └── accounts/           ← Templates for accounts app
        ├── login.html
        └── register.html
        
  After Create Template Folder add that Folder path inside setting.py file of Django Project inside Template list 
    ==> Like ['Templates'] inside setting.py
    Eg.
    Inside Setting.py of Django Project
    
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
        'APP_DIRS': True,
        ...
    },
]

 *** In case we directly create HTML webpages inside Template then we have use in setting.py of Django Project

    Eg.
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Template'],
        'APP_DIRS': True,
        ...
    },
]

Flow of How Templates will render on request 
Browser Request
      ↓
Project urls.py
      ↓
home/urls.py
      ↓
views.py
      ↓
render()
      ↓
templates/home/index.html


***********************************************************************************

Create seperate path for each app inside the urls.py of django project using path & include 
==>path('AppName/',include('AppName.urls')
Eg.
inside urls.py of Django Project 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('AppPath/', include('AppName.urls')),
]

After that create urls.py in Django App & create path in it for render that pages on request 
==>App Structure Look like this After create it 
home/
├── migrations/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── urls.py        ← Create this

Eg.
from django.urls import path
from .views import ViewName #import ViewName from views.py File

urlpatterns = [
    path('Path/',ViewName),
]

Connection Flow 
urls.py 
   ↓
ViewName
   ↓
views.py
   ↓
render()
   ↓
Template Page


***********************************************************************************

Create ViewName inside views.py 
==>With same name inside urls.py path 
Eg.
Inside views.py look this
from django.shortcuts import render

def ViewName(request):
    return render(request, 'AppName/web.html') # AppName inside Templates Folder  

render() Function used for Render Html Webpages as responce on request where as HttpResponse() function render message as responce on request
Before use HttpResponse() we have write 
===>from django.http import HttpResponse
Flow of render HTML Templates
Request
   ↓
View
   ↓
render()
   ↓
HTML Template
   ↓
Response

Flow of Responce Message
Request
   ↓
View
   ↓
HttpResponse()
   ↓
"Welcome to Django"
   ↓
Response

***********************************************************************************

Create Database Model inside Django App inside models.py
==>class ModelName(models.Model):
      ColumnName=models.datatypeField(max_length=length in integer value)
  Eg.
  Inside models.py Look like after create Database Model
  
  from django.db import models

  class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField()
    def __str__(self):
      return self.Name #Here we have write String Value column name

  After Create makemigrations & migrate of database model
  ==>python manage.py makemigrations ---Make migrations (means create Database model)
  ==>python manage.py migrate ---Migrate Database Models(Load Created & Predefined Model) for use on admin panel
  We have to use both above command repited whenever after change in structure of Database model & Add new Columns in database models

  Then Create superuser & register your database models
  ==>python manage.py createsuperuser
  Enter username (by default admin when we skipped this)
  Enter Email 
  Enter Password
  Enter Password Again
  User created successfully 
  run the project 
  ==>python manage.py runserver
  
  Login on url using same credential you created before
  http://127.0.0.1:8000/admin/ 

  ==>admin.site.register(Database Model Name) ---register database model in admin.py of App
  
  Flow of Migration & Create user account
  Create Model in models.py
        ↓
  python manage.py makemigrations
        ↓
  python manage.py migrate
        ↓
  Register Model in admin.py
        ↓
  python manage.py createsuperuser
        ↓
  python manage.py runserver
        ↓
  /admin/
        ↓
  Login with Superuser
        ↓
  Manage Database Model

  Get data using Database model
  ==>Data=Database Model Name.objects.all() ----Get all data & store Data
  ==>Database Model Name.objects.create(Name of Database Model Column = Value or Data extract from request )  --- Add Data inside the Database Model

  Extract Data from request & send to database model
  Name=request.POST.get('Name of Input')  --- Here we have to use name of input in HTML form 

   *** we must have to add method in form like method="post" & Csrf token like this Form like {% csrf_token %}
   Eg.
   from django.shortcuts import render
from .models import Student
from django.shortcuts import render
from .models import Student

def StudentData(request):

    if request.method == 'POST':      #Check Request Method type
        Name = request.POST.get('Name')
        Age = request.POST.get('Age')   #Extract Data from request
        Email = request.POST.get('Email')

        Student.objects.create(
            Name=Name,
            Age=Age,
            Email=Email
        )   #Send Data in Database Model

    Data = Student.objects.all()   #Get & Store Data from Database Model

    return render(request, 'student/student.html', {'Data': Data}) #Send Data to HTML Page


  Send & Display Data on HTML webpage 
  {{Data}} ---Display Data in Query set Format

  {%for Key in Data%}  ---Display Data using For Loop
  #Lines of code
  {{Key.Name}}
  {%endfor%}

***********************************************************************************

Create Static Folder inside Project (Not in Django Project) & Create seperate Folder for Css , JS , Images 
MyProject/
│
├── manage.py
│
├── MyProject/              ← Django Project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── AppName1/
├── AppName2/
│
├── templates/              ← HTML Templates
│   ├── AppName1/
│   └── AppName2/
│
└── static/                 ← Static Files
    ├── css/                ← CSS Files
    ├── js/                 ← JavaScript Files
    └── images/             ← Images

Then Add Static Folder Path inside setting.py in static section
STATIC_URL = 'static/'
#Add Following in above section of setting.py
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

Use External Css in HTML Templates
{% load static %}   ---Write Outside or top of HTML file
use Static CSS File in HTML using in head section of HTML page 
<link rel="stylesheet" href="{% static ,'Css/File.css' %}

Similary Use  external Js in HTML Templates

{% load static %}    ---Write Outside or top of HTML file
In Body Section use JS File like given 
<script src="{% static , 'Js/File.js' %}></script>

***********************************************************************************

Create Common Code file inside the template folder & add Block for uncommon code in it
templates/
│
├── base.html
│
├── common/
│   ├── header.html
│   ├── navbar.html
│   └── footer.html
│
├── home/
│   └── index.html
│
└── accounts/
    └── login.html

Here we can add un common code like Title & main section of web pages
  {%block Blockname%}
  Lines of code
  {%endblock%}

{% include 'common/header.html' %}

<h1>Home Page</h1>

{% include 'common/footer.html' %}

Eg.
<!DOCTYPE html>
<html>
<head>
    <title>
        {% block title %}
        My Website
        {% endblock %}
    </title>
</head>

<body>

    {% include 'common/header.html' %}

    {% include 'common/navbar.html' %}

    <main>
        {% block content %}
        {% endblock %}
    </main>

    {% include 'common/footer.html' %}

</body>
</html>

  we can use extends & include for use base.html file in HTML Templates

***********************************************************************************  
##Database Connectivity in Django 
Create Database & Tables inside the Mysql
Install mysql connector 
===>pip install mysql-connector-python
Go To setting.py File of Project & Add Connection Database section
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Create Models as it same inside models.py but add one class inside 
class Meta:
    managed=False
    db_table='TableName'

After that Make migration & Migrate it & create super user
===>python manage.py makemigrations    --- Make migrations 
===>python manage.py migrate ---- migrate
===>python manage.py createsuperuser 
username
email
password
password again

Login with created credentials created before
http://127.0.0.1:8000/admin/

Register Database Model inside admin.py 
admin.site.register(Database Model Name)

***********************************************************************************

















