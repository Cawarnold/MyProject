## Heroku_DjangoApp_20150401

# Getting Started with Django on Heroku
## https://devcenter.heroku.com/articles/getting-started-with-django

# Directory
## C:\Users\Christian\Documents\GitHub\MyProject\Python\Heroku_DjangoApp

# Today, with mobile front-ends, cloud back-ends, and fully automated management infrastructure, 
# companies are able to launch across many countries at a very high speed with a strong, technology 
# and analytics-enabled central infrastructure and light local teams.

## http://work.thaslwanter.at/Stats/html/statsPreface.html
## https://code.djangoproject.com/wiki/DjangoGraphviz

# Setting up Django on Heroku with Postgresql
## https://thefreshlybaked.wordpress.com/2014/07/09/setting-up-django-on-heroku-with-postgresql/



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### Short Notes ####




########################################################################################################################
########################################################################################################################
########################################################################################################################

#### Full Notes ####

# Prerequisites

# The Heroku Toolbelt, as described in Getting Started with Python.
# Installed Python and Virtualenv in a unix-style environment. See this guide for guidance.
# An installed version of Postgres to test locally.
# A Heroku user account. Signup is free and instant.


#### Start a Django app inside a Virtualenv ####

# First, we’ll create an empty top-level directory for our project:
$ mkdir hellodjango && cd hellodjango
# Make sure you’re using the latest virtualenv release. 
# If you’re using a version that comes with Ubuntu, you may need to add the --no-site-packages flag.
# Next, we’ll create a Python Virtualenv (v1.0+):
$ virtualenv venv
# New python executable in venv/bin/python
# Installing setuptools, pip...done.

	# FOR conda:
		# list all envs:
			conda info -e
		# create env called ENV:
			conda create -n ENV anaconda
		# Activate the environment ENV with:
			source activate ENV
		#or
			activate ENV
		# Deactivate with:
			source deactivate
		#or
			deactivate


	## Now looks like:
	# [ENV_HEROKU_DJANGO_20150401] C:\Users\Christian\Documents\GitHub\MyProject\Python\Heroku_DjangoApp\hellodjango>

# Next, install our application’s dependencies with pip. 
# In this case, we will be installing django-toolbelt, which includes all of the packages we need:
	# Django (the web framework)
	# Gunicorn (WSGI server)
	# dj-database-url (a Django configuration helper)
	# dj-static (a Django static file server)

# From your virtualenv:
$  pip install django-toolbelt
#Installing collected packages: Django, psycopg2, gunicorn, dj-database-url, dj-static, static
#  ...
#Successfully installed Django psycopg2 gunicorn dj-database-url dj-static static
#Cleaning up...

	# FOR conda:
		# List packages:
			conda list
		# Install package:
			conda install -p ~/anaconda/envs/ENV_HEROKU_DJANGO_20150401 django
		## conda does not have django-toolbelt so get it through pip.

# Now that we have a clean Python environment to work in, we’ll create our simple Django application.

# Don’t forget the . at the end. 
# This tells Django to put the extract the into the current directory, 
# instead of putting it in a new subdirectory.

$  django-admin.py startproject hellodjango .

## We have now started a project in the directory hellodjango using a virtual env.

#######
#######

#### Declare process types with Procfile #### 

# Use a Procfile, a text file in the root directory of your application, 
# to explicitly declare what command should be executed to start a web dyno. 
# In this case, you need to execute Gunicorn with a few arguments.
# Here’s a Procfile for our new app. 
# It should be called Procfile and live at the root directory of our project:

### Procfile

#/hellodjango/Procfile
web: gunicorn hellodjango.wsgi --log-file -

# You can now start the processes in your Procfile locally using Foreman (installed as part of the Heroku Toolbelt):
$ foreman start
# 2013-04-03 16:11:22 [8469] [INFO] Starting gunicorn 0.17.2
# 2013-04-03 16:11:22 [8469] [INFO] Listening at: http://127.0.0.1:8000 (8469)

# Make sure things are working properly curl or a web browser, then Ctrl-C to exit.

	# I got:
	# 11:57:39 web.1  | started with pid 5180
	# 11:57:46 web.1  | exited with code 1
	# 11:57:46 system | sending SIGKILL to all processes

Make sure things are working properly curl or a web browser, then Ctrl-C to exit.

#######
#######

#### Specify dependencies with Pip ####

# Heroku recognizes Python applications by the existence of a requirements.txt file 
# in the root of a repository. This simple format is used by most Python projects 
# to specify the external Python modules the application requires.

# Pip has a nice command (pip freeze) that will generate this file for us:
# $ pip freeze > requirements.txt
# Pip can also be used for advanced dependency management. 
# See Python Dependencies via Pip to learn more.

#######
#######

#### Django settings ####

# Next, configure the application for the Heroku environment, including Heroku’s Postgres database. 
# The dj-database-url module will parse the value of the DATABASE_URL environment variable and 
# convert them to something Django can understand.
# Make sure ‘dj-database-url’ is in your requirements file, 
# then add the following to the bottom of your settings.py file:

# settings.py

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

	## I've commented out variables that I thought were over lapping.

# With these settings available, you can add the following code to wsgi.py 
# to serve static files in production:

wsgi.py

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

# Store your app in Git

# Now that we’ve written and tested our application, 
# we need to store the project in a Git repository.
# Since our current directory contains a lof of extra files, 
# we’ll want to configure our repository to ignore these files with a .gitignore file:
# GitHub provides an excellent Python gitignore file that can be installed system-wide.

.gitignore

venv
*.pyc
staticfiles


############################################################################
############################################################################
############################################################################

## Restart Env with:
	# C:\Users\Christian\Documents\GitHub\MyProject\Python\Heroku_DjangoApp\hellodjango>
	# activate ENV_HEROKU_DJANGO_20150401

## Login to Heroku:
	# C:\Users\Christian\Documents\GitHub\MyProject\Python\Heroku_DjangoApp\hellodjango>
	# heroku login

## Push to heroku:
	# Push app from base directory of the project.
	# where the manage.py is located.
