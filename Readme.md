# Student management System
The Purpose of this program is to create API to manage students data



## Django CRUD with MySQL overview
I build Rest Apis using Django Rest Framework that can create, retrieve, update, delete and find Students by Id.

First, I setup Django Project with a MySQL Client. Next, I create Rest-Api app, add it with Django Rest Framework to the project. Next, I define data model and migrate it to the database. Then i write API Views and define Routes for handling all CRUD operations.

The following table shows overview of the Rest APIs that will be exported:


| Methods |  Urls	        |Actions
|  :---:  | :---:               | :---:
|GET	  |api/management	|get all Students
|GET	|api/management/:id	|get Student by id
|POST	|api/management	|add new Student
|PUT	|api/management/:id	|update Student by id
|DELETE	|api/management/:id	|remove Student by id
|DELETE	|api/management	|remove all Students

We also need to setup MySQL Database engine.\
So open settings.py and change declaration of DATABASES:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': '****',
        'PASSWORD': '*****',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
} 
```

## Commands
Setting up this project in you system:\
First Clone it using:
```
git clone <url>
```
Then run the following commands to start the server

```python
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 
```
Dont Forget to change the database in settings.py


You are good to go now.\
Now test APIs on Postman swagger or any other websites  

## Bonus
There is an extra section named accounts. Where you can register and login\
we can also make our mangement's API login required but this isn't the task

# Overview
I Used swagger here for API Documentation.\
you can also visit the login register in django bowsable API view.\
I also rendered Dashboard.html. Where You will find all students data.\
There is also a button which allows you to add new student's data.\
Dashboard is also working on API, Gettting or Posting data using APIs.\
You will find dashboard at.
```
http://127.0.0.1:8000/api/dashboard
```