How To Run
==========

Step 1. Install cookiecutter
```   
$ pip install cookiecutter      
```
Step 2. Run cookiecutter 
```
$ cookiecutter git@github.com:myusername/cookiecutter-django-basic.git
NOTE: You can only run cookiecutter on the repo that you own.
```
Step 3. Install requirements
```
$ pip install -r requirements.txt
```

Step 4. Syncdb
```
$ cd myrepo
$ python manage.py syncdb
```
Step 5. Runserver
```    
$ python manage.py runserver
```
Step 6. Run Django admin
```
Goto: localhost:8000/admin
```
Todo
=====
1. Add 'static', 'assets', and 'media' folder
2. Add 'templates' folder
1. Add Heroku support
2. Add Django Vanilla View support
