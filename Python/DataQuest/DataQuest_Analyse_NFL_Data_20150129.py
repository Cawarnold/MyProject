## DataQuest_Analyse_NFL_Data_20150129

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Basics: Analyse NFL Data -- (Wins_by_year_method)

#####################################

Overview of Useful code:
Importing Module. (Importing_and_using_modules)
Using csv module to read files. (Easy_way_to_read_csv_files)
How many times did Patriots win? (Counting_how_many_times_a_team_won)
Making a function to count wins. (Making_function_to_count_wins)
Using Booleans statements _with AND. (Using_boolean_statements_with_the_AND_keyword)
Using Booleans statements _with OR. (Using_boolean_statements_with_the_OR_keyword)
Counting number of wins _for team _and year.(Counting_wins_in_a_given_year)
Intro to classes, the blueprint of variables _and functions. (Intro_to_classes)
Methods are just functions that are contained within a _class. (Instance_methods)
Open _and read the _file _from within the _class. (Adding_to_the_init_funciton)
Create a _class which has instance methods, total wins _and wins by year. (Wins_by_year_method)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Importing_and_using_modules ####

# Import the module, ther are lots of functions in a module (python file)
import math
# Access the functions in the module by using the module name, then a dot, then the function to use.
a = math.sqrt(16) # Square root
b = math.ceil(111.3) # Round up
c = math.floor(89.9) # Round down

#### Easy_way_to_read_csv_files ####

# Read in all of the data from "nfl.csv" into the nfl variable using the csv module.
import csv
nfl_file = open("nfl.csv",'r')
nfl = list(csv.reader(nfl_file))


#### Counting_how_many_times_a_team_won ####

patriots_wins = 0
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins = patriots_wins + 1
    else:
        print("Never Won")

print(patriots_wins)

#### Making_function_to_count_wins ####

def count_wins(team):
    count = int(0)
    for row in nfl:
        if row[2] == str(team):
            count = count + 1
    return count

cowboys_wins = count_wins("Dallas Cowboys")

#### Using_boolean_statements_with_the_AND_keyword ####

drugs = 1.5
money = 100

a = (drugs == 1.5 and money == 100) #True
b = (drugs == 1.6 and money == 100) #False

#### Using_boolean_statements_with_the_OR_keyword ####

go_brixton = "yes"

a = (go_brixton == "yes" or go_brixton == "no")  #True
b = (go_brixton == "no" or go_brixton == "def no") #False

#### Counting_wins_in_a_given_year ####

def nfl_wins(team,year):
    count = 0
    for row in nfl:
        # We need to ensure that we only increment the count when the row pertains to the year we want.
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins("Cleveland Browns","2010")
print(browns_2010_wins)


#### Counting_wins_by_year ####

def nfl_wins_by_year(team):
    win_dict = {}
    # Fill in code here to compute the wins for each year and store them in win_dict
    win_dict = {"2009":0, "2010":0, "2011":0, "2012":0, "2013":0}
    for row in nfl:
        if row[2] == team:
            win_dict[row[0]] = win_dict[row[0]] + 1
    return win_dict

dolphins_wins_by_year = nfl_wins_by_year("Miami Dolphins")
print(dolphins_wins_by_year)

#### Intro_to_classes ####

# What is a class? Think of a class as a blueprint. 
# It isn't something in itself, it simply describes how to make something. 
#You can create lots of objects from that blueprint - known technically as an instance.

class Team(object1):
    name = "Bears"
    def __init__(self,name):
        self.name = name

# So if we did this: 

b = Team("Cardinals")

# "Cardinals" is at position 0, which is actually at the same position as name in def __init__(self,name):
# which is now the same thing as:

b.name = "Cardinals"

#### Instance_methods ####

# Methods are just functions that are contained within a class
class Team():
    def __init__(self, name):
        self.name = name
    
    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:   #refers to the __init__ self.name = name
                count = count + 1
        return count

# Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
broncos = Team("Denver Broncos")  # insantiates the class "Denver Broncos"
broncos_wins = broncos.count_total_wins()  # calls the function and applies to the class.(i think)
print(broncos_wins)


#### Adding_to_the_init_funciton ####

import csv

# Add in code to read the csv nfl data to the __init__ method.
# Store the nfl data in the self.nfl instance property.
# Then convert the count_total_wins function to use the self.nfl property.
# Use the instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins.

class Team():
    def __init__(self, name):
        self.name = name
        nfl_file = open("nfl.csv",'r')
        self.nfl = list(csv.reader(nfl_file))

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team("Jacksonville Jaguars")
jaguars_wins = jaguars.count_total_wins()
print(jaguars_wins)


#### Wins_by_year_method ####

import csv
#Let's add the wins by year function that we created earlier to our class as a method.
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
        
    def wins_by_year(self):
        win_dict = {"2009":0, "2010":0, "2011":0, "2012":0, "2013":0}
        for row in self.nfl:
            if row[2] == self.name:
                win_dict[row[0]] = win_dict[row[0]] + 1
        return win_dict

jaguars = Team("Jacksonville Jaguars")
niners = Team("San Francisco 49ers")   #tried assigning this variable to 49ers but got errors.
niners_wins_by_year = niners.wins_by_year()
print(niners_wins_by_year)



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


#### Counting_wins_in_a_given_year ####

# Modify this function to also take a year as input, and returns the wins by the team in the year.

# Use the function to assign the number of wins by the "Cleveland Browns" in 2010 to browns_2010_wins.

# Use the function to assign the number of wins by the "Philadelphia Eagles" in 2011 to eagles_2011_wins.

def nfl_wins(team,year):
    count = 0
    for row in nfl:
        # We need to ensure that we only increment the count when the row pertains to the year we want.
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins("Cleveland Browns","2010")
print(browns_2010_wins)

eagles_2011_wins = nfl_wins("Philadelphia Eagles","2011")
print(eagles_2011_wins)

#### Counting_wins_by_year ####

# We'll need to create a new function to returns wins for each year.
# It will call nfl_wins_by_year as part of its computations.
def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

def nfl_wins_by_year(team):
    win_dict = {}
    # Fill in code here to compute the wins for each year and store them in win_dict
    win_dict = {"2009":0, "2010":0, "2011":0, "2012":0, "2013":0}
    for row in nfl:
        if row[2] == team:
            win_dict[row[0]] = win_dict[row[0]] + 1
    return win_dict
    
# Make a new function that calls on the nfl_wins_by_year function to compute wins for each year from 2009 - 2013.
# Valid years are "2009", "2010", "2011", "2012", and "2013".
# The function should return a dictionary with the years as keys, and the number of wins in each year as values.

dolphins_wins_by_year = nfl_wins_by_year("Miami Dolphins")
print(dolphins_wins_by_year)
chargers_wins_by_year = nfl_wins_by_year("San Diego Chargers")
print(chargers_wins_by_year)

#### Intro_to_classes ####

# Classes are a way to organize and structure code.
# We've already been using classes, they just haven't been presented as such.
# Strings in python are classes, and we can access class methods on them, such as .lower().
# Let's define a simple class.

# Classes are defined with the class keyword.
# Then a space, then the class name.
# The parentheses are used to denote which class this class inherits from.
# We'll get to inheritance later on -- it's a pretty deep topic.
class NFLTeam():
    # Classes can have class properties.
    # These properties can then be accessed later on.
    # Properties are just variables that are contained in a class.
    name = "Pittsburgh Steelers"

# After we define a class, we create an instance of it.
steelers = NFLTeam()

# We can access the class property.
print(steelers.name)

# The steelers variable is called an instance of the class.
# NFLTeam is the class.
# Because name is a class property, not an instance property, we can also access it directly.
print(NFLTeam.name)

# Make a class called Team.
# Give it a class property called name, with the value "Tampa Bay Buccaneers".
# Make an instance of the class, and assign it to the variable bucs.

class Team():
    name = "Tampa Bay Buccaneers"
    
bucs = Team()

#### The init method ####

class Team(object1):
	name = "Bears"

b = Team()
b.name = "Cardinals"

# Special class method on this Team, that will allow us to setup the name at the beginning. 
# The name will be set when we setup the Team.

# Whenever you do Team(), it's basically instantiating a new Team object.
# When you instantiate a new object it calls the init function in the class method.

class Team(object1):
	name = "Bears"
	def __init__(self):
		print("blah")

b = Team()
b.name = "Cardinals"

# So this init function is called when a new Team is created.

# Self is a reference to the class itself. called an instance method. this is run and applies to the instance of a class.

# In a Class, we have the definition of a class, the class itself and instances of that class. Instances are their own objects.

# Team is the higher level construct its the class. the bears or the cardinals are instances of this class.

# self is actually referencing b.

class Team(object1):
	name = "Bears"
	def __init__(self,name):
		self.name = name

# So if we did this: 

b = Team("Cardinals")

# "Cardinals" is at position 0, which is actually at the same position as name in def __init__(self,name):

# which is now the same thing as:

b.name = "Cardinals"


#### Initializing_a_class ####

# When we instantiate a class (create an instance of it), we have a chance to run a special function.
# It's called the __init__ function, and it runs every time a class is instantiated.
# We define functions inside our classes by indenting 4 spaces and then using the def keyword.

class Car():
    # The special __init__ function is run whenever a class is instantiated.
    # The init function can take arguments, but self is always the first one.
    # Self is a reference to the instance of the class.
    def __init__(self, car):
        # Using self before car means that car is an instance property.
        self.car = car

# When we instantiate the class, we pass in any arguments that the __init__ function needs.
# We skip the self argument.
accord = Car("Honda Accord")

# We set self.car in the __init__ function, but can print accord.car here.
# self is a reference to the instance of the class.
# It lets us interact with the class instance within the class.
print(accord.car)

# Instance properties are only available to instances, not to the classes.
# We couldn't print Car.car, for example.

class Team():
    name = "Tampa Bay Buccaneers"
    def __init__(self, name):
        self.name = name
    
    
bucs = Team("Tampa Bay Buccaneers")    

print(bucs.name)
    
# Modify the Team class so that name is an instance property.
# Make an instance of the class, passing in the value "Tampa Bay Buccaneers" to the __init__ function.
# Assign the instance to the variable bucs.

#### Instance_methods ####

# Classes can have methods. Once example is the .lower() method that turns a string into a lowercase version.

# Methods are just functions that are contained within a class.

# Here's an example of a method:
class Car():
	def __init__(self, miles_per_gallon):
		self.mpg = miles_per_gallon

	def get_gas_cost(self, miles):
		total_gas = self.mpg * miles
		return total_gas * 3.00


class Zoo():
    def __init__(self):
        self.animals = []

    # This is an instance method.
    # It can be invoked on any instance of this class.
    # Note that because it is an instance method, we still need to put in the self argument.
    def add_animal(self, animal):
        # This will add the animal to the list of animals that the instance is storing.
        self.animals.append(animal)

# We start with no animals.
san_diego_zoo = Zoo()
print(san_diego_zoo.animals)

# Then we get a panda!
san_diego_zoo.add_animal("panda")
print(san_diego_zoo.animals)

# The we get an orca!
san_diego_zoo.add_animal("orca")
print(san_diego_zoo.animals)

# Add a method called count_total_wins to the Team class.
# The method should take no arguments (except self), and should return the number of games the team won from 2009-2013.
# Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
# Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.

# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name
    
    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:   #refers to the __init__ self.name = name
                count = count + 1
        return count

broncos = Team("Denver Broncos")  # insantiates the cless "Denver Broncos"
broncos_wins = broncos.count_total_wins()  # calls the function and applies to the class.(i think)
print(broncos_wins)

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()
print(chiefs_wins)

#### Adding_to_the_init_funciton ####

import csv

# Add in code to read the csv nfl data to the __init__ method.
# Store the nfl data in the self.nfl instance property.
# Then convert the count_total_wins function to use the self.nfl property.
# Use the instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins.

class Team():
    def __init__(self, name):
        self.name = name
        nfl_file = open("nfl.csv",'r')
        self.nfl = list(csv.reader(nfl_file))

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team("Jacksonville Jaguars")
jaguars_wins = jaguars.count_total_wins()
print(jaguars_wins)

#We read in the nfl data to the nfl variable automatically before, but we've removed it.
#Add in code to read the csv nfl data to the __init__ method.
#Store the nfl data in the self.nfl instance property.
#Then convert the count_total_wins function to use the self.nfl property.
#Use the instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins.

#### Wins_by_year_method ####

import csv
#Let's add the wins by year function that we created earlier to our class as a method.
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
        
    def wins_by_year(self):
        win_dict = {"2009":0, "2010":0, "2011":0, "2012":0, "2013":0}
        for row in self.nfl:
            if row[2] == self.name:
                win_dict[row[0]] = win_dict[row[0]] + 1
        return win_dict

jaguars = Team("Jacksonville Jaguars")
niners = Team("San Francisco 49ers")   #tried assigning this variable to 49ers but got errors.
niners_wins_by_year = niners.wins_by_year()
print(niners_wins_by_year)

