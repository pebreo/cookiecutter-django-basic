How To Run
==========

Step 1. Install cookiecutter
   
    $ pip install cookiecutter      

Step 2. Run cookiecutter 

    $ cookiecutter https://github.com:pebreo/cookiecutter-test2.git

Step 3. Syncdb
    
	$ cd myrepo
	$ python manage.py syncdb

Step 4. Runserver
    
	$ python manage.py runserver

Step 5. Run Django admin
 
     Goto: localhost:8000/admin