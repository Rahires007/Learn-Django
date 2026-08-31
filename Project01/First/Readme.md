#Learning Django 
************************************************************************************************************
Django :- Django is nothing but Python Framework which provide ready made tool & structure for devlope webpages & web apps

Modules :- Modules are nothing but every python or .py extension file which contain class , methods & attributes 

Packages :- Pakages are nothing but the collection of modules & which consist of __init__.py file 

Library :- Library is nothing but the collection of packages 

************************************************************************************************************
#How to create First Django Project 
Steps :
Install Virtual Envornment Globally on System
===>pip install env ---Install Vitual Envornment on system
Create Workspace or Folder & Open Cmd in that workspace
Create virtual Envornment in it & Activate it
===>python -m venv VirtualEnvornmentName --Create Envornment
===>VirtualEnvornmentName\Scripts\actiate --Activate Envornment
Install Django in it & Create Project & Go To Project Folder
===>pip install django -- Install Django
===>django-admin startproject ProjectName -- Create Project
===>cd ProjectName
Create App in that Folder & Open it in vs code
===>python manage.py startapp AppName
===>code .

by Following Above steps we Successfully create one project
Run That Project 
===>python manage.py runserver
************************************************************************************************************
After Create First Project 
##Here we render a Functions or methods using path & include methods
Go to setting.py ---> Add App Name in installed apps section in single quotes
--->Go to urls.py file of Project --->Add path of urls.pyof App using path & include Methods
--->Create urls.py file in App before adding path --->Go to urls.py of app and path of any thing which we have render ---> Create same view name Method or Function inside views.py & Import in urls.py of app & Run the project using above Command
************************************************************************************************************