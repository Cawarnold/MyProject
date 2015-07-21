## Django_YourFirstWebApp_StartProjectFiles_20150312

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp



########################################################################################################################
########################################################################################################################
########################################################################################################################

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


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### manage.py ####

	# A command-line utility that lets you interact with this Django project in various ways. 
		# You can read all the details about manage.py in django-admin.py and manage.py.
	
	## django-admin.py is Django’s command-line utility for administrative tasks.
	
	##manage.py is automatically created in each Django project. manage.py is a thin wrapper around django-admin.py 
	# that takes care of several things for you before delegating to django-admin.py:
	
	# It puts your project’s package on sys.path.
	# It sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.
	# It calls django.setup() to initialize various internals of Django.
	
	## Usage
	# manage.py <command> [options]


#### Packages ####

	# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
		# For example, the module name A.B designates a submodule named B in a package named A. 
		# Just like the use of modules saves the authors of different modules from having to worry 
		# about each other’s global variable names, the use of dotted module names saves the authors 
		# of multi-module packages like NumPy or the Python Imaging Library from having to worry 
		# about each other’s module names.

		
		'''
		sound/                          Top-level package
		      __init__.py               Initialize the sound package
		      formats/                  Subpackage for file format conversions
		              __init__.py
		              wavread.py
		              wavwrite.py
		              aiffread.py
		              aiffwrite.py
		              auread.py
		              auwrite.py
		              ...
		      effects/                  Subpackage for sound effects
		              __init__.py
		              echo.py
		              surround.py
		              reverse.py
		              ...
		      filters/                  Subpackage for filters
		              __init__.py
		              equalizer.py
		              vocoder.py
		              karaoke.py
		'''
		
		# Users of the package can import individual modules from the package, for example:
		import sound.effects.echo
		# This loads the submodule sound.effects.echo. It must be referenced with its full name.
		sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
		
		# An alternative way of importing the submodule is:
		from sound.effects import echo
		# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:
		echo.echofilter(input, output, delay=0.7, atten=4)
		
		# Yet another variation is to import the desired function or variable directly:
		from sound.effects.echo import echofilter
		# Again, this loads the submodule echo, but this makes its function echofilter() directly available:
		echofilter(input, output, delay=0.7, atten=4)
		
		# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, 
		# or some other name defined in the package, like a function, class or variable.
		

#### Django settings ####

	# A Django settings file contains all the configuration of your Django installation. 
	# A settings file is just a Python module with module-level variables.

	# Because a settings file is a Python module, the following apply:
		# It doesn’t allow for Python syntax errors.
		# It can assign settings dynamically using normal Python syntax. For example:
			MY_SETTING = [str(i) for i in range(30)]
		# It can import values from other settings files.

	# When using django-admin.py or manage.py, you can either set the environment variable once, 
	# or explicitly pass in the settings module each time you run the utility.
	set DJANGO_SETTINGS_MODULE=mysite.settings
	django-admin.py runserver
	# Use the --settings command-line argument to specify the settings manually:
	django-admin.py runserver --settings=mysite.settings


#### How to deploy with WSGI ####
	
	# Django’s primary deployment platform is WSGI, the Python standard for web servers and applications.
	# Django’s startproject management command sets up a simple default WSGI configuration for you, 
	# which you can tweak as needed for your project, and direct any WSGI-compliant application server to use.

	# Django includes getting-started documentation for the following WSGI servers:
		# How to use Django with Apache and mod_wsgi
		# Authenticating against Django’s user database from Apache
		# How to use Django with Gunicorn
		# How to use Django with uWSGI

	# The application object
		# The key concept of deploying with WSGI is the application callable which the application server 
		# uses to communicate with your code. 
		# It’s commonly provided as an object named 'application' in a Python module accessible to the server.
		# The startproject command creates a file <project_name>/wsgi.py that contains such an application callable.
		# It’s used both by Django’s development server and in production WSGI deployments.
		# WSGI servers obtain the path to the application callable from their configuration. 
		# Django’s built-in servers, namely the runserver and runfcgi commands, read it from the WSGI_APPLICATION setting. 
		# By default, it’s set to <project_name>.wsgi.application, which points to the application callable in <project_name>/wsgi.py.

