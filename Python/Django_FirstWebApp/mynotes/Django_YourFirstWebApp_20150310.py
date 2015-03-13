## Django_YourFirstWebApp_20150310

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp



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

########################################################################################################################
########################################################################################################################
########################################################################################################################

#### Short Notes ####

### Installing Packages: 

	## To install package (django) to Anaconda/envs/py34:
		#> conda install -p ~/anaconda/envs/py34 django

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

### Hop into the interactive Python shell and play around with the free API Django gives you:

	python manage.py shell

### Create a Question:
	from polls.models import Question, Choice
	from django.utils import timezone
	q = Question(question_text="What's new?", pub_date=timezone.now())
	q.save()

#### View all Questions:
	Question.objects.all()

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



