## DataQuest_Weather_Patterns_20150122

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 3

# Basics: Count up how many times each type of weather occurs.

# Learn about dictionaries, the in statement, list slicing, and else statements while finding out how the weather in Los Angeles is.  

#####################################

Overview of Useful code:

Open, Read then parse the _file. (Parsing_the_file)
Getting a single column _from the data. (Getting_Second_column)
Dictonaries. (Dictonaries_basics)
Entering Keys _and Values into a dictionary. (Indexing_a_dictionary)
Creating a dictionary _with keys _and values. (Defining_a_dictionary)
The _in statement (List). (Testing_if_items_are_in_list)
The _in statement (Dictionary). (Testing_if_key_is_in_dictionary)
The _else statement. (The_else_statement)
Count up how many times each _type of weather occurs. (Counting_the_weather)

#####################################

#### SUMMARY OF USEFUL CODE ####


#### Parsing_the_file ####

f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
weather_data = []
for row in rows:
    split_rows = row.split(",")
    weather_data.append(split_rows)
print(weather_data)


#### Getting_Second_column ####

weather_column = []

for item in weather_data:
    value = item[1]
    weather_column.append(value)
print(weather_column)


#### Slicing_lists ####

## Removing the header
# The weather data is still loaded into the weather variable.

count = 0
for item in weather:
    count = count + 1 
print(count)

new_weather = weather[1:367]
print(new_weather)


#### Dictonaries_basics ####

# We can make a dictionary with curly braces.
dictionary_one = {}

# The we can add keys and values.
dictionary_one["key_one"] = 2
print(dictionary_one)


#### Indexing_a_dictionary ####

# We can index dictionaries with square brackets.
# a = dictionary[10] will get the value stored in the dictionary for the key 10 and assign it to a.

dictionary_one = {}
dictionary_one["test"] = 10
dictionary_one["key"] = "fly"


#### Defining_a_dictionary ####

# We can define dictionaries that already contain values.
# All we do is add in keys and values separated by colons.
# We have to separate pairs of keys and values with commas.
a = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}


#### Testing_if_items_are_in_list ####

# We can check if values are in lists using the in statement.
the_list = [10,60,-5,8]

# This is True because 10 is in the_list
print(10 in the_list)


#### Testing_if_key_is_in_dictionary ####

# We can check if a key is in a dictionary with the in statement.
the_dict = {"robin": "red", "cardinal": "red", "oriole": "orange", "lark": "blue"}

# This is True
print("robin" in the_dict)

#### The_else_statement ####

# The code in an else statement will be executed if the if statement boolean is False.

a = 8
b = 10
if a == 7:
    print(a)
else:
    print(b)


#### Count_how_many_times_items_appear_in_a_list_using_dictionaries ####

# We can count how many times items appear in a list using dictionaries.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

# Create an empty dictionary
pantry_counts = {}
# Loop through the whole list
for item in pantry:
    # If the list item is already a key in the dictionary, then add 1 to the value of that key.
    # This is because we've seen the item again, so our count goes up.
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        # We set the value to 1 because we are seeing the item, so it's occured once already in the list.
        pantry_counts[item] = 1
print(pantry_counts)


#### Counting_the_weather ####

# Our weather column, minus the header, is assigned to the weather variable.
weather_counts = {}

# The weather column, minus the header, has been loaded into the weather variable.
# Count up how many times each type of weather occurs.
# Store the counts in weather_counts.

print(weather)
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1
print(weather_counts)

# Rem: dictionary[key] = value


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#### Parsing_the_file ####

# Let's parse the data from the last mission as an example.
# First, we open the wait times file from the last mission.
f = open("crime_rates.csv", 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

# This data has a header, so I can't make the day a int until that is dealt with.

f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
weather_data = []
for row in rows:
    split_rows = row.split(",")
    weather_data.append(split_rows)
print(weather_data)

#### Getting_Second_column ####

# The "days" column in our data isn't extremely useful for our task, so we need to just grab the second column, with the weather.
# We looped over lists before, and this is how we will extract the second column.
lolist = [[1,2],[3,4],[5,6],[7,8]]
second_column = []
for item in lolist:
    # Each item in lolist is a list.
    # We can get just the second column value by indexing the item.
    value = item[1]
    second_column.append(value)

# second_column is now a list containing only values from the second column of lolist.
print(second_column)

# Let's read in our weather data again.
weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)

# Get all of the values in the second column and append them to weather_column.

weather_column = []

for item in weather_data:
    value = item[1]
    weather_column.append(value)
print(weather_column)

#### Predefined_vaiables ####

# In order to make it easier to use the weather column that we just parsed, we're going to automatically include it from now on.
# If you look in the variables panel, you'll see the "weather" variable exists, even though we didn't define it in the code.
# It's been specially added before our code runs.
# We can interact with it normally -- it's a list.
print(weather[0])

count = 0

# Loop over the weather variable, and set count equal to the number of items in weather.

for item in weather:
    count = count + 1
print(count)

#### Slicing_lists ####

# Dealing with the header, the header describes what is happening in those columns.
# We will want to get rid of the header when we count the number of items.
# list slicing. is a way to index lists.
a = [5,10,6,8]
a[0] == 5 #True
a[0:2] == [5,10]
# Upto to and not including the second item.

## Let's practice with some list slicing.

a = [4,5,6,7,8]
# New list containing index 2 and 3.
print(a[2:4])
# New list with no elements.
print(a[2:2])
# New list containing only index 2.
print(a[2:3])

slice_me = [7,6,4,5,6]

#index 2 and 3
slice1 = slice_me[2:4]
print(slice1)

#index 1
slice2 = slice_me[1:2]
print(slice2)

#index 3 and 4
slice3 = slice_me[3:5]
print(slice3)

## Remove the header

# The weather data is still loaded into the weather variable.

count = 0
for item in weather:
    count = count + 1 
print(count)

new_weather = weather[1:367]
print(new_weather)

########################################################################################################################

#### Dictonaries_basics ####

dictionary_has_curly_braces = {key,value}

# To store data in a dict,
# Use curly braces to define a dictionary
# Then you add the keys
a = {}
a["Tom"] = 10
a["Bob"] = 2
a["Julie"] = 8

print(a["Tom"])
>>> 10

# We can make a dictionary with curly braces.
dictionary_one = {}

# The we can add keys and values.
dictionary_one["key_one"] = 2
print(dictionary_one)

# Keys and values can be anything.
# And dictionaries can have multiple keys
dictionary_one[10] = 5
dictionary_one[5.2] = "hello"
print(dictionary_one)

dictionary_two = {}

dictionary_two["test"] = 5
dictionary_two[10] = "hello"

print(dictionary_two)

#### Indexing_a_dictionary ####

# We can index dictionaries with square brackets.
# a = dictionary[10] will get the value stored in the dictionary for the key 10 and assign it to a.

dictionary_one = {}
dictionary_one["test"] = 10
dictionary_one["key"] = "fly"

# We can retrieve values from dictionaries with square brackets.
print(dictionary_one["test"])
print(dictionary_one["key"])

dictionary_two = {}
dictionary_two["key1"] = "high"
dictionary_two["key2"] = 10
dictionary_two["key3"] = 5.6

# Assign the value in "key1" in dictionary_two to a.

a = dictionary_two["key1"]
b = dictionary_two["key2"]
c = dictionary_two["key3"]

print(a,b,c)

#### Defining_a_dictionary ####

# We can define dictionaries that already contain values.
# All we do is add in keys and values separated by colons.
# We have to separate pairs of keys and values with commas.
a = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}

# a is initialized with those keys and values, so we can access them.
print(a["key1"])

# Another example
b = {4: "robin", 5: "bluebird", 6: "sparrow"}
print(b[4])

# Make a dictionary c with the keys 7, 8, and 9 corresponding to the values "raven", "goose", and "duck".
# Make a dictionary d with the keys "morning", "afternoon", "evening", and "night" corresponding to the values 9, 14, 19, and 23.

c = {7:"raven",8:"goose",9:"duck"}
d = {"morning":9,"afternoon":14,"evening":19,"night":23}

print(c[7])
print(d["morning"])

#### The_in_statement ####

# "In" is a way for us to check whether a item is in a list, returning a boolean.

b = ["test","s2","and"]


#### Testing_if_items_are_in_list ####

# We can check if values are in lists using the in statement.
the_list = [10,60,-5,8]

# This is True because 10 is in the_list
print(10 in the_list)

# This is True because -5 is in the_list
print(-5 in the_list)

# This is False because 9 isn't in the_list
print(9 in the_list)

# We can assign the results of an in statement to a variable.
# Just like any other boolean.
a = 7 in the_list

list2 = [8, 5.6, 70, 800]

c = 9 in list2
d = 8 in list2
e = -1 in list2


#### Testing_if_key_is_in_dictionary ####

# We can check if a key is in a dictionary with the in statement.
the_dict = {"robin": "red", "cardinal": "red", "oriole": "orange", "lark": "blue"}

# This is True
print("robin" in the_dict)

# This is False
print("crow" in the_dict)

# We can also assign the boolean to a variable
a = "cardinal" in the_dict
print(a)

dict2 = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

#Check whether "jupiter" is in dict2 and assign the result to b.
#Check whether "earth" is in dict2 and assign the result to c.

b = "jupiter" in dict2
c = "earth" in dict2

print(b)
print(c)

#### The_else_statement ####

a = 8
b = 10
if a == 7:
    print(a)
else:
    print(b)

# The code in an else statement will be executed if the if statement boolean is False.
# This will print "Not 7!"
a = 6
# a doesn't equal 7, so this is False.
if a == 7:
    print(a)
else:
    print("Not 7!")

# This will print "Nintendo is the best!"
video_game = "Mario"
# video_game is "Mario", so this is True
if video_game == "Mario":
    print("Nintendo is the best!")
else:
    print("Sony is the best!")

season = "Spring"

if season == "Summer":
    print("It's hot!")
else:
    print("It might be hot!")

###############################################################################################################

#### Count_how_many_times_items_appear_in_a_list_using_dictionaries ####

# We can count how many times items appear in a list using dictionaries.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

# Create an empty dictionary
pantry_counts = {}
# Loop through the whole list
for item in pantry:
    # If the list item is already a key in the dictionary, then add 1 to the value of that key.
    # This is because we've seen the item again, so our count goes up.
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        # We set the value to 1 because we are seeing the item, so it's occured once already in the list.
        pantry_counts[item] = 1
print(pantry_counts)

us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]

us_president_counts = {}

for item in us_presidents:
    if item in us_president_counts:
        us_president_counts[item] = us_president_counts[item] + 1
    else:
        us_president_counts[item] = 1
print(us_president_counts)

#### Counting_the_weather ####

# Our weather column, minus the header, is assigned to the weather variable.
weather_counts = {}

# The weather column, minus the header, has been loaded into the weather variable.
# Count up how many times each type of weather occurs.
# Store the counts in weather_counts.

print(weather)
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1
print(weather_counts)

# Rem: dictionary[key] = value




