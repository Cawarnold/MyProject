## DataQuest_Weather_Patterns_20150122

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Basics: Find the US city with the lowest crime rate

#####################################

Overview of Useful code:

Open, Read then parse the _file. (Parsing_the_file)
Getting a single column _from the data. (Getting_Second_column)
Dictonaries. (Dictonaries_basics)



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













