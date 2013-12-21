How it works
==========
Cookiecutter is a command line utility that makes project templating easy. It works by taking variables from a JSON file full of variable and filling them into Jinja syntaxed variable names. The variables in the JSON can be for directory names, file names, and file contents. 

You can use Cookiecutter from a local cookiecutter project (CP) or remotely from a github repo. But keep in mind that cookiecutter will copy the remote CP into your ~/.cookiecutters directory, so once you run cookiecutter on a remote repo, you only have to invoke the local copy.

So instead of doing this:
`cookiecutter git@github.com:myuserid/my-cp.git`

You do this:
`cookiecutter ~/.cookiecutter/my-cp.git`

How To Run
==========

Step 1. Install cookiecutter
```   
$ pip install cookiecutter      
```
Step 2. Run cookiecutter 
```
$ cookiecutter git@github.com:pebreo/cookiecutter-django-basic.git
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
1. Add 'assets' and 'media' folder
1. Add Heroku support
2. Add Django Vanilla View support
