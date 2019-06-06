# netprofit-django

Back End - Django

Steps for create a django app on local machine,
	-sudo apt-get install python-pip python-virtualenv python-setuptools python-dev build-essential  python3.6

-install virtualenv for run django project
		-sudo pip install virtualenv
	-create virtualenv 
		-virtualenv <virtualenv name>
		-eg : virtualenv myprojectenv
	-activate virtualenv
		-source myprojectenv/bin/activate

	-To deactivate virtualenv
		-deactivate
	-Install django
		-pip install django
	-create a django app
		-django-admin.py startproject <project-name>
		-eg: django-admin.py startproject djangoapp
	-enter into project folder
		-cd djangoapp
	-create apps on django projects by,
		-python manage.py startapp <appname>
	-run django app
		-python manage.py runserver

--------------------------------------------------------------
Steps for run a github django project on local machine 

-Create and activate virtual environment
-install django packages using pip install
-django-cors-headers  2.4.0
-djangorestframework 3.9.0
-drf-writable-nested  0.5.1
-psycopg2  2.7.7
-Django 2.1.3


Clone the project by using git clone command.
-example
git clone https://github.com/adithyanps/my_portfolio

	Enter into project folder.
		-cd my_portfolio
------------------------
Database setup
	-goto settings.py on django project
	-we can see like,
		
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netprofit',
        'USER':'postgres',
        'PASSWORD':'test123',
        'HOST':'127.0.0.1',
        'PORT':'5432'

    }
}

-first we need to create a database with same name in settings.py.

We need to migrate all models in the project.
-python manage.py makemigrations
-python manage.py migrate
Create a super user by,
	-python manage.py createsuperuser
Run django app by,
	-python manage.py runserver

Successfully completed django app !!!

------------------------------------------------------------------------------------------------------------
