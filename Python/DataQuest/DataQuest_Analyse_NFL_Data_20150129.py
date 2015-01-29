## DataQuest_Analyse_NFL_Data_20150129

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Basics: Analyse NFL Data

#####################################

Overview of Useful code:
Importing Module. (Importing_and_using_modules)


#####################################

#### SUMMARY OF USEFUL CODE ####

#### Importing_and_using_modules ####

# Import the module, ther are lots of functions in a module (python file)
import math
# Access the functions in the module by using the module name, then a dot, then the function to use.
a = math.sqrt(16) # Square root
b = math.ceil(111.3) # Round up
c = math.floor(89.9) # Round down



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# NFL - National Football League
# 32 Teams in NFL
# 17 weeks in the regular season.
# Each team will play 16 Games.

# Each week will have several rows.
# Year, Week, Winner, Loser

# Data is from 2009 to 2013

#### Modules ####

# We're going to use modules to help us.
# Modules are chunks of code that somebody else has written.
# Module is something you can import.

import csv

# csv is a module that we are going to use to open and read our data.

#### Importing_and_using_modules ####

# Let's say we want to take the square root of a number.
# Python's math module has a handy function that can do that.
# But, we have to import the module before we can use it.
import math

# Now, we can access the functions in the module by using the module name, then a dot, then the function to use.
# The sqrt function in the math module will take the square root of a number.
print(math.sqrt(9))

# We can use other functions, too.
# The ceil function will always round a number up.
print(math.ceil(8.1))

# And the floor function will always round a number down.
print(math.floor(11.9))

# Tasks

a = math.sqrt(16) # Square root
b = math.ceil(111.3) # Round up
c = math.floor(89.9) # Round down

#### More about modules ####

import math

# Let's say we want to multiply pi by 2
print(math.pi * 2)

# We can also access other properties in modules.
# Some modules have variables defined inside them.
# Just like with functions, we can access them with the dot notation.
# Imagine a module as a street, with houses on that street being functions and variables.
# If you wanted to tell someone how to get to a house, 
# you would first tell them how to get to the street.
# Then you would tell them to turn onto the street and stop at the house.
# Python is the same way -- it has to know how to get to a function or variable before it can find it.
# If the function or variable is inside a module, 
# Python needs directions to be told about the module first.

#Tasks
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

#### Easy_way_to_read_csv_files ####




