## Django_YourFirstWebApp_DataBaseSetup_20150312

# Writing your first Django app, part 1
## 	https://docs.djangoproject.com/en/1.7/intro/tutorial01/

# Directory
# C:\Users\Christian\Documents\GitHub\MyProject\Python\Django_FirstWebApp



########################################################################################################################
########################################################################################################################
########################################################################################################################

############## Database Setup ###########

# Now, edit mysite/settings.py. It’s a normal Python module with module-level variables representing Django settings.

	# By default, the configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, 
	# this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. 
	# When starting your first real project, however, you may want to use a more robust database like PostgreSQL, 
	# to avoid database-switching headaches down the road.

# If you wish to use another database, install the appropriate database bindings, 
# and change the following keys in the DATABASES 'default' item to match your database connection settings:

# ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql_psycopg2',other.

# NAME – The name of your database. 
# If you’re using SQLite, the database will be a file on your computer; 
# in that case, NAME should be the full absolute path, including filename, of that file. 
# The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.

# Note
# If you’re using PostgreSQL or MySQL, make sure you’ve created a database by this point. 
# Do that with “CREATE DATABASE database_name;” within your database’s interactive prompt.

# If you’re using SQLite, you don’t need to create anything beforehand - 
# the database file will be created automatically when it is needed.

########################################################################################################################
########################################################################################################################
########################################################################################################################

## Database bindings, get your database running

	# If you plan to use Django’s database API functionality, you’ll need to make sure a database server is running. Django supports many different database servers
	# and is officially supported with PostgreSQL, MySQL, Oracle and SQLite.

	# If you are developing a simple project or something you don’t plan to deploy in a production environment, 
	# SQLite is generally the simplest option as it doesn’t require running a separate server. 
	# However, SQLite has many differences from other databases, so if you are working on something substantial, 
	# it’s recommended to develop with the same database as you plan on using in production.

	# If you’re using PostgreSQL, you’ll need the psycopg2 package. Refer to the PostgreSQL notes for further details.

	# If you plan to use Django’s manage.py migrate command to automatically create database tables for your models 
	# (after first installing Django and creating a project), you’ll need to ensure that Django has permission 
	# to create and alter tables in the database you’re using; 
	# if you plan to manually create the tables, you can simply grant Django SELECT, INSERT, UPDATE and DELETE permissions. 
	# After creating a database user with these permissions, you’ll specify the details in your project’s settings file, 
	# see DATABASES for details.

# If you’re using Django’s testing framework to test database queries, Django will need permission to create a test database.

		# $ sqlite3 ex1
		# SQLite version 3.8.5 2014-05-29 12:36:14
		# Enter ".help" for usage hints.
		# sqlite> create table tbl1(one varchar(10), two smallint);
		# sqlite> insert into tbl1 values('hello!',10);
		# sqlite> insert into tbl1 values('goodbye', 20);
		# sqlite> select * from tbl1;
		# hello!|10
		# goodbye|20
		# sqlite> .schema
		# create table tbl1(one varchar(10), two smallint);


# this created a table and has nothing to do with the django app project.

