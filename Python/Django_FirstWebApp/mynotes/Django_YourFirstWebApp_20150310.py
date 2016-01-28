## Django_YourFirstWebApp_20150310

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp

# Today, with mobile front-ends, cloud back-ends, and fully automated management infrastructure, 
# companies are able to launch across many countries at a very high speed with a strong, technology 
# and analytics-enabled central infrastructure and light local teams.

## http://work.thaslwanter.at/Stats/html/statsPreface.html
## https://code.djangoproject.com/wiki/DjangoGraphviz
## http://blog.treasuredata.com/blog/2015/04/24/python-for-aspiring-data-nerds/

########################################################################################################################
########################################################################################################################
########################################################################################################################


#### Useful resources ####

# Python WebApp Guide:
##  http://docs.python-guide.org/en/latest/scenarios/web/#django

# Django Project:
##  https://www.djangoproject.com/

# Django Packages:
#  https://www.djangopackages.com/

# Python on Heroku:
##  https://devcenter.heroku.com/categories/python

# Heroku for django
## https://devcenter.heroku.com/articles/getting-started-with-django

# Math view point guide to Python
## http://www.kevinsheppard.com/images/0/09/Python_introduction.pdf

# Pandas Introduction to Data Analysis
## http://nbviewer.ipython.org/format/slides/github/jorisvandenbossche/2015-PyDataParis/blob/master/pandas_introduction.ipynb#/6

# Python Intermediate tips
## http://book.pythontips.com/en/latest/args_and_kwargs.html

########################################################################################################################
########################################################################################################################
########################################################################################################################

#### Short Notes ####

### Creating / Checking conda envs
	
	## Creating: conda create --name Python2Env python=2.7
	## Checking: conda info --envs 
	## Activate: activate Python2Env

### Replacing root env with default env
	
	## $ conda create --name=Env_Python276_Django171 anaconda=2 python=2.7 django=1.7
	## $ conda config --set core.default_env=Env_Python276_Django171

### Installing Packages: 

	## To install package (django) to Anaconda/envs/py34:
		#> conda install -p ~/anaconda/envs/py34 django

### Installing django-extensions package for shell_plus
	
	## go to your env
	## conda create --name Env3_Python276_Django171_djangoextensions python=2.7.6 django=1.7.1
	## activate Env3_Python276_Django171_djangoextensions
	## conda install -c https://conda.anaconda.org/trentonoliphant django-extensions


### Running commands: 

	## Running scripts from the command line using  manage.py:
		#> manage.py <command> [options]

### Database setup:

	## If you want to use postgres, go to mysite/settings.py and change to:
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR, 'db.postgresql_psycopg2'),
    	}
	}

### Run server:

	## When the server’s running, visit http://127.0.0.1:8000/ with your Web browser. 
	python manage.py runserver
	python manage.py runserver 8103 ## To use a different port
	# ctrl c to break the connection.

### Visit views page:
	# Which you defined in the index view. (polls/views.py > def index(request)...)
	http://localhost:8000/polls/
	http://ecostuff-cawarnold.c9.io/polls/

### Include new tables in database:

	# write new model eg.
	class Choice(models.Model):
    	question = models.ForeignKey(Question)
    	choice_text = models.CharField(max_length=200)
    	votes = models.IntegerField(default=0)

### To include the polls app, change settings and run the makemigrations command:

	# Edit the mysite/settings.py file again, and change the INSTALLED_APPS setting to include the string 'polls'.
	python manage.py makemigrations polls

### Now, run the migrate command to create those model tables in your database:

	python manage.py migrate

### syncdb looks for apps that have not yet been set up, or changed in ways that it can understand.
	
	# This creates all the tables, initial data and indexes for any apps you have added to your project since the last time you ran syncdb. 
	# syncdb can be called as often as you like, and it will only ever create the tables that don’t exist.	
	python manage.py syncdb

### In the terminal, we can run our test:

	python manage.py test polls
	python manage.py test polls -v 2 ## where v is for verbosity, it now names the tests.


### Hop into the interactive Python shell and play around with the free API Django gives you:

	python manage.py shell

	# In the shell if you want to use indented lines, the first line has to end in a semicolon :

	try:
		stuff

### To execute a script from the python shell
	
	execfile('TOTALLYMETALCODE.py')

### Create a Question:
	from polls.models import Question, Choice
	from django.utils import timezone
	q = Question(question_text="What's new?", pub_date=timezone.now())
	q.save()

### Other methods and attributes for the Question instance
	dir(q)
	help(q)

### Change the values of an attirbute:
	q.pub_date = datetime.datetime(2015, 12, 15, 0, 0)
	q.save()

### View all Questions:
	Question.objects.all()

### View Specific Question:
	Question.objects.all()[1]
	Question.objects.all()[5:10]
	Question.objects.get(id=1) 	#These queries are similar.

### View all Choices for a specific question
	Question.objects.get(pk=1).choice_set.all()

### Creating Choices for those Questions:
	q = Question.objects.get(pk=1)
	q.choice_set.create(choice_text='Not much', votes=0)

### Retrieve the votes for a specific choice:
	q = Question.object.get(id=4)
	q.choice_set.all()[2].votes

### Retreive the choice:
	Choice.objects.get(id=1)

### Delete a Question:
	Question.objects.all()[1].delete

### Filter for a Question:
	Question.objects.filter(question_text__startswith='W')
	Question.objects.filter(question_text__icontains='h') 
			# Here the i of icontains means case in-sensitive
	Question.objects.filter(pk__in=[1,4,7])
			# Here filters exaclty for ids 1,4 or 7.

	## Delete Entries where id > 4:
		qs = Question.objects.filter(id__gte=4)
		qs.delete()

### Create a user who can login to the admin site. Run the following command:
	python manage.py createsuperuser

### Visit admin site, (first run server):
	python manage.py runserver
	# Then visit http://127.0.0.1:8000/admin/

#### Check HTTP response codes:
	Responses: 200 = OK, 302 = Found, 400 = Bad Request
	# http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

#### View contents of a directory
	import polls.views
	dir(polls.views)

#### Get directory string
	import inspect
	inspect.getsourcefile(polls.views)
		#C:\\Users\\U6030064\\Documents\\GitHub\\MyApp\\polls\\views.py

#### HTTP Status codes
	http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# A model is the single, definitive source of data about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 


# A view is a “type” of Web page in your Django application that generally serves a specific function 
# and has a specific template. 

# Django - model, template, view -> 
# model is the db, template is html, view is python connecting the model(data) with the template(html page).

### The Django test client:
	>>> from django.test.utils import setup_test_environment
	>>> setup_test_environment()
	>>> from django.test import Client
	>>> # create an instance of the client for our use
	>>> client = Client()
	>>> # get a response from '/'
	>>> response = client.get('/')
	>>> # we should expect a 404 from that address
	>>> response.status_code
	## Now begin testing


######## 
########
########

#### Dealing with git "modified: db.sqlite3" ####

	#20151016: I have seen this problem before and it cause me some trouble.
		# I am going to find the most recent commit to the branch [AddUsersModel]
		# and then try and do a git add ... > git commit ... > git push

		## Most recent commit was 657fd94d25b562336b312a93634582cb48d40f5d
		## authored on 20th Aug 2015
	# if i need to revert I can do the following:
	# git revert --no-commit 657fd94d25b562336b312a93634582cb48d40f5d
	# git commit

		## I have commited the change and tested the app: python ./manage.py runserver 8100
			# and it works fine
			# now try and push to github..
			# also seems to have gone fine.
		## Now I'm going to check the cloud9 instance, yep working fine. 
		## Ok will leave it for now. 

	#20151029: I did it again, same outcome - so I'll leave it for now.
	#20151211: It has the same "modified: db.sqlite3" part. 
	#	Thinking about the above - the reason icloud9 workd is because i didn't pull anything down to it.
	#	So its still in the same state. Obv. anyway I just commited again and local is fine.

########################################################################################################################
########################################################################################################################
########################################################################################################################

#### Full Notes ####

#### Creation of a basic poll application ####

# It’ll consist of two parts:
# A public site that lets people view polls and vote in them.
# An admin site that lets you add, change and delete polls.

# Check version of Django
# $ python -c "import django; print(django.get_version())"

# This tutorial is written for Django 1.7 and Python 3.2 or later.
# If you are still using Python 2.7, you will need to adjust the code samples slightly, as described in comments.

# Where to get help:
# If you’re having trouble going through this tutorial, please post a message to django-users or 
# drop by #django on irc.freenode.net to chat with other Django users who might be able to help.

############################################################################
############################################################################
############################################################################

#### Creating a project ####

# If this is your first time using Django, you’ll have to take care of some initial setup. 
# Namely, you’ll need to auto-generate some code that establishes a Django project – 
# a collection of settings for an instance of Django, including database configuration, 
# Django-specific options and application-specific settings.

# From the command line, cd into a directory where you’d like to store your code, then run the following command:
# $ django-admin.py startproject mysite

	# This will create a mysite directory in your current directory. If it didn’t work, see Problems running django-admin.py.
	# If you used virtualenv to install Django on Windows, you may get an ImportError when you try to run django-admin.py. 
	# This is because Windows does not run the Python interpreter from your virtual environment unless you invoke it directly. 
	# Instead, prefix all commands that use .py files with python and use the full path to the file, 
	# like so: python C:\pythonXY\Scripts\django-admin.py.

		# http://docs.python-guide.org/en/latest/dev/virtualenvs/
		# virtualenv is a tool to create isolated Python environments. 
		# virtualenv creates a folder which contains all the necessary 
		# executables to use the packages that a Python project would need.

			# Install virtualenv via pip: 
				# $ pip install virtualenv
			# Create a virtual environment for a project:
				# $ cd my_project_folder
				# $ virtualenv venv

		# virtualenv venv will create a folder in the current directory which will contain the Python executable files, 
		# and a copy of the pip library which you can use to install other packages. 
		# The name of the virtual environment (in this case, it was venv) can be anything.

			# You can also use a Python interpreter of your choice.
				# $ virtualenv -p /usr/bin/python3.2 venv

			#To begin using the virtual environment, it needs to be activated:
				# $ source venv/bin/activate


		# conda create -n python3 python=3.4 anaconda
		# now trying to get anaconda to have both python 2.7 and python 3.4
## >>>> Re - downloded anaconda after removing python27 from my path variables.

		# Ran the following to install and activate python 3.4
			# $ conda update conda
			# $ conda create -n py27 python=2.7 anaconda
			# $ activate py34
		# To deactivate the environment
			# $ deactivate

###########
## >> Created project in PyCharm Community Edition 4, using Anaconda/envs/py34
## >> Start Again:
	# $ python -c "import django; print(django.get_version())"
## >> And Nope - PyCharm is now being ridiculously slow when trying to check for django package.
###########

############## Back to working in Sublime ###########

## To install package to Anaconda/envs/py34:
	#> conda install -p ~/anaconda/envs/py34 django

## activate python 3.4 with django installed
	#> activate py34

## Create Django project
	# ~/MyFirstDjangoProject> django-admin.py startproject mysite

## Yey - created a django project!

############## Start Project files ###########

# The outer mysite/ root directory is just a container for your project. 
	# Its name doesn’t matter to Django; you can rename it to anything you like.

# manage.py: A command-line utility that lets you interact with this Django project in various ways. 
	# You can read all the details about manage.py in django-admin.py and manage.py.

# The inner mysite/ directory is the actual Python package for your project. 
	# Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

# mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. 
	# (Read more about packages in the official Python docs if you’re a Python beginner.)

# mysite/settings.py: Settings/configuration for this Django project. 
	# Django settings will tell you all about how settings work.

# mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. 
	# You can read more about URLs in URL dispatcher.

# mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. 
	# See How to deploy with WSGI for more details.


############## Database setup ###########

# Now, edit mysite/settings.py. It’s a normal Python module with module-level variables representing Django settings.

	# By default, the configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, 
	# this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. 
	# When starting your first real project, however, you may want to use a more robust database like PostgreSQL, 
	# to avoid database-switching headaches down the road.

# If you’re using SQLite, you don’t need to create anything beforehand - 
# the database file will be created automatically when it is needed.

# While you’re editing mysite/settings.py, set TIME_ZONE to your time zone

# Also, note the INSTALLED_APPS setting at the top of the file. 
	# That holds the names of all Django applications that are activated in this Django instance. 
	# Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

	# By default, INSTALLED_APPS contains the following apps, all of which come with Django:
	# django.contrib.admin – The admin site. You’ll use it in part 2 of this tutorial.
	# django.contrib.auth – An authentication system.
	# django.contrib.contenttypes – A framework for content types.
	# django.contrib.sessions – A session framework.
	# django.contrib.messages – A messaging framework.
	# django.contrib.staticfiles – A framework for managing static files.
	# These applications are included by default as a convenience for the common case.

# Some of these applications makes use of at least one database table, though, 
# so we need to create the tables in the database before we can use them. To do that, run the following command:

	#> $ python manage.py migrate

	# The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables 
	# according to the database settings in your mysite/settings.py file and the database migrations 
	# shipped with the app (we’ll cover those later). 
	# You’ll see a message for each migration it applies. 
	# If you’re interested, run the command-line client for your database and 
	# type \dt (PostgreSQL), SHOW TABLES; (MySQL), or .schema (SQLite) to display the tables Django created.


############## The development server ###########

# Let’s verify your Django project works. Change into the outer mysite directory, 
	# if you haven’t already, and run the following commands:

	#> $ python manage.py runserver
	
	# You’ll see the following output on the command line:
 
		# Performing system checks...
		# 
		# 0 errors found
		# March 12, 2015 - 15:50:53
		# Django version 1.7, using settings 'mysite.settings'
		# Starting development server at http://127.0.0.1:8000/
		# Quit the server with CONTROL-C.

# You’ve started the Django development server, a lightweight Web server written purely in Python. 
# We’ve included this with Django so you can develop things rapidly, 
# without having to deal with configuring a production server – such as Apache – until you’re ready for production.

# Now’s a good time to note: don’t use this server in anything resembling a production environment. 
# It’s intended only for use while developing. (We’re in the business of making Web frameworks, not Web servers.)

# Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser. 
# You’ll see a “Welcome to Django” page, in pleasant, light-blue pastel. It worked!


############################################################################
############################################################################
############################################################################

#### Creating models ####

# Now that your environment – a “project” – is set up, you’re set to start doing work.

# Each application you write in Django consists of a Python package that follows a certain convention. 
# Django comes with a utility that automatically generates the basic directory structure of an app, 
# so you can focus on writing code rather than creating directories.


## Projects vs. apps

# What’s the difference between a project and an app? 
# An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. 
# A project is a collection of configuration and apps for a particular Web site. 
# A project can contain multiple apps. 
# An app can be in multiple projects.

# Your apps can live anywhere on your Python path. 
# In this tutorial, we’ll create our poll app right next to your manage.py file 
# so that it can be imported as its own top-level module, rather than a submodule of mysite.

# To create your app, make sure you’re in the same directory as manage.py and type this command:

	#> $ python manage.py startapp polls

# That’ll create a directory polls, which is laid out like this:

polls/
    __init__.py
    admin.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py


# This directory structure will house the poll application.
# The first step in writing a database Web app in Django is to define your models – 
# essentially, your database layout, with additional metadata.

######################################################
######################################################

### Philosophy

# A model is the single, definitive source of data about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 
# Django follows the DRY Principle. 
# The goal is to define your data model in one place and automatically derive things from it.

# This includes the migrations - 
# unlike in Ruby On Rails, for example, 
# migrations are entirely derived from your models file,
# and are essentially just a history that Django can roll through to update your database schema to match your current models.
# In our simple poll app, we’ll create two models: Question and Choice. 
# A Question has a question and a publication date. 
# A Choice has two fields: the text of the choice and a vote tally. 
# Each Choice is associated with a Question.

######################################################
######################################################

# These concepts are represented by simple Python classes. 
# Edit the polls/models.py file so it looks like this:

polls/models.py
from django.db import models

# A Question has a question and a publication date. 
class Question(models.Model):
    question_text = models.CharField(max_length=200)     
    pub_date = models.DateTimeField('date published')

# A Choice has two fields: the text of the choice and a vote tally.
# Each Choice is associated with a Question.
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# The code is straightforward. Each model is represented by a class that subclasses django.db.models.Model. 
# Each model has a number of class variables, each of which represents a database field in the model.

# Each field is represented by an instance of a Field class – 
# e.g., CharField for character fields and DateTimeField for datetimes. 
# This tells Django what type of data each field holds.

# The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. 
# You’ll use this value in your Python code, and your database will use it as the column name.

# You can use an optional first positional argument to a Field to designate a human-readable name. 
# That’s used in a couple of introspective parts of Django, and it doubles as documentation. 
# If this field isn’t provided, Django will use the machine-readable name. 
# In this example, we’ve only defined a human-readable name for Question.pub_date. 
# For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.

	# Docs for finding Field Arguments - https://docs.djangoproject.com/en/1.7/ref/models/fields/#charfield


# Some Field classes have required arguments. 
# CharField, for example, requires that you give it a max_length. 
# That’s used not only in the database schema, but in validation, as we’ll soon see.

# A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

# Finally, note a relationship is defined, using ForeignKey. 
	# ForeignKey is a many-to-one relationship. Many (Choice)s to One (Question)
# That tells Django each Choice is related to a single Question. 
# Django supports all the common database relationships: many-to-one, many-to-many and one-to-one.

	# A database index is automatically created on the ForeignKey
	# Behind the scenes, Django appends "_id" to the field name to create its database column name
	# In the above example, the database table for the Choice model will have a question_id column.


############################################################################
############################################################################
############################################################################


#### Activating models ####

# That small bit of model code gives Django a lot of information. With it, Django is able to:

# Create a database schema (CREATE TABLE statements) for this app.
# Create a Python database-access API for accessing Question and Choice objects.
# But first we need to tell our project that the polls app is installed.

# Philosophy
# Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, 
# because they don’t have to be tied to a given Django installation.

# Edit the mysite/settings.py file again, 
# and change the INSTALLED_APPS setting to include the string 'polls'. So it’ll look like this:

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

# Now Django knows to include the polls app. Let’s run another command:

	#> $ python manage.py makemigrations polls

# You should see something similar to the following:

Migrations for 'polls':
  0001_initial.py:
    - Create model Question
    - Create model Choice
    - Add field question to choice

# By running makemigrations, you’re telling Django that you’ve made some changes to your models 
# (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

# Migrations are how Django stores changes to your models (and thus your database schema) - 
# they’re just files on disk. 
# You can read the migration for your new model if you like; 
# it’s the file polls/migrations/0001_initial.py. 
# Don’t worry, you’re not expected to read them every time Django makes one, 
# but they’re designed to be human-editable in case you want to manually tweak how Django changes things.

# There’s a command that will run the migrations for you and manage your database schema automatically - 
# that’s called migrate, and we’ll come to it in a moment - 
# but first, let’s see what SQL that migration would run. 
# The sqlmigrate command takes migration names and returns their SQL:

	#> $ python manage.py sqlmigrate polls 0001

# You should see something similar to the following (we’ve reformatted it for readability):

BEGIN;
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;


# Note the following:

# The exact output will vary depending on the database you are using. The example above is generated for PostgreSQL.
# Table names are automatically generated by combining the name of the app (polls) 
# and the lowercase name of the model – question and choice. (You can override this behavior.)
# Primary keys (IDs) are added automatically. (You can override this, too.)
# By convention, Django appends "_id" to the foreign key field name. (Yes, you can override this, as well.)
# The foreign key relationship is made explicit by a FOREIGN KEY constraint. 
# Don’t worry about the DEFERRABLE parts; 
# that’s just telling PostgreSQL to not enforce the foreign key until the end of the transaction.

# It’s tailored to the database you’re using, so database-specific field types such as 
# auto_increment (MySQL), serial (PostgreSQL), or integer primary key autoincrement (SQLite) 
# are handled for you automatically. Same goes for quoting of field names – e.g., using double quotes or single quotes.

# The sqlmigrate command doesn’t actually run the migration on your database - 
# it just prints it to the screen so that you can see what SQL Django thinks is required. 
# It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

# If you’re interested, you can also run 

	#> $ python manage.py check

System check identifier no issues (0 silences).

#; this checks for any problems in your project without making migrations or touching the database.

# Now, run migrate again to create those model tables in your database:

	#> $ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, contenttypes, polls, auth, sessions
Running migrations:
  Applying <migration name>... OK


# The migrate command takes all the migrations that haven’t been applied 
# (Django tracks which ones are applied using a special table in your database called django_migrations) 
# and runs them against your database - 
# essentially, synchronizing the changes you made to your models with the schema in the database.

# Migrations are very powerful and let you change your models over time, as you develop your project, 
# without the need to delete your database or tables and make new ones - 
# it specializes in upgrading your database live, without losing data. 
# We’ll cover them in more depth in a later part of the tutorial, but for now, 
# remember the three-step guide to making model changes:

	# Change your models (in models.py).
	# Run python manage.py makemigrations to create migrations for those changes
	# Run python manage.py migrate to apply those changes to the database.
	# The reason there’s separate commands to make and apply migrations is because 
	# you’ll commit migrations to your version control system and ship them with your app; 
	# they not only make your development easier, they’re also useable by other developers and in production.

# Read the django-admin.py documentation for full information on what the manage.py utility can do.


############################################################################
############################################################################
############################################################################


#### Playing with the API ####

# Now, let’s hop into the interactive Python shell and play around with the free API Django gives you. 
# To invoke the Python shell, use this command:

	#> $ python manage.py shell

# We’re using this instead of simply typing “python”, because manage.py sets the DJANGO_SETTINGS_MODULE environment variable, 
# which gives Django the Python import path to your mysite/settings.py file.


	# Bypassing manage.py
	
	# If you’d rather not use manage.py, no problem. 
	# Just set the DJANGO_SETTINGS_MODULE environment variable to mysite.settings, 
	# start a plain Python shell, and set up Django:
	
	>>> import django
	>>> django.setup()
	
	# If this raises an AttributeError, you’re probably using a version of Django that doesn’t match this tutorial version. 
	# You’ll want to either switch to the older tutorial or the newer Django version.
	
	# You must run python from the same directory manage.py is in, or ensure that directory is on the Python path, 
	# so that import mysite works.
	
	# For more information on all of this, see the django-admin.py documentation.
	
		## Making Queries
		# https://docs.djangoproject.com/en/1.7/topics/db/queries/

		# Once you’ve created your data models, Django automatically gives you a database-abstraction API 
		# that lets you create, retrieve, update and delete objects.  
		# Refer to the data model reference for full details of all the various model lookup options.


# Once you’re in the shell, explore the database API:

>>> from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
[]

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer objects.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
[<Question: Question object>]

# Wait a minute. <Question: Question object> is, utterly, an unhelpful representation of this object. 
# Let’s fix that by editing the Question model (in the polls/models.py file) and 
# adding a __str__() method to both Question and Choice:

polls/models.py
	from django.db import models

	class Question(models.Model):
	    # ...
	    def __str__(self):              # __unicode__ on Python 2
	        return self.question_text

	class Choice(models.Model):
	    # ...
	    def __str__(self):              # __unicode__ on Python 2
	        return self.choice_text


# It’s important to add __str__() methods to your models, not only for your own convenience 
# when dealing with the interactive prompt, but also because objects’ representations are used 
# throughout Django’s automatically-generated admin.

	# Unicode
	__str__ or __unicode__?
	# On Python 3, it’s easy, just use __str__().
	# On Python 2, you should define __unicode__() methods returning unicode values instead. 
	# Django models have a default __str__() method that calls __unicode__() and converts the result to a UTF-8 bytestring. 
	# This means that unicode(p) will return a Unicode string, and str(p) will return a bytestring, 
	# with characters encoded as UTF-8. 
	# Python does the opposite: 
	# object has a __unicode__ method that calls __str__ and interprets the result as an ASCII bytestring. 
	# This difference can create confusion. If all of this is gibberish to you, just use Python 3.


# Note these are normal Python methods. Let’s add a custom method, just for demonstration:

polls/models.py
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Note the addition of import datetime and from django.utils import timezone, 
# to reference Python’s standard datetime module and 
# Django’s time-zone-related utilities in django.utils.timezone, respectively. 
# If you aren’t familiar with time zone handling in Python, you can learn more in the time zone support docs.

# Save these changes and start a new Python interactive shell by running python manage.py shell again:

>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
# [<Question: What's up?>]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
# [<Question: What's up?>]
>>> Question.objects.filter(question_text__startswith='What')
# [<Question: What's up?>]

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
# <Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
# <Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. 
# The create call constructs a new Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. 
# Django creates a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
[]

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
# <Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

# For more information on model relations, see Accessing related objects. 
# For more on how to use double underscores to perform field lookups via the API, see Field lookups. 
# For full details on the database API, see our Database API reference.

# When you’re comfortable with the API, read part 2 of this tutorial to get Django’s automatic admin working.


############################################################################
############################################################################
############################################################################

## Writing your first Django app, part 2

## We’re continuing the Web-poll application and will focus on Django’s automatically-generated admin site.

# Philosophy
# Generating admin sites for your staff or clients to add, change and delete content 
# is tedious work that doesn’t require much creativity. 
# For that reason, Django entirely automates creation of admin interfaces for models.

# Django was written in a newsroom environment, 
# with a very clear separation between “content publishers” and the “public” site. 
# Site managers use the system to add news stories, events, sports scores, etc.,
# and that content is displayed on the public site. 
# Django solves the problem of creating a unified interface for site administrators to edit content.

# The admin isn’t intended to be used by site visitors. It’s for site managers.


#### Creating an admin user ####

# First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser

# Enter your desired username and press enter.

# Username: christian
# You will then be prompted for your desired email address:

# Email address: christian.w.arnold@gmail.com
# The final step is to enter your password. 
# You will be asked to enter your password twice, the second time as a confirmation of the first.

# Password: H14ts...
# Password (again): H14ts...
# Superuser created successfully.


#### Start the development server ####

# The Django admin site is activated by default. Let’s start the development server and explore it.

# Recall from Tutorial 1 that you start the development server like so:

$ python manage.py runserver

# Now, open a Web browser and go to “/admin/” on your local domain – 
# e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:


#### Enter the admin site ####

# Now, try logging in with the superuser account you created in the previous step. You should see the Django admin index page.

# You should see a few types of editable content: groups and users. 
# They are provided by django.contrib.auth, the authentication framework shipped by Django.

#### Make the poll app modifiable in the admin ####

# But where’s our poll app? It’s not displayed on the admin index page.

# Just one thing to do: we need to tell the admin that Question objects have an admin interface. 
# To do this, open the polls/admin.py file, and edit it to look like this:

# polls/admin.py
from django.contrib import admin
from polls.models import Question

admin.site.register(Question)

#### Explore the free admin functionality ####

# Now that we’ve registered Question, Django knows that it should be displayed on the admin index page:

## There is now a table for our polls app.

# Click “Questions”. Now you’re at the “change list” page for questions. 
# This page displays all the question in the database and lets you choose one to change it. 
# There’s the “What’s up?” question we created in the first tutorial:
# Click the “What’s up?” question to edit it:


# Things to note here:
# The form is automatically generated from the Question model.
# The different model field types (DateTimeField, CharField) correspond to the appropriate HTML input widget. 
# Each type of field knows how to display itself in the Django admin.
# Each DateTimeField gets free JavaScript shortcuts. 
# Dates get a “Today” shortcut and calendar popup, 
# and times get a “Now” shortcut and a convenient popup that lists commonly entered times.
# The bottom part of the page gives you a couple of options:

# Save – Saves changes and returns to the change-list page for this type of object.
# Save and continue editing – Saves changes and reloads the admin page for this object.
# Save and add another – Saves changes and loads a new, blank form for this type of object.
# Delete – Displays a delete confirmation page.
# If the value of “Date published” doesn’t match the time when you created the question in Tutorial 1, 
# it probably means you forgot to set the correct value for the TIME_ZONE setting. 
# Change it, reload the page and check that the correct value appears.

# Change the “Date published” by clicking the “Today” and “Now” shortcuts. 
# Then click “Save and continue editing.” Then click “History” in the upper right. 
# You’ll see a page listing all changes made to this object via the Django admin, 
# with the timestamp and username of the person who made the change:


#### Customize the admin form ####

# Take a few minutes to marvel at all the code you didn’t have to write. 
# By registering the Question model with admin.site.register(Question), 
# Django was able to construct a default form representation. 
# Often, you’ll want to customize how the admin form looks and works. 
# You’ll do this by telling Django the options you want when you register the object.

# Let’s see how this works by re-ordering the fields on the edit form. 
# Replace the admin.site.register(Question) line with:

# polls/admin.py
from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

# You’ll follow this pattern – create a model admin object, 
# then pass it as the second argument to admin.site.register() – 
# any time you need to change the admin options for an object.

# This particular change above makes the “Publication date” come before the “Question” field:
# This isn’t impressive with only two fields, but for admin forms with dozens of fields, 
# choosing an intuitive order is an important usability detail.

# And speaking of forms with dozens of fields, you might want to split the form up into fieldsets:

#polls/admin.py
from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

# The first element of each tuple in fieldsets is the title of the fieldset. 


# You can assign arbitrary HTML classes to each fieldset. 
# Django provides a "collapse" class that displays a particular fieldset initially collapsed. 
# This is useful when you have a long form that contains a number of fields that aren’t commonly used:

#polls/admin.py
from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Question, QuestionAdmin)


####################################################
####################################################
####################################################


#### Adding related objects ####

# OK, we have our Question admin page. 
# But a Question has multiple Choices, and the admin page doesn’t display choices.

# Yet.

# There are two ways to solve this problem. 
# The first is to register Choice with the admin just as we did with Question. That’s easy:

# polls/admin.py
from django.contrib import admin
from polls.models import Choice, Question
# ...
admin.site.register(Choice)

# Now “Choices” is an available option in the Django admin. 

# In that form, the “Question” field is a select box containing every question in the database. 
# Django knows that a ForeignKey should be represented in the admin as a <select> box. 
# In our case, only one question exists at this point.

# Also note the “Add Another” link next to “Question.” 
# Every object with a ForeignKey relationship to another gets this for free. 
# When you click “Add Another,” you’ll get a popup window with the “Add question” form. 
# If you add a question in that window and click “Save,” 
# Django will save the question to the database and 
# dynamically add it as the selected choice on the “Add choice” form you’re looking at.


# But, really, this is an inefficient way of adding Choice objects to the system. 
# It’d be better if you could add a bunch of Choices directly when you create the Question object. 
# Let’s make that happen.

# Remove the register() call for the Choice model. Then, edit the Question registration code to read:

# polls/admin.py
from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
# Load the “Add question” page to see how that looks:

# It works like this: There are three slots for related Choices – 
# as specified by extra – and each time you come back to the “Change” page for an already-created object, 
# you get another three extra slots.

# At the end of the three current slots you will find an “Add another Choice” link. 
# If you click on it, a new slot will be added.
# If you want to remove the added slot, you can click on the X to the top right of the added slot. 
# Note that you can’t remove the original three slots. This image shows an added slot:

# One small problem, though. 
# It takes a lot of screen space to display all the fields for entering related Choice objects.
# For that reason, Django offers a tabular way of displaying inline related objects; 
# you just need to change the ChoiceInline declaration to read

#polls/admin.py
class ChoiceInline(admin.TabularInline):
    #...

# With that TabularInline (instead of StackedInline), the related objects are displayed in a more compact, table-based format:

# Note that there is an extra “Delete?” column that allows removing rows added using the 
# “Add Another Choice” button and rows that have already been saved.


#### Customise the admin change list ####

# Now that the Question admin page is looking good, let’s make some tweaks to the “change list” page – 
# the one that displays all the questions in the system.

# By default, Django displays the str() of each object. 
# But sometimes it’d be more helpful if we could display individual fields. 
# To do that, use the list_display admin option, which is a tuple of field names to display, 
# as columns, on the change list page for the object:

# polls/admin.py
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')

# Just for good measure, let’s also include the was_published_recently custom method from Tutorial 1:

# polls/admin.py
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')


# You can click on the column headers to sort by those values – 
# except in the case of the was_published_recently header, 
# because sorting by the output of an arbitrary method is not supported. 
# Also note that the column header for was_published_recently is, by default, 
# the name of the method (with underscores replaced with spaces), 
# and that each line contains the string representation of the output.

# You can improve that by giving that method (in polls/models.py) a few attributes, as follows:

polls/models.py
class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# For more information on these method properties, see list_display.

# Edit your polls/admin.py file again and add an improvement to the Question change list page: 
# filters using the list_filter. Add the following line to QuestionAdmin:

# That adds a “Filter” sidebar that lets people filter the change list by the pub_date field:

# The type of filter displayed depends on the type of field you’re filtering on. 
# Because pub_date is a DateTimeField, Django knows to give appropriate filter options: 
# “Any date,” “Today,” “Past 7 days,” “This month,” “This year.”

#This is shaping up well. Let’s add some search capability:

search_fields = ['question_text']

# That adds a search box at the top of the change list. When somebody enters search terms, 
# Django will search the question_text field. 
# You can use as many fields as you’d like – 
# although because it uses a LIKE query behind the scenes, limiting the number of search 
# fields to a reasonable number will make it easier for your database to do the search.

# Now’s also a good time to note that change lists give you free pagination. 
# The default is to display 100 items per page. 
# Change list pagination, search boxes, filters, date-hierarchies, 
# and column-header-ordering all work together like you think they should.

####################################################
####################################################
####################################################

#### Customize the admin look and feel ####

# Clearly, having “Django administration” at the top of each admin page is ridiculous. 
# It’s just placeholder text.

# That’s easy to change, though, using Django’s template system. 
# The Django admin is powered by Django itself, and its interfaces use Django’s own template system.

#### Customizing your project’s templates ####

# Create a templates directory in your project directory. 
# Templates can live anywhere on your filesystem that Django can access. 
# (Django runs as whatever user your server runs.) 
# However, keeping your templates within the project is a good convention to follow.

# Open your settings file (mysite/settings.py, remember) and add a TEMPLATE_DIRS setting:

# mysite/settings.py
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# TEMPLATE_DIRS is an iterable of filesystem directories to check when loading Django templates; it’s a search path.

# Now create a directory called admin inside templates, 
# and copy the template admin/base_site.html from within the default Django admin template directory 
# in the source code of Django itself (django/contrib/admin/templates) into that directory.

# Where are the Django source files?

# If you have difficulty finding where the Django source files are located on your system, run the following command:
	# $ python -c "
	#	import sys
	#	sys.path = sys.path[1:]
	#	import django
	#	print(django.__path__)"


# Then, just edit the file and replace {{ site_header|default:_('Django administration') }} (including the curly braces) 
# with your own site’s name as you see fit. You should end up with a section of code like:

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
{% endblock %}

# We use this approach to teach you how to override templates. 
# In an actual project, you would probably use the django.contrib.admin.AdminSite.site_header 
# attribute to more easily make this particular customization.

# This template file contains lots of text like {% block branding %} and {{ title }}. 
# The {% and {{ tags are part of Django’s template language. 
# When Django renders admin/base_site.html, this template language will be evaluated to produce the final HTML page. 
# Don’t worry if you can’t make any sense of the template right now – 
# we’ll delve into Django’s templating language in Tutorial 3.

# Note that any of Django’s default admin templates can be overridden. 
# To override a template, just do the same thing you did with base_site.html – 
# copy it from the default directory into your custom directory, and make changes.


#### Customizing your application’s templates ####

# Astute readers will ask: But if TEMPLATE_DIRS was empty by default, 
# how was Django finding the default admin templates? The answer is that, 
# by default, Django automatically looks for a templates/ subdirectory within each application package, 
# for use as a fallback (don’t forget that django.contrib.admin is an application).

# Our poll application is not very complex and doesn’t need custom admin templates. 
# But if it grew more sophisticated and required modification of Django’s standard admin templates 
# for some of its functionality, it would be more sensible to modify the application’s templates, 
# rather than those in the project. 
# That way, you could include the polls application in any new project and be assured that 
# it would find the custom templates it needed.

# See the template loader documentation for more information about how Django finds its templates.


#### Customize the admin index page ####

# On a similar note, you might want to customize the look and feel of the Django admin index page.

# By default, it displays all the apps in INSTALLED_APPS that have been registered with the admin application, 
# in alphabetical order. You may want to make significant changes to the layout. 
# After all, the index is probably the most important page of the admin, and it should be easy to use.

# The template to customize is admin/index.html. 
# (Do the same as with admin/base_site.html in the previous section – 
# copy it from the default directory to your custom template directory.) 
# Edit the file, and you’ll see it uses a template variable called app_list. That variable contains every installed Django app. Instead of using that, you can hard-code links to object-specific admin pages in whatever way you think is best. Again, don’t worry if you can’t understand the template language – we’ll cover that in more detail in Tutorial 3.

# When you’re comfortable with the admin site, read part 3 of this tutorial to start working on public poll views.


############################################################################
############################################################################
############################################################################


# Writing your first Django app, part 3

# This tutorial begins where Tutorial 2 left off. 

# We’re continuing the Web-poll application and will focus on creating the public interface – “views.”

## Philosophy ##

# A view is a “type” of Web page in your Django application that generally serves a specific function 
# and has a specific template. 

# For example, in a blog application, you might have the following views:

# Blog homepage – displays the latest few entries.
# Entry “detail” page – permalink page for a single entry.
# Year-based archive page – displays all months with entries in the given year.
# Month-based archive page – displays all days with entries in the given month.
# Day-based archive page – displays all entries in the given day.
# Comment action – handles posting comments to a given entry.

# In our poll application, we’ll have the following four views:
# Question “index” page – displays the latest few questions.
# Question “detail” page – displays a question text, with no results but with a form to vote.
# Question “results” page – displays results for a particular question.
# Vote action – handles voting for a particular choice in a particular question.

# In Django, web pages and other content are delivered by views. 
# Each view is represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that’s requested 
# (to be precise, the part of the URL after the domain name).


# Now in your time on the web you may have come across such beauties as 
# “ME2/Sites/dirmod.asp?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B”. 
# You will be pleased to know that Django allows us much more elegant URL patterns than that.

# A URL pattern is simply the general form of a URL - for example: /newsarchive/<year>/<month>/.
# To get from a URL to a view, Django uses what are known as ‘URLconfs’. 
# A URLconf maps URL patterns (described as regular expressions) to views.

# This tutorial provides basic instruction in the use of URLconfs, 
# and you can refer to django.core.urlresolvers for more information.

#### Write your first view ####

# Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

#polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

####################################################
####################################################
####################################################

# To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

polls/
    __init__.py
    admin.py
    models.py
    tests.py
    urls.py
    views.py

# In the polls/urls.py file include the following code:

# polls/urls.py
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

# The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py insert an include(), leaving you with:

#mysite/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),


	## Doesn’t match what you see?

	## If you’re seeing admin.autodiscover() before the definition of urlpatterns, 
	## you’re probably using a version of Django that doesn’t match this tutorial version. 
	## You’ll want to either switch to the older tutorial or the newer Django version.

# You have now wired an index view into the URLconf. 
# Go to http://localhost:8000/polls/ in your browser, 
# and you should see the text “Hello, world. You’re at the polls index.”, 
# which you defined in the index view.

# The url() function is passed four arguments, 
# two required: regex and view, 
# and 
# two optional: kwargs, and name. 

####################################################
####################################################
####################################################

# At this point, it’s worth reviewing what these arguments are for.

### url() argument: regex ###

# The term “regex” is a commonly used short form meaning “regular expression”, 
# which is a syntax for matching patterns in strings, or in this case, url patterns. 
# Django starts at the first regular expression and makes its way down the list, 
# comparing the requested URL against each regular expression until it finds one that matches.

# Note that these regular expressions do not search GET and POST parameters, or the domain name. 
# For example, in a request to http://www.example.com/myapp/, the URLconf will look for myapp/. 
# In a request to http://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

# If you need help with regular expressions, see Wikipedia’s entry and the documentation of the re module. 
# (https://docs.python.org/3/library/re.html#module-re)
# Also, the O’Reilly book “Mastering Regular Expressions” by Jeffrey Friedl is fantastic. 
# In practice, however, you don’t need to be an expert on regular expressions, 
# as you really only need to know how to capture simple patterns. 
# In fact, complex regexes can have poor lookup performance, 
# so you probably shouldn’t rely on the full power of regexes.

# Finally, a performance note: 
# these regular expressions are compiled the first time the URLconf module is loaded. 
# They’re super fast (as long as the lookups aren’t too complex as noted above).


### url() argument: view ###

# When Django finds a regular expression match, Django calls the specified view function, 
# with an HttpRequest object as the first argument and any “captured” values 
# from the regular expression as other arguments. 
# If the regex uses simple captures, values are passed as positional arguments; 
# if it uses named captures, values are passed as keyword arguments. 
# We’ll give an example of this in a bit.


### url() argument: kwargs ###

# Arbitrary keyword arguments can be passed in a dictionary to the target view. 
# We aren’t going to use this feature of Django in the tutorial.


### url() argument: name ###

# Naming your URL lets you refer to it unambiguously from elsewhere in Django especially templates. 
# This powerful feature allows you to make global changes to the url patterns of your project while 
# only touching a single file.

####################################################
####################################################
####################################################


#### Writing more views ####

# Now let’s add a few more views to polls/views.py. 
# These views are slightly different, because they take an argument:

# polls/views.py
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Wire these new views into the polls.urls module by adding the following url() calls:

# Take a look in your browser, at “/polls/34/”. 
# It’ll run the detail() method and display whatever ID you provide in the URL. 
# Try “/polls/34/results/” and “/polls/34/vote/” too – these will display the placeholder results and voting pages.

# If you go to:			http://127.0.0.1:8000/polls/34/vote/ 
# you will see: 		You're voting on question 34.

# When somebody requests a page from your Web site – say, “/polls/34/”, 
# Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. 
# It finds the variable named urlpatterns and traverses the regular expressions in order. 
# The include() functions we are using simply reference other URLconfs. 
# Note that the regular expressions for the include() functions 
# don’t have a $ (end-of-string match character) 
# but rather a trailing slash. Whenever Django encounters include(), 
# it chops off whatever part of the URL matched up to that point and 
# sends the remaining string to the included URLconf for further processing.


# The idea behind include() is to make it easy to plug-and-play URLs. 
# Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, 
# or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

# Here’s what happens if a user goes to “/polls/34/” in this system:
# Django will find the match at '^polls/'
# Then, Django will strip off the matching text ("polls/") 
# and send the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing 
# which matches r'^(?P<question_id>\d+)/$' resulting in a call to the detail() view like so:

detail(request=<HttpRequest object>, question_id='34')

# The question_id='34' part comes from (?P<question_id>\d+). 
# Using parentheses around a pattern “captures” the text matched by that pattern 
# and sends it as an argument to the view function; 
# ?P<question_id> defines the name that will be used to identify the matched pattern; 
# and \d+ is a regular expression to match a sequence of digits (i.e., a number).

# Because the URL patterns are regular expressions, there really is no limit on what you can do with them. 
# And there’s no need to add URL cruft such as .html – unless you want to, 
# in which case you can do something like this:

(r'^polls/latest\.html$', 'polls.views.index'),

# But, don’t do that. It’s silly.

####################################################
####################################################
####################################################

#### Write views that actually do something ####

# Each view is responsible for doing one of two things: 
# returning an HttpResponse object containing the content for the requested page, 
# or raising an exception such as Http404. The rest is up to you.

# Your view can read records from a database, or not. 
# It can use a template system such as Django’s – or a third-party Python template system – or not. 
# It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, 
# using whatever Python libraries you want.

# All Django wants is that HttpResponse. Or an exception.

# Because it’s convenient, let’s use Django’s own database API, which we covered in Tutorial 1. 
# Here’s one stab at a new index() view, which displays the latest 5 poll questions in the system, 
# separated by commas, according to publication date:

#polls/views.py
from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged

# There’s a problem here, though: the page’s design is hard-coded in the view. 
# If you want to change the way the page looks, you’ll have to edit this Python code. 
# So let’s use Django’s template system to separate the design from Python 
# by creating a template that the view can use.

# First, create a directory called templates in your polls directory. 
# Django will look for templates in there.

# Django’s TEMPLATE_LOADERS setting contains a list of callables that 
# know how to import templates from various sources. 
# One of the defaults is django.template.loaders.app_directories.Loader 
# which looks for a “templates” subdirectory in each of the INSTALLED_APPS - 
# this is how Django knows to find the polls templates even though we didn’t modify TEMPLATE_DIRS,
# as we did in Tutorial 2.


	# Organizing templates

	# We could have all our templates together, in one big templates directory, 
	# and it would work perfectly well. However, this template belongs to the polls application, 
	# so unlike the admin template we created in the previous tutorial, 
	# we’ll put this one in the application’s template directory (mysite/polls/templates) 
	# rather than the project’s (mysite/templates). 
	# We’ll discuss in more detail in the reusable apps tutorial why we do this.


# Within the templates directory you have just created, create another directory called polls, 
# and within that create a file called index.html. 
# In other words, your template should be at polls/templates/polls/index.html. 
# Because of how the app_directories template loader works as described above, 
# you can refer to this template within Django simply as polls/index.html.


	# Template namespacing

	# Now we might be able to get away with putting our templates directly in polls/templates 
	# (rather than creating another polls subdirectory), but it would actually be a bad idea. 
	# Django will choose the first template it finds whose name matches, 
	# and if you had a template with the same name in a different application, 
	# Django would be unable to distinguish between them. 
	# We need to be able to point Django at the right one, 
	# and the easiest way to ensure this is by namespacing them. 
	# That is, by putting those templates inside another directory named for the application itself.

# Put the following code in that template:

# polls/templates/polls/index.html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}


# Now let’s update our index view in polls/views.py to use the template:

# polls/views.py
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


# That code loads the template called polls/index.html and passes it a context. 
# The context is a dictionary mapping template variable names to Python objects.

# Load the page by pointing your browser at “/polls/”, 
# and you should see a bulleted-list containing the “What’s up” question from Tutorial 1. 
# The link points to the question’s detail page.

#### A shortcut: render() ####

# It’s a very common idiom to load a template, 
# fill a context and return an HttpResponse object with the result of the rendered template. 
# Django provides a shortcut. Here’s the full index() view, rewritten:

polls/views.py
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Note that once we’ve done this in all these views, 
# we no longer need to import loader, RequestContext and HttpResponse 
# (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

# The render() function takes the request object as its first argument, 
# a template name as its second argument 
# and a dictionary as its optional third argument. 
# It returns an HttpResponse object of the given template rendered with the given context.


####################################################
####################################################
####################################################


#### Raising a 404 error ####

# Now, let’s tackle the question detail view – 
# the page that displays the question text for a given poll. Here’s the view:

#polls/views.py
from django.http import Http404
from django.shortcuts import render

from polls.models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# The new concept here: 
# The view raises the Http404 exception if a question with the requested ID doesn’t exist.

# We’ll discuss what you could put in that polls/detail.html template a bit later, 
# but if you’d like to quickly get the above example working, a file containing just:

#polls/templates/polls/detail.html
{{ question }}

#will get you started for now.


### A shortcut: get_object_or_404() ####

# https://docs.djangoproject.com/en/1.7/intro/tutorial03/

# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. 
# Django provides a shortcut. Here’s the detail() view, rewritten:

# polls/views.py
from django.shortcuts import get_object_or_404, render

from polls.models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# The get_object_or_404() function takes a Django model as its first argument and an arbitrary 
# number of keyword arguments, which it passes to the get() function of the model’s manager. 
# It raises Http404 if the object doesn’t exist.

	# Philosophy

	# Why do we use a helper function get_object_or_404() instead of automatically catching 
	# the ObjectDoesNotExist exceptions at a higher level, 
	# or having the model API raise Http404 instead of ObjectDoesNotExist?

	# Because that would couple the model layer to the view layer. 
	# One of the foremost design goals of Django is to maintain loose coupling. 
	# Some controlled coupling is introduced in the django.shortcuts module.

# There’s also a get_list_or_404() function, which works just as get_object_or_404() – 
# except using filter() instead of get(). It raises Http404 if the list is empty.


####################################################
####################################################
####################################################


#### Use the template system ####

# Back to the detail() view for our poll application. 
# Given the context variable question, here’s what the polls/detail.html template might look like:

#polls/templates/polls/detail.html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>

# The template system uses dot-lookup syntax to access variable attributes. 
# In the example of {{ question.question_text }}, 
# first Django does a dictionary lookup on the object question. 
# Failing that, it tries an attribute lookup – which works, in this case. 
# If attribute lookup had failed, it would’ve tried a list-index lookup.

# Method-calling happens in the {% for %} loop: question.choice_set.all 
# is interpreted as the Python code question.choice_set.all(), 
# which returns an iterable of Choice objects and is suitable for use in the {% for %} tag.

# <h1>{{ question.question_text }}</h1>
#~=
# Question.objects.all()[0].question_text
#=
#"What's up?"

# {% for choice in question.choice_set.all %}
#~=
# Question.objects.get(pk=1).choice_set.all()
#=
# [<Choice: Not Much>, <Choice: The sky>]


#See the template guide for more about templates.
	# https://docs.djangoproject.com/en/1.7/topics/templates/
	# Django’s template language is designed to strike a balance between power and ease. 
	# It’s designed to feel comfortable to those used to working with HTML
	# A template is simply a text file. It can generate any text-based format (HTML, XML, CSV, etc.).
	# A template contains variables, which get replaced with values when the template is evaluated, 
	# and tags, which control the logic of the template.


####################################################
####################################################
####################################################


#### Removing hardcoded URLs in Tempates ####

# Remember, when we wrote the link to a question in the polls/index.html template, 
# the link was partially hardcoded like this:

<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>

# The problem with this hardcoded, tightly-coupled approach is that 
# it becomes challenging to change URLs on projects with a lot of templates. 
# However, since you defined the name argument in the url() functions in the polls.urls module, 
# you can remove a reliance on specific URL paths defined in your url configurations by using 
# the {% url %} template tag:

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

# The way this works is by looking up the URL definition as specified in the polls.urls module. 
# You can see exactly where the URL name of ‘detail’ is defined below:

...
# the 'name' value as called by the {% url %} template tag
url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
...

# If you want to change the URL of the polls detail view to something else, 
# perhaps to something like polls/specifics/12/ instead of doing it in the template 
# (or templates) you would change it in polls/urls.py:

...
# added the word 'specifics'
url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
...


####################################################
####################################################
####################################################


#### Namespacing URL names ####

# The tutorial project has just one app, polls. 
# In real Django projects, there might be five, ten, twenty apps or more. 
# How does Django differentiate the URL names between them? 
# For example, the polls app has a detail view, 
# and so might an app on the same project that is for a blog. 
# How does one make it so that Django knows which app view to create for 
# a url when using the {% url %} template tag?

# The answer is to add namespaces to your root URLconf. 
# In the mysite/urls.py file, go ahead and change it to include namespacing:

# mysite/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)

#Now change your polls/index.html template from:

#polls/templates/polls/index.html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>


#to point at the namespaced detail view:

#polls/templates/polls/index.html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

# When you’re comfortable with writing views, 
# read part 4 of this tutorial to learn about simple form processing and generic views.


############################################################################
############################################################################
############################################################################


#### Writing your first Django app, part 4 ####

# This tutorial begins where Tutorial 3 left off. 
# We’re continuing the Web-poll application and will focus on simple form processing and cutting down our code.

####################################################
####################################################
####################################################

#### Write a simple form ####

# Let’s update our poll detail template (“polls/detail.html”) from the last tutorial, 
# so that the template contains an HTML <form> element:

# polls/templates/polls/detail.html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

# A quick rundown:

	# The above template displays a radio button for each question choice. 
	# The value of each radio button is the associated question choice’s ID. 
	# The name of each radio button is "choice". 
	# That means, when somebody selects one of the radio buttons and submits the form, 
	# it’ll send the POST data choice=# where # is the ID of the selected choice. 
	# This is the basic concept of HTML forms.
	
	# We set the form’s action to {% url 'polls:vote' question.id %}, and we set method="post". 
	# Using method="post" (as opposed to method="get") is very important, 
	# because the act of submitting this form will alter data server-side. 
	# Whenever you create a form that alters data server-side, use method="post". 
	# This tip isn’t specific to Django; it’s just good Web development practice.
	
	# forloop.counter indicates how many times the for tag has gone through its loop
	
	# Since we’re creating a POST form (which can have the effect of modifying data), 
	# we need to worry about Cross Site Request Forgeries. 
	# Thankfully, you don’t have to worry too hard, 
	# because Django comes with a very easy-to-use system for protecting against it. 
	# In short, all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag.

# Now, let’s create a Django view that handles the submitted data and does something with it. 
# Remember, in Tutorial 3, we created a URLconf for the polls application that includes this line:

#polls/urls.py
url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

# We also created a dummy implementation of the vote() function. 
# Let’s create a real version. Add the following to polls/views.py:

#polls/views.py
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from polls.models import Choice, Question
# ...
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# This code includes a few things we haven’t covered yet in this tutorial:

	# request.POST is a dictionary-like object that lets you access submitted data by key name. 
	# In this case, request.POST['choice'] returns the ID of the selected choice, as a string. 
	# request.POST values are always strings.

	# Note that Django also provides request.GET for accessing GET data in the same way – 
	# but we’re explicitly using request.POST in our code, 
	# to ensure that data is only altered via a POST call.

	# request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. 
	# The above code checks for KeyError and 
	# redisplays the question form with an error message if choice isn’t given.

	# After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. 
	# HttpResponseRedirect takes a single argument: the URL to which the user will be redirected 
	# (see the following point for how we construct the URL in this case).

	# As the Python comment above points out,
	# you should always return an HttpResponseRedirect after successfully dealing with POST data. 
	# This tip isn’t specific to Django; it’s just good Web development practice.

	# We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
	# This function helps avoid having to hardcode a URL in the view function. 
	# It is given the name of the view that we want to pass control to and 
	# the variable portion of the URL pattern that points to that view. 
	# In this case, using the URLconf we set up in Tutorial 3, this reverse() call will return a string like

'/polls/3/results/'

	# ... where the 3 is the value of p.id. 
	# This redirected URL will then call the 'results' view to display the final page.

	# As mentioned in Tutorial 3, request is a HttpRequest object. 
	# For more on HttpRequest objects, see the request and response documentation.

	# After somebody votes in a question, 
	# the vote() view redirects to the results page for the question. 

	#Let’s write that view:

polls/views.py
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# This is almost exactly the same as the detail() view from Tutorial 3. 
# The only difference is the template name. We’ll fix this redundancy later.

# Now, create a polls/results.html template:

#polls/templates/polls/results.html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>

# Now, go to /polls/1/ in your browser and vote in the question. 
# You should see a results page that gets updated each time you vote. 
# If you submit the form without having chosen a choice, you should see the error message.


####################################################
####################################################
####################################################


#### Use generic views: Less code is better ####

# The detail() (from Tutorial 3) and results() views are stupidly simple – 
# and, as mentioned above, redundant. 
# The index() view (also from Tutorial 3), which displays a list of polls, is similar.

# These views represent a common case of basic Web development: 
# getting data from the database according to a parameter passed in the URL, 
# loading a template and returning the rendered template. 
# Because this is so common, Django provides a shortcut, called the “generic views” system.

# Generic views abstract common patterns to the point where you don’t even need to write Python code to write an app.

# Let’s convert our poll app to use the generic views system, 
# so we can delete a bunch of our own code. 
# We’ll just have to take a few steps to make the conversion. 
# We will:

# Convert the URLconf.
# Delete some of the old, unneeded views.
# Introduce new views based on Django’s generic views.

# Read on for details.

	# Why the code-shuffle?

	# Generally, when writing a Django app, you’ll evaluate whether generic views 
	# are a good fit for your problem, and you’ll use them from the beginning, 
	# rather than refactoring your code halfway through.
	# But this tutorial intentionally has focused on writing the views “the hard way” 
	# until now, to focus on core concepts.

	# You should know basic math before you start using a calculator.


####################
####################


# Step 1 # Convert the URLconf.

#### Amend URLconf ####

# First, open the polls/urls.py URLconf and change it like so:

#polls/urls.py
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)


# Note that the name of the matched pattern in the regexes of the second and third patterns 
# has changed from <question_id> to <pk>.


####################
####################


# Step 2 # Delete some of the old, unneeded views.

#### Amend views ####

# Next, we’re going to remove our old index, detail, and results views 
# and use Django’s generic views instead. 
# To do so, open the polls/views.py file and change it like so:

#polls/views.py
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above

# We’re using two generic views here: ListView and DetailView. 
# Respectively, those two views abstract the concepts of 
# “display a list of objects” and 
# “display a detail page for a particular type of object.”

	# Each generic view needs to know what model it will be acting upon. 
	# This is provided using the model attribute.
	
	# The DetailView generic view expects the primary key value captured from the URL to be called "pk", 
	# so we’ve changed question_id to pk for the generic views.

# By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html.
# In our case, it would use the template "polls/question_detail.html". 
# The template_name attribute is used to tell Django to use a specific template name 
# instead of the autogenerated default template name. 
# We also specify the template_name for the results list view – 
# this ensures that the results view and the detail view have a different appearance when rendered, 
# even though they’re both a DetailView behind the scenes.

# Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html; 
# we use template_name to tell ListView to use our existing "polls/index.html" template.

# In previous parts of the tutorial, the templates have been provided with a context 
# that contains the question and latest_question_list context variables. 
# For DetailView the question variable is provided automatically – since we’re using a Django model (Question), 
# Django is able to determine an appropriate name for the context variable. 
# However, for ListView, the automatically generated context variable is question_list. 
# To override this we provide the context_object_name attribute, 
# specifying that we want to use latest_question_list instead. 
# As an alternative approach, you could change your templates to match the new default context variables – 
# but it’s a lot easier to just tell Django to use the variable you want.

# Run the server, and use your new polling app based on generic views.

# For full details on generic views, see the generic views documentation.
# https://docs.djangoproject.com/en/1.7/topics/class-based-views/

# When you’re comfortable with forms and generic views, 
# read part 5 of this tutorial to learn about testing our polls app.


############################################################################
############################################################################
############################################################################


#### Writing your first Django app, part 5 ####

# This tutorial begins where Tutorial 4 left off. 
# We’ve built a Web-poll application, and we’ll now create some automated tests for it.


####################################################
####################################################
####################################################


#### Introducing automated testing ####

### What are automated tests? ###

# Tests are simple routines that check the operation of your code.

# Testing operates at different levels. 
# Some tests might apply to a tiny detail 
	#(does a particular model method return values as expected?) 
# while others examine the overall operation of the software 
	#(does a sequence of user inputs on the site produce the desired result?). 

# That’s no different from the kind of testing you did earlier in Tutorial 1, 
# using the shell to examine the behavior of a method, 
# or running the application and entering data to check how it behaves.

# What’s different in automated tests is that the testing work is done for you by the system. 
# You create a set of tests once, and then as you make changes to your app, 
# you can check that your code still works as you originally intended, 
# without having to perform time consuming manual testing.

#######
#######

### Why you need to create tests ###

# So why create tests, and why now?

# You may feel that you have quite enough on your plate just learning Python/Django, 
# and having yet another thing to learn and do may seem overwhelming and perhaps unnecessary. 
# After all, our polls application is working quite happily now; 
# going through the trouble of creating automated tests is not going to make it work any better. 
# If creating the polls application is the last bit of Django programming you will ever do, 
# then true, you don’t need to know how to create automated tests. 
# But, if that’s not the case, now is an excellent time to learn.

#######
#######

### Tests will save you time ###

# Up to a certain point, ‘checking that it seems to work’ will be a satisfactory test. 
# In a more sophisticated application, you might have dozens of complex interactions between components.

# A change in any of those components could have unexpected consequences on the application’s behavior. 
# Checking that it still ‘seems to work’ could mean running through your code’s functionality with 
# twenty different variations of your test data just to make sure you haven’t broken something - 
# not a good use of your time.

# That’s especially true when automated tests could do this for you in seconds. 
# If something’s gone wrong, tests will also assist in identifying the code that’s causing the unexpected behavior.

# Sometimes it may seem a chore to tear yourself away from your productive, creative programming work to face 
# the unglamorous and unexciting business of writing tests, particularly when you know your code is working properly.

# However, the task of writing tests is a lot more fulfilling than spending hours testing your application manually 
# or trying to identify the cause of a newly-introduced problem.

#######
#######

### Tests don’t just identify problems, they prevent them ###

# It’s a mistake to think of tests merely as a negative aspect of development.

# Without tests, the purpose or intended behavior of an application might be rather opaque. 
# Even when it’s your own code, you will sometimes find yourself poking around in it 
# trying to find out what exactly it’s doing.

# Tests change that; they light up your code from the inside, and when something goes wrong, 
# they focus light on the part that has gone wrong - even if you hadn’t even realized it had gone wrong.

#######
#######

### Tests make your code more attractive ###

# You might have created a brilliant piece of software, but you will find that many other developers 
# will simply refuse to look at it because it lacks tests; without tests, they won’t trust it. 
# Jacob Kaplan-Moss, one of Django’s original developers, says “Code without tests is broken by design.”

# That other developers want to see tests in your software before they take it seriously 
# is yet another reason for you to start writing tests.

#######
#######

### Tests help teams work together

# The previous points are written from the point of view of a single developer maintaining an application. 
# Complex applications will be maintained by teams. 
# Tests guarantee that colleagues don’t inadvertently break your code 
# (and that you don’t break theirs without knowing). 
# If you want to make a living as a Django programmer, you must be good at writing tests!


####################################################
####################################################
####################################################

#### Basic testing strategies ####

# There are many ways to approach writing tests.

# Some programmers follow a discipline called “test-driven development”; 
	# http://en.wikipedia.org/wiki/Test-driven_development
# they actually write their tests before they write their code. 
# This might seem counter-intuitive, but in fact it’s similar to what most people will often do anyway: 
# they describe a problem, then create some code to solve it. 
# Test-driven development simply formalizes the problem in a Python test case.

# More often, a newcomer to testing will create some code and later decide that it should have some tests. 
# Perhaps it would have been better to write some tests earlier, but it’s never too late to get started.

# Sometimes it’s difficult to figure out where to get started with writing tests. 
# If you have written several thousand lines of Python, choosing something to test might not be easy. 
# In such a case, it’s fruitful to write your first test the next time you make a change, 
# either when you add a new feature or fix a bug.

# So let’s do that right away.

####################################################
####################################################
####################################################

#### Writing our first test ####

# Testing internal behavior of the code.

### We identify a bug

# Fortunately, there’s a little bug in the polls application for us to fix right away: 
# the Question.was_published_recently() method returns True 
# if the Question was published within the last day (which is correct) but also 
# if the Question’s pub_date field is in the future (which certainly isn’t).

# You can see this in the Admin; create a question whose date lies in the future; 
# you’ll see that the Question change list claims it was published recently.

# You can also see this using the shell:

>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
>>> past_question = Question(pub_date=timezone.now() + datetime.timedelta(days=-1))
>>> # was it published recently?
>>> past_question.was_published_recently()
False

# Since things in the future are not ‘recent’, this is clearly wrong.

#######
#######

### Create a test to expose the bug

# What we’ve just done in the shell to test for the problem is exactly what we can do in an automated test, 
# so let’s turn that into an automated test.

# A conventional place for an application’s tests is in the application’s tests.py file; 
# the testing system will automatically find tests in any file whose name begins with test.

# Put the following in the tests.py file in the polls application:

# polls/tests.py
import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        Tests the the Question.was_published_recently() method.
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)


# What we have done here is created a django.test.TestCase subclass with a method that 
# creates a Question instance with a pub_date in the future. 
# We then check the output of was_published_recently() - which ought to be False.

#######
#######

### Running tests

# In the terminal, we can run our test:

$ python manage.py test polls

# and you’ll see something like:

'''
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertEqual(future_question.was_published_recently(), False)
AssertionError: True != False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
'''

# What happened is this:

# python manage.py test polls looked for tests in the polls application
# it found a subclass of the django.test.TestCase class
# it created a special database for the purpose of testing
# it looked for test methods - ones whose names begin with test
# in test_was_published_recently_with_future_question it created a 
	# Question instance whose pub_date field is 30 days in the future
# ... and using the assertEqual() method, it discovered that its was_published_recently() returns True, 
	# though we wanted it to return False
# The test informs us which test failed and even the line on which the failure occurred.

#######
#######

### Fixing the bug

# We already know what the problem is: Question.was_published_recently() 
# should return False if its pub_date is in the future. Amend the method in models.py, 
# so that it will only return True if the date is also in the past:

polls/models.py
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

#and run the test again:

'''
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
'''

# After identifying a bug, we wrote a test that exposes it and corrected the bug in the code so our test passes.

# Many other things might go wrong with our application in the future, 
# but we can be sure that we won’t inadvertently reintroduce this bug, 
# because simply running the test will warn us immediately. 
# We can consider this little portion of the application pinned down safely forever.

#######
#######

### More comprehensive tests

# While we’re here, we can further pin down the was_published_recently() method; 
# in fact, it would be positively embarrassing if in fixing one bug we had introduced another.

# Add two more test methods to the same class, to test the behavior of the method more comprehensively:

#polls/tests.py
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() should return False for questions whose
    pub_date is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() should return True for questions whose
    pub_date is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)

# And now we have three tests that confirm that Question.was_published_recently() 
# returns sensible values for past, recent, and future questions.

# Again, polls is a simple application, 
# but however complex it grows in the future and whatever other code it interacts with, 
# we now have some guarantee that the method we have written tests for will behave in expected ways.


####################################################
####################################################
####################################################


#### Test a view ####

# Test behavior as it would be experienced by a user through a web browser

# The polls application is fairly undiscriminating: it will publish any question, 
# including ones whose pub_date field lies in the future. We should improve this. 
# Setting a pub_date in the future should mean that the Question is published at that moment, 
# but invisible until then.

#######
#######

### A test for a view

# When we fixed the bug above, we wrote the test first and then the code to fix it. 
# In fact that was a simple example of test-driven development, 
# but it doesn’t really matter in which order we do the work.

# In our first test, we focused closely on the internal behavior of the code. 
# For this test, we want to check its behavior as it would be experienced by a user through a web browser.

# Before we try to fix anything, let’s have a look at the tools at our disposal.

#######
#######

### The Django test client

# Django provides a test Client to simulate a user interacting with the code at the view level. 
# We can use it in tests.py or even in the shell.

# We will start again with the shell, where we need to do a couple of things that won’t be necessary in tests.py.
# The first is to set up the test environment in the shell:

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

# setup_test_environment() installs a template renderer which will allow us to examine some additional 
# attributes on responses such as response.context that otherwise wouldn’t be available. 
# Note that this method does not setup a test database, 
# so the following will be run against the existing database and 
# the output may differ slightly depending on what questions you already created.

# Next we need to import the test client class 
# (later in tests.py we will use the django.test.TestCase class, 
	# which comes with its own client, so this won’t be required):

>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()

# With that ready, we can ask the client to do some work for us:

>>> # get a response from '/'
>>> response = client.get('/')
>>> # we should expect a 404 from that address
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> response = client.get('/polls/')
>>> # we should expect a 200 from that address
>>> response.status_code
200
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.core.urlresolvers import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
'\n\n\n    <p>No polls are available.</p>\n\n'
>>> # note - you might get unexpected results if your ``TIME_ZONE``
>>> # in ``settings.py`` is not correct. If you need to change it,
>>> # you will also need to restart your shell session
>>> from polls.models import Question
>>> from django.utils import timezone
>>> # create a Question and save it
>>> q = Question(question_text="Who is your favorite Beatle?", pub_date=timezone.now())
>>> q.save()
>>> # check the response once again
>>> response = client.get('/polls/')
>>> response.content
'\n\n\n    <ul>\n    \n        <li><a href="/polls/1/">Who is your favorite Beatle?</a></li>\n    \n    </ul>\n\n'
>>> # If the following doesn't work, you probably omitted the call to
>>> # setup_test_environment() described above
>>> response.context['latest_question_list']
[<Question: Who is your favorite Beatle?>]

#######
#######

### Improving our view

# The list of polls shows polls that aren’t published yet (i.e. those that have a pub_date in the future). 
# Let’s fix that.

# In Tutorial 4 we introduced a class-based view, based on ListView:

#polls/views.py
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# response.context_data['latest_question_list'] extracts the data this view places into the context.

# We need to amend the get_queryset method and change it so that it also checks the date 
# by comparing it with timezone.now(). First we need to add an import:

#polls/views.py
from django.utils import timezone

# and then we must amend the get_queryset method like so:

#polls/views.py
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

# Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing 
# Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.

#######
#######

### Testing our new view

# Now you can satisfy yourself that this behaves as expected by firing up the runserver, 
# loading the site in your browser, creating Questions with dates in the past and future, 
# and checking that only those that have been published are listed. 
# You don’t want to have to do that every single time you make any change that might affect this - 
# so let’s also create a test, based on our shell session above.

# Add the following to polls/tests.py:

#polls/tests.py
from django.core.urlresolvers import reverse

# and we’ll create a shortcut function to create questions as well as a new test class:

polls/tests.py
def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


# Let’s look at some of these more closely.

# First is a question shortcut function, create_question, 
# to take some repetition out of the process of creating questions.

# test_index_view_with_no_questions doesn’t create any questions, but checks the message: “No polls are available.” 
# and verifies the latest_question_list is empty. 
# Note that the django.test.TestCase class provides some additional assertion methods. 
# In these examples, we use assertContains() and assertQuerysetEqual().

# In test_index_view_with_a_past_question, we create a question and verify that it appears in the list.

# In test_index_view_with_a_future_question, we create a question with a pub_date in the future. 
# The database is reset for each test method, so the first question is no longer there, 
# and so again the index shouldn’t have any questions in it.

# And so on. In effect, we are using the tests to tell a story of admin input and user experience on the site, 
# and checking that at every state and for every new change in the state of the system, 
# the expected results are published.

#######
#######

### Testing the DetailView

# What we have works well; however, even though future questions don’t appear in the index, 
# users can still reach them if they know or guess the right URL. 
# So we need to add a similar constraint to DetailView:

#polls/views.py
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# And of course, we will add some tests, 
# to check that a Question whose pub_date is in the past can be displayed, 
# and that one with a pub_date in the future is not:

#polls/tests.py
class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        response = self.client.get(reverse('polls:detail',
                                   args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        response = self.client.get(reverse('polls:detail',
                                   args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                            status_code=200)

#######
#######

### Ideas for more tests

# We ought to add a similar get_queryset method to ResultsView and create a new test class for that view.
# It’ll be very similar to what we have just created; in fact there will be a lot of repetition.

# We could also improve our application in other ways, adding tests along the way. 
# For example, it’s silly that Questions can be published on the site that have no Choices. 
# So, our views could check for this, and exclude such Questions. 
# Our tests would create a Question without Choices and then test that it’s not published, 
# as well as create a similar Question with Choices, and test that it is published.

#### From end of page # https://docs.djangoproject.com/en/1.7/intro/tutorial05/

####  MY WORKINGS ####
# Change below to make it not accept questions which do not have choices

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


all_questions = Question.objects.filter()  #list of all questions
[i.choice_set.exists() for i in Question.objects.filter()] #list of all choices for those questions

[i for i in Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] if i.choice_set.exists()]
#list of questions if choice_set exists!


#### NOW BUILD TEST FOR IT ####

# design test to verify that questions with no choices are not shown.

## Creates question
def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)


## Create Choice function to create choices for a question
def create_choice(choice_text, question_id):
	"""
	Creatas a choice with the given `choice_text` published for a given
	question that has been created using create_question.
	"""
	return  Choice.objects.create(question = Question.objects.get(id=question_id), 
									choice_text = choice_text, 
									votes = 0)


## Create test for if question has choices it should be shown.
class QuestionViewTests(TestCase):
    def test_index_view_only_questions_with_choices(self):
        """
        If choices exist for specific question, then that question should be shown.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        question = create_question(question_text="A Question.", days=-5)
        question
        create_choice(choice_text="A Choice.", question_id=question.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: A Question.>']
        )

## Create test for if question has no choices it should not be shown.
    def test_index_view_only_questions_with_NOchoices(self):
        """
        If no choices exist for specific question, then that question should not be shown.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        question1 = create_question(question_text="A Question 1.", days=-5)
        question1
        create_choice(choice_text="A Choice.", question_id=question1.id)
        question2 = create_question(question_text="A Question 2.", days=-5)
        question2
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: A Question 1.>']
        )

#### WORKS!!! 20150331

## I also had to change all the other tests to conform to this new rule:
# that a question should have a choice, otherwise it will not be displayed.

# And added a test that tested that if there were 6 questions only the most recent 5 would be displayed.

#### END OF MY WORKINGS ####

# Perhaps logged-in admin users should be allowed to see unpublished Questions, 
# but not ordinary visitors. 
# Again: whatever needs to be added to the software to accomplish this should be 
# accompanied by a test, whether you write the test first and then make the code pass the test, 
# or work out the logic in your code first and then write a test to prove it.

# At a certain point you are bound to look at your tests and wonder whether 
# your code is suffering from test bloat, which brings us to:

#######
#######

#### When testing, more is better #####

# It might seem that our tests are growing out of control. 
# At this rate there will soon be more code in our tests than in our application, 
# and the repetition is unaesthetic, compared to the elegant conciseness of the rest of our code.

# It doesn’t matter. Let them grow. 
# For the most part, you can write a test once and then forget about it. 
# It will continue performing its useful function as you continue to develop your program.

# Sometimes tests will need to be updated. 
# Suppose that we amend our views so that only Questions with Choices are published. 
# In that case, many of our existing tests will fail - 
# telling us exactly which tests need to be amended to bring them up to date, 
# so to that extent tests help look after themselves.

# At worst, as you continue developing, 
# you might find that you have some tests that are now redundant. 
# Even that’s not a problem; in testing redundancy is a good thing.

# As long as your tests are sensibly arranged, they won’t become unmanageable. 
# Good rules-of-thumb include having:

# a separate TestClass for each model or view
# a separate test method for each set of conditions you want to test
# test method names that describe their function

#######
#######

#### Further testing ####

# This tutorial only introduces some of the basics of testing. 
# There’s a great deal more you can do, and a number of very useful tools 
# at your disposal to achieve some very clever things.

# For example, while our tests here have covered some of the internal logic of a model 
# and the way our views publish information, you can use an “in-browser” framework 
# such as Selenium to test the way your HTML actually renders in a browser. 
# These tools allow you to check not just the behavior of your Django code, 
# but also, for example, of your JavaScript. 
# It’s quite something to see the tests launch a browser, and start interacting with your site, 
# as if a human being were driving it! Django includes LiveServerTestCase to facilitate 
# integration with tools like Selenium.

# If you have a complex application, you may want to run tests automatically with every commit for 
# the purposes of continuous integration, so that quality control is itself - at least partially - automated.

# A good way to spot untested parts of your application is to check code coverage. 
# This also helps identify fragile or even dead code. 
# If you can’t test a piece of code, it usually means that code should be refactored or removed. 
# Coverage will help to identify dead code. See Integration with coverage.py for details.

# Testing in Django has comprehensive information about testing.

#### What’s next? ###

# For full details on testing, see Testing in Django. 
# https://docs.djangoproject.com/en/1.7/topics/testing/

# When you’re comfortable with testing Django views, 
# read part 6 of this tutorial to learn about static files management.

############################################################################
############################################################################
############################################################################

#### Writing your first Django app, part 6 ####

# This tutorial begins where Tutorial 5 left off. 
# We’ve built a tested Web-poll application, and we’ll now add a stylesheet and an image.

# Aside from the HTML generated by the server, web applications generally need to serve additional files — 
# such as images, JavaScript, or CSS — necessary to render the complete web page. 
# In Django, we refer to these files as “static files”.

# For small projects, this isn’t a big deal, 
# because you can just keep the static files somewhere your web server can find it. 
# However, in bigger projects – especially those comprised of multiple apps – 
# dealing with the multiple sets of static files provided by each application starts to get tricky.

# That’s what django.contrib.staticfiles is for: 
# it collects static files from each of your applications (and any other places you specify) 
# into a single location that can easily be served in production.

####################################################
####################################################
####################################################

#### Customize your app’s look and feel ####

# First, create a directory called static in your polls directory. 
# Django will look for static files there, similarly to how Django finds templates inside polls/templates/.

# Django’s STATICFILES_FINDERS setting contains a list of finders 
# that know how to discover static files from various sources. 
# One of the defaults is AppDirectoriesFinder which looks for a “static” subdirectory 
# in each of the INSTALLED_APPS, like the one in polls we just created. 
# The admin site uses the same directory structure for its static files.

# Within the static directory you have just created, create another directory called polls 
# and within that create a file called style.css. 
# In other words, your stylesheet should be at polls/static/polls/style.css. 
# Because of how the AppDirectoriesFinder staticfile finder works, 
# you can refer to this static file in Django simply as polls/style.css, 
# similar to how you reference the path for templates.

	## Static file namespacing ##

	# Just like templates, we might be able to get away with putting our static files directly in 
	# polls/static (rather than creating another polls subdirectory), but it would actually be a bad idea. 
	# Django will choose the first static file it finds whose name matches, 
	# and if you had a static file with the same name in a different application, 
	# Django would be unable to distinguish between them. 
	# We need to be able to point Django at the right one, 
	# and the easiest way to ensure this is by namespacing them. 
	# That is, by putting those static files inside another directory named for the application itself.

# Put the following code in that stylesheet (polls/static/polls/style.css):

#polls/static/polls/style.css
li a {
    color: green;
}

# Next, add the following at the top of polls/templates/polls/index.html:

#polls/templates/polls/index.html
{% load staticfiles %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />

# {% load staticfiles %} loads the {% static %} template tag from the staticfiles template library. 
# The {% static %} template tag generates the absolute URL of the static file.

# That’s all you need to do for development. 
# Reload http://localhost:8000/polls/ and you should see that the question links are green 
# (Django style!) which means that your stylesheet was properly loaded.

#######
#######

#### Adding a background-image ####

# Next, we’ll create a subdirectory for images. 
# Create an images subdirectory in the polls/static/polls/ directory. 
# Inside this directory, put an image called background.gif. 
# In other words, put your image in polls/static/polls/images/background.gif.

# Then, add to your stylesheet (polls/static/polls/style.css):

#polls/static/polls/style.css
body {
    background: white url("images/background.gif") no-repeat right bottom;
}

# Reload http://localhost:8000/polls/ and you should see the background loaded in the bottom right of the screen.


	## Warning

	# Of course the {% static %} template tag is not available for use in static files 
	# like your stylesheet which aren’t generated by Django. 
	# You should always use relative paths to link your static files between each other, 
	# because then you can change STATIC_URL (used by the static template tag to generate its URLs) 
	# without having to modify a bunch of paths in your static files as well.

# These are the basics. 
# For more details on settings and other bits included with the framework see the static files how to 
# and the staticfiles reference. Deploying static files discusses how to use static files on a real server.


#### What’s next? ####

# The beginner tutorial ends here for the time being. 
# In the meantime, you might want to check out some pointers on where to go from here.

# If you are familiar with Python packaging and interested in learning how to turn polls into a “reusable app”, 
# check out Advanced tutorial: How to write reusable apps.


# NEXT UP REUSABLE APP
####
# https://docs.djangoproject.com/en/1.7/intro/reusable-apps/
####




################################################################################################
######################## Continue working on the app, with help from pystar ####################
################################################################################################

################################################################################################
########################		  	DONE!!!!!!!!!!!!!!!!   				    ####################
################################################################################################



#### Around line 620 in the Django_Mockups_Views_andURLS_20150423 file

## line : "Copy test_polls.py and move it into polls directory"



##############################################################################
##############################################################################
##############################################################################


#### Include the tests that pystar gives us ####

	## compare them with the ones I have written.

    ## https://raw.githubusercontent.com/pystar/pystar/master/docs/test_polls.py

'''
Tests for the 'polls' application.  Call using:

    ./manage.py test polls

'''


# called automatically by ./manage.py test; no harm though.
from django.test.utils import setup_test_environment
setup_test_environment()

# uses the new 'unittest2' improved testing framework, django 1.3+
from django.utils import unittest 
from django.test.client import Client

import datetime
import random

import django
if django.VERSION < (1,3):
    raise Exception("Needs Django 1.3+, becuase it uses unittest2")


## check whether the models even exist yet!
models_importable = False
try:
    from polls.models import Choice,Poll
    models_importable = True
except ImportError:
    pass



def setup_metal(seed=2929485983):
    '''
    produce a number of heavy metal polls, to populate the db with.
    
    Args:
        seed:  int for random number generator
    
    Returns:
        a list of constucted, *saved* polls.
    
    '''
    opinions = ['HEINOUS!', 'suxxors', 'rulez!', 
    'AWESOME!', 'righTEOUS', 'HAVE MY BABY!!!!',
    'BEYOND METAL','SUCKS','RULES', 'TOTALLY RULES']

    band_names = '''
    Abonos Meshuggah Xasthur Silencer Fintroll Beherit Basilisk Cryptopsy
    '''.strip().split()

    random.seed(seed)  # so it will always make the same polls
    def make_metal_poll(bandname,opinions):
        pub = datetime.datetime.now()
        marks = '?' * random.randint(1,5)
        question = bandname + marks
        chosen = random.sample(opinions,5)
        choices = list()
        for c in chosen:
            votes = random.randint(1,1000)
            choices.append(Choice(choice=c,votes=votes))
        
        p = Poll(question=question,pub_date=pub)
        p.save()
        p.choice_set=choices
        return p

    polls = [make_metal_poll(band,opinions) for band in band_names]
    return polls

## Tests

''' (r'^polls/$', 'polls.views.index'),
 (r'^polls/(\d+)/$', 'polls.views.detail'),
 (r'^polls/(\d+)/results/$', 'polls.views.results'),
 (r'^polls/(\d+)/vote/$', 'polls.views.vote'),'''

class Text_example(unittest.TestCase):
    def test_testing_is_sane(self):
        self.assertEqual(1,1)


## some testing utilities
def get(url):
    c = Client()
    response = c.get(url)
    return response

def post(url,post_kwargs=None):
    if post_kwargs is None:  post_kwargs={}
    c = Client()
    response = c.post(url,post_kwargs)
    return response

def fail(self,msg=None):
    self.assertFalse(True,msg=msg)

def ok_(self,msg=None):
    self.assertTrue(True,msg=msg)


def no_test_written(self):
    fail(self,"test not yet written")


def vote(poll_id,up=True):
    url = '/polls/%i/vote' % poll_id,
    r = post(url,)
    return r

def get_poll(id):
    try:
        return Poll.objects.get(id=id)
    except Exception,exc:
        return None


class Test_urls(unittest.TestCase):

    def test_root_redirects(self):
        response = get('/')
        self.assertEqual(response.status_code, 302)

    def test_poll_responds(self):
        response = get('/polls/')
        self.assertEqual(response.status_code, 200)

    def test_poll_reachable_if_exists(self):
        response = get('/polls/1/results/')
        self.assertEqual(response.status_code, 200)

    def test_poll_vote_reachable_if_exists(self):
        response = get('/polls/1/vote/')
        self.assertEqual(response.status_code, 200)

    def test_non_exist_poll_404s(self):
        # get a non-existent poll, then 404!
        response = get('/polls/1000000/')
        self.assertEqual(response.status_code, 404)
    
    def test_poll_post_without_choice_redirects(self):
        # Verify that if you submit the form without having chosen a 
        # choice, you should stay
        response = post('/polls/1/vote',{})
        self.assertEqual(response.status_code, 301)


class Test_index(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_index_has_5(self):
        if not models_importable :
            self.assertFalse()
        
        response = post('/polls/')
        content = response.content
        # silly!
        self.assertTrue(content.count('<li>',5))

class Test_detail(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_poll_1_has_right_count_of_choices(self):
        if not models_importable :
            self.assertFalse()
        
        expecting = len(get_poll(1).choice_set.all())
        response = post('/polls/1/')
        content = response.content
        # silly!
        self.assertEqual(content.count('radio'), expecting)

class Test_voting(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None

    def test_vote_up_raises_vote_by_one(self):
        if not models_importable :
            self.assertFalse()
        
        c = get_poll(1).choice_set.all()[0]
        before = c.votes

        # simlulate a vote
        r = response = post('/polls/1/vote/',{'choice':c.id})
        c = get_poll(1).choice_set.all()[0]
        after = c.votes
        self.assertEqual(before+1, after)

    def test_after_vote_redirect_to_poll_details(self):
        ## after voting in a poll, it should redirect to that poll
        # post=....).redirects to whatever!
        if not models_importable :
            self.assertFalse()
        
        c = get_poll(1).choice_set.all()[0]
        r = response = post('/polls/1/vote/',{'choice':c.id})
        self.assertEqual(response.status_code, 302)
        # /polls/1/results/


## there must be a more elegant way
## to get this from Django!
def check_attrs(obj,attrs):
    for attr in attrs:
        try:
            getattr(obj,attr)
        except AttributeError,Exc:
            return False
        
        return True


## this isn't a great test, but illustrative.
## (unit-testy, fragile, not BDD).
class Test_models(unittest.TestCase):
    def setUp(self):
        if models_importable :
            self.polls = setup_metal()
        else:
            self.polls=None
    
    def test_poll_has_right_fields(self):
        if not models_importable:
            fail(self)
        
        P = Poll()
        assert check_attrs(P,['choice_set','question','pub_date','was_published_today'])
    
    def test_choice_has_right_fields(self):
        if not models_importable:
            fail(self)
        
        C = Choice()
        assert check_attrs(C,['choice','votes'])




## polls need to have pubdate and text
## choices need text and votes

## also choices need a 'is today' method.

## templates!









## I finished going through the PyStar version of the app.
## I think the django tutorial had been updated since the last pystar update. 











###############################################################################
################## No Longer Used ##  mysite/polls/urls.py ####################
###############################################################################


#NEW:
#urlpatterns = patterns('',
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#)
#
#OLD:
#urlpatterns = patterns('',
#	## url(regex, view, kwargs=None, name=None, prefix='')
#    # ex: /polls/
#    url(r'^$', views.index, name='index'),
#    # ex: /polls/5/
#    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#    # ex: /polls/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#)



###############################################################################
################## No Longer Used ##  mysite/polls/views.py ###################
###############################################################################
#

#FROM VVV: 
	#def index(request):
	#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#    context = {'latest_question_list': latest_question_list}
	#    template_name = 'polls/index.html'
	#    #render() : https://docs.djangoproject.com/en/1.7/topics/http/shortcuts/#django.shortcuts.render
	#    return render(request, template_name, context)
	#
	#
	## http://127.0.0.1:8000/polls/1/
	#def detail(request, question_id):
	#    question = get_object_or_404(Question, pk=question_id)
	#    return render(request, 'polls/detail.html', {'question': question})
	#
	#
	## http://127.0.0.1:8000/polls/1/results/
	#def results(request, question_id):
	#    question = get_object_or_404(Question, pk=question_id)
	#    return render(request, 'polls/results.html', {'question': question})
	## http://127.0.0.1:8000/polls/1/vote/
	#def vote(request, question_id):
	#    p = get_object_or_404(Question, pk=question_id)
	#    try:
	#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
	#    except (KeyError, Choice.DoesNotExist):
	#        # Redisplay the question voting form.
	#        return render(request, 'polls/detail.html', {
	#            'question': p,
	#            'error_message': "You didn't select a choice.",
	#        })
	#    else:
	#        selected_choice.votes += 1
	#        selected_choice.save()
	#        # Always return an HttpResponseRedirect after successfully dealing
	#        # with POST data. This prevents data from being posted twice if a
	#        # user hits the Back button.
	#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
	#


#TO VVV:
	#class IndexView(generic.ListView):
	#    template_name = 'polls/index.html'
	#    context_object_name = 'latest_question_list'
	#
	#    def get_queryset(self):
	#        """Return the last five published questions."""
	#        return Question.objects.order_by('-pub_date')[:5]
	#
	#
	#class DetailView(generic.DetailView):
	#    model = Question
	#    template_name = 'polls/detail.html'
	#
	#
	#class ResultsView(generic.DetailView):
	#    model = Question
	#    template_name = 'polls/results.html'
	#
	#def vote(request, question_id):
    #... # same as above


