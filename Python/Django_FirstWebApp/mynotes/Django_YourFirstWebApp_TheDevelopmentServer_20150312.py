## Django_YourFirstWebApp_TheDevelopmentServer_20150312

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp



########################################################################################################################
########################################################################################################################
########################################################################################################################

############## The development server ###########

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

# Changing the port
	
		# By default, the runserver command starts the development server on the internal IP at port 8000.
		# 
		# If you want to change the server’s port, pass it as a command-line argument.
		#  For instance, this command starts the server on port 8080:
		# 
		# $ python manage.py runserver 8080
		# If you want to change the server’s IP, pass it along with the port. So to listen on all public IPs 
		# (useful if you want to show off your work on other computers), use:

		# $ python manage.py runserver 0.0.0.0:8000
		# Full docs for the development server can be found in the runserver reference.

	# Automatic reloading of runserver
	# The development server automatically reloads Python code for each request as needed. 
	# You don’t need to restart the server for code changes to take effect. 
	# However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.


