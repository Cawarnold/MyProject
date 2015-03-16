## Django_YourFirstWebApp_20150310

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp

# Today, with mobile front-ends, cloud back-ends, and fully automated management infrastructure, 
# companies are able to launch across many countries at a very high speed with a strong, technology 
# and analytics-enabled central infrastructure and light local teams.


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
	# ctrl c to break the connection.

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

### Create a user who can login to the admin site. Run the following command:
	python manage.py createsuperuser

### Visit admin site, (first run server):
	python manage.py runserver
	# Then visit http://127.0.0.1:8000/admin/



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
# At this point, it’s worth reviewing what these arguments are for.

####################################################
####################################################
####################################################

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


