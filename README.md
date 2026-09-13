LEARN DJANGO
================================================================================

Steps:
Create Django Project Folder & Go inside that Django Project Folder
==> cd "Django Project Folder Name"

Create one Virtual Environment in it & Activate it
==> python -m venv EnvironmentName
    --- Create Virtual Environment

==> EnvironmentName\Scripts\activate
    --- Activate Virtual Environment

Install Django inside project & create Django project using django-admin & go
inside that project

==> pip install django
    --- Install Django

==> django-admin startproject ProjectName
    --- Create Django Project

==> cd ProjectName
    --- Go inside Django Project

Create App in it & open it in VS Code editor

==> python manage.py startapp AppName
    --- Create Django App

==> code .
    --- Open project in VS Code


EXAMPLE:

cd "Django Project Folder"

python -m venv env

env\Scripts\activate

pip install django

django-admin startproject MyProject

cd MyProject

python manage.py startapp home

code .


FOR RUN THE DJANGO PROJECT:

python manage.py runserver



ADD APP NAME INSIDE settings.py


After creating the App, we have to add App Name inside settings.py file of
Django Project in INSTALLED_APPS list.

Example:

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

Example:

If we create an App named "home":

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
]



CREATE TEMPLATE FOLDER


Create a templates folder inside the main project folder.

Do NOT create the project-level templates folder inside the Django project
configuration folder.

Example Project Structure:

MyProject/
|
|-- manage.py
|
|-- MyProject/                  <- Django Project Configuration Folder
|   |-- settings.py
|   |-- urls.py
|   |-- ...
|
|-- home/                       <- App 1
|   |-- views.py
|   |-- models.py
|   |-- ...
|
|-- accounts/                   <- App 2
|   |-- views.py
|   |-- models.py
|   |-- ...
|
|-- templates/                  <- Create this yourself
    |
    |-- home/                   <- Templates for home app
    |   |-- index.html
    |   |-- about.html
    |
    |-- accounts/               <- Templates for accounts app
        |-- login.html
        |-- register.html


After creating the templates folder, add its path inside settings.py file of
Django Project inside TEMPLATES section.

Example:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


If we directly create HTML webpages inside the templates folder:

templates/
|
|-- index.html
|-- about.html
|-- contact.html

Then we can use:

'DIRS': [BASE_DIR / 'templates']

And render the page using:

return render(request, 'index.html')


FLOW OF HOW TEMPLATES WILL RENDER ON REQUEST:

Browser Request
      |
      v
Project urls.py
      |
      v
App urls.py
      |
      v
views.py
      |
      v
render()
      |
      v
templates/home/index.html
      |
      v
HTML Response



CREATE SEPARATE PATH FOR EACH APP INSIDE urls.py


Create separate path for each App inside the urls.py of Django Project using
path() and include().

Syntax:

path('AppPath/', include('AppName.urls'))


Example:

Inside urls.py of Django Project:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('AppPath/', include('AppName.urls')),
]


Example with home App:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', include('home.urls')),
]


After that create urls.py inside Django App.


APP STRUCTURE:

home/
|
|-- migrations/
|-- admin.py
|-- apps.py
|-- models.py
|-- tests.py
|-- views.py
|-- urls.py             <- Create this


Inside home/urls.py:

from django.urls import path
from .views import ViewName

urlpatterns = [
    path('Path/', ViewName),
]


Example:

from django.urls import path
from .views import HomePage

urlpatterns = [
    path('home/', HomePage),
]


CONNECTION FLOW:

Project urls.py
      |
      v
App urls.py
      |
      v
ViewName
      |
      v
views.py
      |
      v
render()
      |
      v
Template Page



CREATE VIEW INSIDE views.py


Create ViewName inside views.py.

The ViewName used inside urls.py must be imported from views.py.

Example:

Inside views.py:

from django.shortcuts import render

def ViewName(request):
    return render(request, 'AppName/web.html')


Here:

'AppName/web.html'

means:

templates/
|
|-- AppName/
    |-- web.html


Example:

from django.shortcuts import render

def HomePage(request):
    return render(request, 'home/index.html')



render() AND HttpResponse()


render() function is used to render HTML webpages as a response to a request.

HttpResponse() function is used to return a message or other HTTP response
directly.

Before using HttpResponse(), we have to write:

from django.http import HttpResponse


Example:

from django.http import HttpResponse

def HomePage(request):
    return HttpResponse("Welcome to Django")


FLOW OF RENDER HTML TEMPLATE:

Request
   |
   v
View
   |
   v
render()
   |
   v
HTML Template
   |
   v
Response


FLOW OF RESPONSE MESSAGE:

Request
   |
   v
View
   |
   v
HttpResponse()
   |
   v
"Welcome to Django"
   |
   v
Response



CREATE DATABASE MODEL INSIDE DJANGO APP


Create Database Model inside Django App inside models.py.

Syntax:

class ModelName(models.Model):
    ColumnName = models.DataTypeField(...)


Example:

Inside models.py:

from django.db import models

class Student(models.Model):

    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Name


Here:

Student
    -> Database Model Name

Name
    -> Database Column

Age
    -> Database Column

Email
    -> Database Column

CharField
    -> Data Type

IntegerField
    -> Data Type

EmailField
    -> Data Type


__str__() is used to return a readable string representation of the model
object, especially in Django Admin.



MAKEMIGRATIONS AND MIGRATE


After creating Database Model:

==> python manage.py makemigrations
    --- Create migration files based on changes in models.py

==> python manage.py migrate
    --- Apply migrations to the database


We have to use makemigrations and migrate whenever we make changes to
Django-managed Database Models, such as adding or changing fields.

FLOW:

Create / Change Model
        |
        v
makemigrations
        |
        v
migrate
        |
        v
Database Updated



CREATE SUPERUSER


Create Superuser:

==> python manage.py createsuperuser

Django will ask:

Username
Email
Password
Password Again


After successful creation:

Superuser created successfully.


Run the project:

==> python manage.py runserver


Open Django Admin:

http://127.0.0.1:8000/admin/


Login using the same credentials created while creating the superuser.



REGISTER DATABASE MODEL IN ADMIN PANEL


Open admin.py inside Django App.

Example:

from django.contrib import admin
from .models import Student

admin.site.register(Student)


Now Student Model will be available in Django Admin Panel.


FLOW OF MIGRATION & CREATE USER ACCOUNT:

Create Model in models.py
        |
        v
python manage.py makemigrations
        |
        v
python manage.py migrate
        |
        v
Register Model in admin.py
        |
        v
python manage.py createsuperuser
        |
        v
python manage.py runserver
        |
        v
/admin/
        |
        v
Login with Superuser
        |
        v
Manage Database Model



GET DATA USING DATABASE MODEL


Get all data:

Data = Student.objects.all()

This gets all records from the Student Database Model.


ADD DATA INSIDE DATABASE MODEL:

Student.objects.create(
    Name="Rahul",
    Age=22,
    Email="rahul@gmail.com"
)


We can also send values extracted from request:

Student.objects.create(
    Name=Name,
    Age=Age,
    Email=Email
)



EXTRACT DATA FROM REQUEST & SEND TO DATABASE MODEL


To extract data from HTML form:

Name = request.POST.get('Name')

Here 'Name' must match the name attribute of HTML input.


Example HTML:

<input type="text" name="Name">
<input type="number" name="Age">
<input type="email" name="Email">


Then in Django:

Name = request.POST.get('Name')
Age = request.POST.get('Age')
Email = request.POST.get('Email')


IMPORTANT:

We must add method="POST" in the form and CSRF token.

Example:

<form method="POST">

    {% csrf_token %}

    <input type="text" name="Name">
    <input type="number" name="Age">
    <input type="email" name="Email">

    <button type="submit">Submit</button>

</form>


COMPLETE EXAMPLE:

Inside views.py:

from django.shortcuts import render
from .models import Student


def StudentData(request):

    if request.method == 'POST':

        Name = request.POST.get('Name')
        Age = request.POST.get('Age')
        Email = request.POST.get('Email')

        Student.objects.create(
            Name=Name,
            Age=Age,
            Email=Email
        )

    Data = Student.objects.all()

    return render(
        request,
        'student/student.html',
        {'Data': Data}
    )



SEND & DISPLAY DATA ON HTML WEBPAGE


Send Data from View to HTML Template:

return render(
    request,
    'student/student.html',
    {'Data': Data}
)


Here:

Data
    -> Variable available inside HTML Template.


Display QuerySet:

{{ Data }}


Display Data using For Loop:

{% for Key in Data %}

    {{ Key.Name }}
    {{ Key.Age }}
    {{ Key.Email }}

{% endfor %}


Here:

Data
    -> Contains all Student objects

Key
    -> Contains one Student object at a time


Example:

{% for Key in Data %}

    <h2>{{ Key.Name }}</h2>
    <p>{{ Key.Age }}</p>
    <p>{{ Key.Email }}</p>

{% endfor %}



CREATE STATIC FOLDER


Create static folder inside the main project folder at the same level as
manage.py.

Do NOT create the project-level static folder inside the Django project
configuration folder.

Create separate folders for CSS, JavaScript and Images.


PROJECT STRUCTURE:

MyProject/
|
|-- manage.py
|
|-- MyProject/                  <- Django Project Folder
|   |-- settings.py
|   |-- urls.py
|   |-- ...
|
|-- AppName1/
|-- AppName2/
|
|-- templates/                  <- HTML Templates
|   |-- AppName1/
|   |-- AppName2/
|
|-- static/                     <- Static Files
    |
    |-- css/                    <- CSS Files
    |
    |-- js/                     <- JavaScript Files
    |
    |-- images/                 <- Images



ADD STATIC FOLDER PATH INSIDE settings.py


Inside settings.py:

STATIC_URL = 'static/'


Add:

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


Complete:

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]



USE EXTERNAL CSS IN HTML TEMPLATES


At the top of HTML file:

{% load static %}


Use CSS file inside head section:

<link rel="stylesheet" href="{% static 'css/File.css' %}">


Correct Django syntax:

{% static 'css/File.css' %}



USE EXTERNAL JAVASCRIPT IN HTML TEMPLATES


At the top of HTML file:

{% load static %}


Use JavaScript file:

<script src="{% static 'js/File.js' %}"></script>



USE IMAGE FROM STATIC FOLDER


Example:

<img src="{% static 'images/photo.jpg' %}" alt="Photo">



CREATE COMMON CODE FILE INSIDE TEMPLATE FOLDER


We can create a common base.html file inside the templates folder.

We can also create a common folder for common HTML files.

templates/
|
|-- base.html
|
|-- common/
|   |-- header.html
|   |-- navbar.html
|   |-- footer.html
|
|-- home/
|   |-- index.html
|
|-- accounts/
    |-- login.html



INCLUDE


We can use {% include %} to include common HTML files.

Example:

{% include 'common/header.html' %}

<h1>Home Page</h1>

{% include 'common/footer.html' %}


Similarly:

{% include 'common/navbar.html' %}



BLOCK


We can add blocks for code that is different on different webpages.

Syntax:

{% block Blockname %}

    Lines of code

{% endblock %}


Example:

{% block content %}

    <h1>Home Page</h1>

{% endblock %}



base.html


Example:

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



EXTENDS


We can use {% extends %} to use base.html file in other HTML Templates.

Example:

{% extends 'base.html' %}


{% block title %}
    Home Page
{% endblock %}


{% block content %}

    <h1>Welcome to Home Page</h1>

{% endblock %}


DIFFERENCE:

extends
    -> Used to inherit the base template structure.

include
    -> Used to include a small/common HTML file.


FLOW:

base.html
    |
    v
extends
    |
    v
home/index.html


common/header.html
common/navbar.html
common/footer.html
        |
        v
      include
        |
        v
     base.html



DATABASE CONNECTIVITY IN DJANGO


We can connect Django with MySQL Database.

First create the Database and Tables inside MySQL if required.



INSTALL MYSQL CONNECTOR


Install MySQL Connector:

==> pip install mysql-connector-python



DATABASE CONFIGURATION IN settings.py


Go to settings.py file of Django Project and add Database connection.

Example:

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


The database engine/connector must be compatible with the installed Django
and connector versions.


CREATE MODEL FOR EXISTING MYSQL TABLE


If we want Django to work with an existing database table without allowing
Django migrations to create or modify that table, we can use:

class Meta:
    managed = False
    db_table = 'TableName'


Example:

from django.db import models


class Student(models.Model):

    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField()

    class Meta:
        managed = False
        db_table = 'Student'


managed = False
    -> Django does not manage the table using migrations.

db_table = 'Student'
    -> Specifies the existing database table name.


IMPORTANT:

If we want Django to create and manage the table normally, we should not use
managed = False.



MAKEMIGRATIONS AND MIGRATE FOR NORMAL DJANGO MODELS


==> python manage.py makemigrations

==> python manage.py migrate


If the model uses:

managed = False

Django will not create/manage that existing table through migrations.



CREATE SUPERUSER


==> python manage.py createsuperuser

Enter:

Username
Email
Password
Password Again


Run:

==> python manage.py runserver


Login:

http://127.0.0.1:8000/admin/


Register Database Model inside admin.py:

from django.contrib import admin
from .models import Student

admin.site.register(Student)



AUTHENTICATION & AUTHORIZATION IN DJANGO


AUTHENTICATION:

Authentication is the process of checking whether a user is valid or not.

It verifies the user's identity, usually using a username and password.

Example:

Username + Password
        |
        v
Is this a valid user?


AUTHORIZATION:

Authorization is the process of checking a user's privileges and rights.

It determines what an authenticated user is allowed to access or perform.

Example:

User is authenticated
        |
        v
What is the user allowed to access?
        |
        v
Dashboard / Profile / Admin / Other Permission


Django provides built-in features for both Authentication and Authorization
through its authentication system.



STEPS TO IMPLEMENT AUTHENTICATION IN DJANGO


1. CREATE LOGIN FORM

Create HTML login form using POST method and add {% csrf_token %} for
CSRF protection.

Example:

<form method="POST">

    {% csrf_token %}

    <input
        type="text"
        name="username"
        placeholder="Username"
    >

    <input
        type="password"
        name="password"
        placeholder="Password"
    >

    <button type="submit">
        Login
    </button>

</form>


================================================================================
2. CREATE LOGIN VIEW
================================================================================

Create a View to handle Login Form submission.

Import:

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


Example:

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("/dashboard/")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(request, "login.html")


IMPORTANT FUNCTIONS:

authenticate()
    -> Checks whether username and password are valid.

login()
    -> Logs the authenticated user into the session.


If authenticate() is successful:

user object
    -> Returned

If authentication fails:

None
    -> Returned



3. CREATE URL PATH FOR LOGIN


Create urls.py inside App.

Example:

from django.urls import path
from .views import login_view

urlpatterns = [

    path("login/", login_view),

]


We are using direct URL path and not using name=.



4. CREATE USER BEFORE TESTING


Before testing Authentication, create a user in Django Admin Panel under
Users section.

We can also create a user using command line:

python manage.py createsuperuser


Then open:

http://127.0.0.1:8000/admin/


Login using created credentials.



PROTECTING PAGES USING @login_required


Sometimes we don't want an unauthenticated user to directly access certain
pages.

For example, we have a Dashboard page.

We want Dashboard to be accessible only after Login.

Django provides @login_required decorator for this purpose.


Import:

from django.contrib.auth.decorators import login_required


Then apply it above the View:

@login_required
def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )



WHAT DOES @login_required DO?


When user tries to access Dashboard:

If user is logged in:

User Logged In
      |
      v
Dashboard Page


If user is not logged in:

User Not Logged In
      |
      v
Login Page


FLOW:

User requests Dashboard
        |
        v
Is user logged in?
     /       \
   YES       NO
    |         |
    v         v
Dashboard   Login Page


We can protect multiple Views:

@login_required
def profile(request):

    return render(
        request,
        "profile.html"
    )


@login_required
def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )


@login_required
def orders(request):

    return render(
        request,
        "orders.html"
    )



CONFIGURE LOGIN URL


By default Django needs to know where to redirect unauthenticated user.

Inside settings.py:

LOGIN_URL = "/login/"


Now if user tries to access a page protected by @login_required without Login,
Django redirects the user to:

/login/



IMPLEMENT LOGOUT IN DJANGO


Django provides built-in logout() function.

Import:

from django.contrib.auth import logout


Create Logout View:

def logout_view(request):

    logout(request)

    return redirect("/login/")


logout(request)
    -> Logs the user out and removes authentication information from session.



CREATE URL PATH FOR LOGOUT


Inside App urls.py:

from django.urls import path
from .views import login_view, logout_view

urlpatterns = [

    path("login/", login_view),

    path("logout/", logout_view),

]


No name= is required because we are using direct URL.



CREATE LOGOUT BUTTON


Use direct URL:

<a href="/logout/">
    Logout
</a>


When user clicks Logout:

Click Logout
     |
     v
/logout/
     |
     v
logout_view()
     |
     v
logout(request)
     |
     v
User Session Removed
     |
     v
Redirect to /login/



COMPLETE AUTHENTICATION FLOW


                LOGIN
                  |
                  v
          Login Form (POST)
                  |
                  v
       Extract username/password
                  |
                  v
            authenticate()
                  |
        +---------+---------+
        |                   |
        v                   v
   Valid User          Invalid User
        |                   |
        v                   v
 login(request,user)    Show Error
        |
        v
    Dashboard
        |
        v
  @login_required
        |
        v
Only authenticated users
can access protected pages
        |
        v
      Logout
        |
        v
  logout(request)
        |
        v
   Login Page



IMPORTANT DJANGO AUTHENTICATION FUNCTIONS


authenticate()
    -> Checks username and password.

login()
    -> Logs authenticated user into session.

logout()
    -> Logs user out and clears authentication information.

@login_required
    -> Prevents unauthenticated users from accessing protected View.

{% csrf_token %}
    -> Provides CSRF protection for POST forms.


IN SHORT:

Authentication
    -> Who are you?

Authorization
    -> What are you allowed to do?

authenticate()
    -> Verify credentials.

login()
    -> Start authenticated session.

@login_required
    -> Don't allow unauthenticated users to access protected pages.

logout()
    -> End authenticated session.



API CREATION IN DJANGO


API:

API stands for Application Programming Interface.

API is used to send and receive data between Client and Server.

In Django we can create API using Django REST Framework (DRF).

Django REST Framework provides features to create REST APIs.



CRUD OPERATIONS


CRUD means:

C -> Create
R -> Read
U -> Update
D -> Delete


HTTP Methods used for CRUD:

POST
    -> Create Data

GET
    -> Read Data

PUT
    -> Update Data

DELETE
    -> Delete Data



STEPS TO CREATE API IN DJANGO


STEP 1: INSTALL DJANGO REST FRAMEWORK

Install Django REST Framework inside Virtual Environment:

==> pip install djangorestframework



STEP 2: ADD REST FRAMEWORK INSIDE settings.py


Go to settings.py of Django Project.

Add:

'rest_framework',

inside INSTALLED_APPS.

Example:

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'home',
]



STEP 3: CREATE DATABASE MODEL


We can create API using existing Database Model or create a new Database Model.

Example:

Inside models.py:

from django.db import models


class Student(models.Model):

    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Name


After creating Database Model:

==> python manage.py makemigrations

==> python manage.py migrate



STEP 4: CREATE SERIALIZER


Serializer is used to convert Database Model data into JSON data.

It can also convert JSON data received from API into Python/Django data that
can be saved into Database Model.

Create a new file:

serializers.py

inside Django App.


APP STRUCTURE:

home/
|
|-- migrations/
|-- admin.py
|-- apps.py
|-- models.py
|-- serializers.py       <- Create this
|-- tests.py
|-- views.py
|-- urls.py


Inside serializers.py:

from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = '__all__'


HERE:

StudentSerializer
    -> Serializer Class

model = Student
    -> Which Database Model we want to use

fields = '__all__'
    -> Use all fields of Database Model



STEP 5: CREATE API VIEW


Go to views.py of Django App.

Import required classes:

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


Create API View:

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def StudentAPI(request):


    # GET - Read Data

    if request.method == 'GET':

        Data = Student.objects.all()

        serializer = StudentSerializer(
            Data,
            many=True
        )

        return Response(serializer.data)


    # POST - Create Data

    elif request.method == 'POST':

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )


    # PUT - Update Data

    elif request.method == 'PUT':

        ID = request.data.get('id')

        Data = Student.objects.get(id=ID)

        serializer = StudentSerializer(
            Data,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=400
        )


    # DELETE - Delete Data

    elif request.method == 'DELETE':

        ID = request.data.get('id')

        Data = Student.objects.get(id=ID)

        Data.delete()

        return Response(
            {
                "Message": "Student Deleted Successfully"
            }
        )



UNDERSTAND API VIEW


@api_view()

Used to tell Django REST Framework which HTTP methods are allowed in API.

Example:

@api_view(['GET', 'POST', 'PUT', 'DELETE'])


This API accepts:

GET
POST
PUT
DELETE


request.data

Used to get data sent by API Client.

Example:

Name = request.data.get('Name')
Age = request.data.get('Age')
Email = request.data.get('Email')


Response()

Used to send response from API.

Example:

return Response(serializer.data)


serializer.is_valid()

Checks whether received data is valid according to Serializer.

Example:

if serializer.is_valid():


serializer.save()

Used to save new data or update existing data through Serializer.

Example:

serializer.save()



STEP 6: CREATE URL FOR API


Create urls.py inside Django App if it is not already created.

Example:

home/
|
|-- migrations/
|-- admin.py
|-- apps.py
|-- models.py
|-- serializers.py
|-- tests.py
|-- views.py
|-- urls.py


Inside App urls.py:

from django.urls import path
from .views import StudentAPI


urlpatterns = [

    path('students/', StudentAPI),

]



STEP 7: CONNECT APP URLS WITH PROJECT URLS


Go to urls.py of Django Project.

Example:

from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('home/', include('home.urls')),

]


Now API URL will be:

http://127.0.0.1:8000/home/students/



CRUD OPERATIONS IN API



1. POST - CREATE DATA
--------------------------------

POST method is used to add new data inside Database.

API URL:

/home/students/

Method:

POST


Send JSON data:

{
    "Name": "Rahul",
    "Age": 22,
    "Email": "rahul@gmail.com"
}


Flow:

POST Request
      |
      v
request.data
      |
      v
Serializer
      |
      v
serializer.is_valid()
      |
      v
serializer.save()
      |
      v
Database
      |
      v
Response


Response:

{
    "id": 1,
    "Name": "Rahul",
    "Age": 22,
    "Email": "rahul@gmail.com"
}



2. GET - READ DATA


GET method is used to get data from Database.

API URL:

/home/students/

Method:

GET


View:

Data = Student.objects.all()

serializer = StudentSerializer(
    Data,
    many=True
)

return Response(serializer.data)


Response:

[
    {
        "id": 1,
        "Name": "Rahul",
        "Age": 22,
        "Email": "rahul@gmail.com"
    },
    {
        "id": 2,
        "Name": "Priya",
        "Age": 21,
        "Email": "priya@gmail.com"
    }
]


Here:

many=True

is used because we are serializing multiple Student objects.


3. PUT - UPDATE DATA


PUT method is used to update existing data inside Database.

API URL:

/home/students/

Method:

PUT


Send JSON data:

{
    "id": 1,
    "Name": "Rahul Sharma",
    "Age": 23,
    "Email": "rahulsharma@gmail.com"
}


Flow:

PUT Request
     |
     v
Get ID from request.data
     |
     v
Find Student from Database
     |
     v
Serializer
     |
     v
serializer.is_valid()
     |
     v
serializer.save()
     |
     v
Updated Data
     |
     v
Response



4. DELETE - DELETE DATA


DELETE method is used to delete existing data from Database.

API URL:

/home/students/

Method:

DELETE


Send JSON data:

{
    "id": 1
}


Flow:

DELETE Request
      |
      v
Get ID from request.data
      |
      v
Find Student
      |
      v
Data.delete()
      |
      v
Database Data Deleted
      |
      v
Response


Response:

{
    "Message": "Student Deleted Successfully"
}



API TESTING


We can test API using:

Postman
Thunder Client
Django REST Framework Browsable API


Run Django Project:

python manage.py runserver


API URL:

http://127.0.0.1:8000/home/students/


In Postman we can select different HTTP methods:

POST
    -> Add Student

GET
    -> Get Student

PUT
    -> Update Student

DELETE
    -> Delete Student



COMPLETE API FLOW


Client / Postman
       |
       v
API URL
       |
       v
Project urls.py
       |
       v
App urls.py
       |
       v
views.py
       |
       v
Serializer
       |
       v
Model
       |
       v
Database
       |
       v
Serializer
       |
       v
JSON Response
       |
       v
Client / Postman



API DATA FLOW


FOR SENDING DATA FROM CLIENT TO DATABASE:

Client
   |
   v
JSON Data
   |
   v
request.data
   |
   v
Serializer
   |
   v
is_valid()
   |
   v
save()
   |
   v
Model
   |
   v
Database


FOR GETTING DATA FROM DATABASE:

Database
   |
   v
Model
   |
   v
Serializer
   |
   v
JSON
   |
   v
Response
   |
   v
Client



IMPORTANT DJANGO REST FRAMEWORK TERMS


djangorestframework

    -> Package used to create REST APIs in Django.


@api_view()

    -> Used to create Function-Based API View and specify allowed HTTP
       methods.


request.data

    -> Used to get data sent by API Client.


Response()

    -> Used to send API response.


Serializer

    -> Converts Model data into JSON and JSON data into Python/Django data.


serializer.is_valid()

    -> Checks whether received data is valid or not.


serializer.save()

    -> Saves new data or updates existing data.



CRUD IN SHORT


POST
 |
 v
CREATE
 |
 v
Add New Data


GET
 |
 v
READ
 |
 v
Get Existing Data


PUT
 |
 v
UPDATE
 |
 v
Modify Existing Data


DELETE
 |
 v
DELETE
 |
 v
Remove Existing Data



COMPLETE DJANGO API STRUCTURE


MyProject/
|
|-- manage.py
|
|-- MyProject/
|   |-- settings.py
|   |-- urls.py
|   |-- ...
|
|-- home/
|   |-- migrations/
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|   |-- tests.py
|
|-- templates/
|
|-- static/


MAIN API FLOW:

Model
  |
  v
Serializer
  |
  v
View
  |
  v
URL
  |
  v
API



OVERALL DJANGO PROJECT FLOW


Browser / Client
       |
       v
URL Request
       |
       v
Project urls.py
       |
       v
App urls.py
       |
       v
View
       |
       +----------------------+
       |                      |
       v                      v
   Template                 Model
       |                      |
       v                      v
HTML Response             Database
                              |
                              v
                             Data


FOR NORMAL DJANGO WEBPAGE:

Browser
   |
   v
urls.py
   |
   v
views.py
   |
   v
Model
   |
   v
Database
   |
   v
View
   |
   v
Template
   |
   v
HTML Response
   |
   v
Browser


FOR API:

Client / Postman
       |
       v
API URL
       |
       v
urls.py
       |
       v
API View
       |
       v
Serializer
       |
       v
Model
       |
       v
Database
       |
       v
Serializer
       |
       v
JSON Response
       |
       v
Client



DJANGO TOPICS LEARNED


1. Django Project Creation
        |
        v
2. Virtual Environment
        |
        v
3. Django Installation
        |
        v
4. Django Project
        |
        v
5. Django App
        |
        v
6. settings.py
        |
        v
7. URLs
        |
        v
8. Views
        |
        v
9. Templates
        |
        v
10. Static Files
        |
        v
11. Models
        |
        v
12. Migrations
        |
        v
13. Django Admin
        |
        v
14. Database Connectivity
        |
        v
15. Authentication
        |
        v
16. Authorization
        |
        v
17. Login
        |
        v
18. @login_required
        |
        v
19. Logout
        |
        v
20. Django REST Framework
        |
        v
21. API
        |
        v
22. CRUD Operations



IMPORTANT DJANGO COMMANDS


Create Virtual Environment:

python -m venv env


Activate Virtual Environment:

env\Scripts\activate


Install Django:

pip install django


Create Django Project:

django-admin startproject MyProject


Go Inside Project:

cd MyProject


Create App:

python manage.py startapp home


Open VS Code:

code .


Run Server:

python manage.py runserver


Create Migrations:

python manage.py makemigrations


Apply Migrations:

python manage.py migrate


Create Superuser:

python manage.py createsuperuser


Install Django REST Framework:

pip install djangorestframework



FINAL IMPORTANT CONCEPTS


Django Project
      |
      v
Contains multiple Apps


App
      |
      v
Contains Views, Models, URLs, etc.


urls.py
      |
      v
Handles URL Routing


views.py
      |
      v
Handles Request & Response Logic


models.py
      |
      v
Handles Database Structure


templates/
      |
      v
Contains HTML Pages


static/
      |
      v
Contains CSS, JavaScript & Images


admin.py
      |
      v
Register & Manage Models in Admin Panel


serializers.py
      |
      v
Used for API Model <-> JSON Conversion


Django REST Framework
      |
      v
Used to Create APIs


Authentication
      |
      v
Who are you?


Authorization
      |
      v
What are you allowed to do?


@login_required
      |
      v
Allow Only Logged-in Users


CRUD
      |
      v
Create -> Read -> Update -> Delete



DJANGO IN ONE FLOW


                  DJANGO
                     |
                     v
             Create Project
                     |
                     v
               Create App
                     |
                     v
              settings.py
                     |
                     v
        Add App in INSTALLED_APPS
                     |
                     v
                Create URLs
                     |
                     v
                Create Views
                     |
                     v
              Create Templates
                     |
                     v
              Create Static Files
                     |
                     v
              Create Database
                     |
                     v
                  Models
                     |
                     v
               Migrations
                     |
                     v
              Django Admin
                     |
                     v
          Authentication
                     |
                     v
           Authorization
                     |
                     v
             Login / Logout
                     |
                     v
            @login_required
                     |
                     v
         Django REST Framework
                     |
                     v
                    API
                     |
                     v
                  CRUD
                     |
          +----------+----------+
          |          |          |
          v          v          v
        POST        GET        PUT
          |          |          |
          v          v          v
       CREATE       READ      UPDATE
                                |
                                v
                              DELETE
