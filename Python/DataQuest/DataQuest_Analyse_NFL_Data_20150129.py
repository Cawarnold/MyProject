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

import csv

f = open("la_weather.csv", 'r')

# We call the reader function, which is inside the csv module.
# It returns a value that we assign to csvreader.
csvreader = csv.reader(f)

# We'll get more into what the value stored in the csvreader variable is later on.
# For now, we can turn it into a list by using the list function.
# Just like int() turns a value into an integer, list() turns a value into a list.
data = list(csvreader)

# Wasn't that easy?  We read in all of the weather data from the mission before, but we did it with a lot less work.
print(data)

# Read in all of the data from "nfl.csv" into the nfl variable using the csv module.

nfl_file = open("nfl.csv",'r')

nfl = list(csv.reader(nfl_file))

print(nfl)

#### Counting_how_many_times_a_team_won ####

# The nfl data is loaded into the nfl variable.

# Loop through the nfl data.
# Count up how many games the "New England Patriots" won from 2009-2013.
# Assign the count to patriots_wins. The count should be an integer.

patriots_wins = 0
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins = patriots_wins + 1
    else:
        print("Never Won")

print(patriots_wins)

#### Making_function_to_count_wins ####

# The nfl data is loaded into the nfl variable.

# Make a function that will take a team name, in the form of a string, as input.
# The function should output the number of wins the team had from 2009-2013, as an integer.
# Use the function to assign the number of wins by the "Dallas Cowboys" to cowboys_wins.
# Use the function to assign the number of wins by the "Atlanta Falcons" to falcons_wins.

def count_wins(team):
    count = int(0)
    for row in nfl:
        if row[2] == str(team):
            count = count + 1
    return count

cowboys_wins = count_wins("Dallas Cowboys")
falcons_wins = count_wins("Atlanta Falcons")

print("How many times did these teams win?")
print("Dallas Cowboys won: ",cowboys_wins)
print("Atlanta Falcons won: ",falcons_wins)

#### Using_boolean_statements_with_the_AND_keyword ####

its_raining = "Yes"
its_snowing = "No"

# Each statement is evaluated separately.
# If either of them is False on its own, then the whole statement is False.
print(its_raining == "Yes" and its_snowing == "Yes")

# If both evaluate to True, then the whole statement is True.
print(its_raining == "Yes" and its_snowing == "No")

drugs = 1.5
money = 100

# Assign a boolean that uses the and keyword and evaluates to True to a.
# Assign a boolean that uses the and keyword and evaluates to False to b.

a = (drugs == 1.5 and money == 100)
b = (drugs == 1.6 and money == 100)

#### Using_boolean_statements_with_the_OR_keyword ####

current_president = "Barack Obama"

# Each statement is evaluated separately.
# If either of them is True on its own, then the statement is True.
print(current_president == "Barack Obama" or current_president == "George Bush")

# If all of the statements evaluate to False, then the statement is False.
print(current_president == "Eminem" or current_president == "Kanye West")

# Assign a boolean that uses the or keyword and evaluates to True to a.
# Assign a boolean that uses the or keyword and evaluates to False to b.

go_brixton = "yes"

a = (go_brixton == "yes" or go_brixton == "no")
b = (go_brixton == "no" or go_brixton == "def no")





