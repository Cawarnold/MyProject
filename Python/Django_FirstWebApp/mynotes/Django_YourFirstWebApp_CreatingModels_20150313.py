## Django_YourFirstWebApp_CreatingModels_20150313

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp



########################################################################################################################
########################################################################################################################
########################################################################################################################

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

	# When a module named spam is imported, the interpreter first searches for a built-in module with that name. 
	# If not found, it then searches for a file named spam.py in a list of directories 
	# given by the variable sys.path. sys.path is initialized from these locations:
		# the directory containing the input script (or the current directory).
		# PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
		# the installation-dependent default.

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

	# Don't Repeat Yourself (DRY)
	# Every distinct concept and/or piece of data should live in one, and only one, place. Redundancy is bad. Normalization is good.

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


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


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




