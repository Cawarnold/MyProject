## DataQuest_Name_of_US_Congresspersons_20150202

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 6

# Basics: What should you name your kid if you want them to be a US Congressperson?

# Learn about the enumerate function, list comprehensions, try/except blocks, and the None type while finding the most common names for US Congressman/Congresswomen.

#####################################

Overview of Useful code:
Get _all unique values _in a column. (Find_the_different_genders)
Replacing values _in a column. (Replacing_genders)
String split on '-'. (Parsing_birth_years)
Enumerate _is a _for loop counter. (Create_a_birthyear_column_with_Enumerate)
Use Try Except when a function may _not work.(Practice_with_try_except)
The _pass keyword enables us to end a function _or skip code. (The_pass_keyword)
Using _try _except to convert strings to integers. (Convert_birth_years_to_integers)
Using _for loops, _if _and statements, _if _in statements. (Counting_up_the_female_names)
The _None _type _and how to use it. (Practicing_with_the_None_type)
Using the _None _type to find _max value. (Finding_how_many_times_the_top_female_names_occur)
Using .items method to get keys _and values _from a dictionary. (Practice_with_the_items_method)
Use _all above to find male names that occur the most. (Finding_the_male_names_that_occur_the_most)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Find_the_different_genders ####

# A set is a data type, just like a list, but it only contains each value once.
genders_list = []
unique_genders = set()
unique_genders_list = []

for row in legislators:
    genders_list.append(row[3])
    
unique_genders = set(genders_list)
unique_genders_list = list(unique_genders)
print(unique_genders_list)

# unique_genders_list is now a list of unique genders.

#### Replacing_genders ####

# Loop through the rows in legislators and replace any gender values of "" with "M".
for row in legislators:
    if row[3] == "":
        row[3] = "M"

#### Parsing_birth_years ####

birth_years = []

for row in legislators:
    birth_years.append((row[2]).split('-')[0]) 
 
#Takes second element of each list in legislators, splits this string by '-'. 
#There are three of these elements. We want the one at index 0.
#Which we then append to our birthyears list.
    
print(birth_years)

#### Create_a_birthyear_column_with_Enumerate ####

# The enumerate() function adds a counter to an iterable. enumerate() starts counting at 0.
for i, row in enumerate(legislators):
    row.append(birth_years[i])
print(legislators)

## Same as -- which I did all by myself :)
for row in legislators:
    row.append((row[2]).split('-')[0])
    
print(legislators)

#### Practice_with_list_compehensions ####

# Define a list of lists
data = [["tiger", 2], ["duck", 10], ["cardinal", 4]]

# Extract the first column from the list
first_column = [row[0] for row in data]
# Double the number of animals.
double_numbers = [row[1]*2 for row in data]


#### Practice_with_try_except ####

invalid_int = ""         # Cannot be parsed into an int with the int() function.
valid_int = "10"         # Can be parsed into an int.

# Parse the valid int
try:
    valid_int = int(valid_int)
except Exception:        # This code is never run, because there is no error parsing valid_int into an integer.
    valid_int = 0

# Try to parse the invalid int
try:
    invalid_int = int(invalid_int)
except Exception:        # The parsing fails, so we end up here.
    invalid_int = 0      # The code here will be run, and will assign 0 to invalid_int.


#### The_pass_keyword ####

# We can use the pass keyword inside the body of any statement that ends with a colon.
valid_int = "10"
try:                                    # Use a try/except block to parse valid_int into an integer.
    valid_int = int(valid_int)
except Exception:
    pass                                # Use the pass keyword inside the except block.

#### Convert_birth_years_to_integers ####

# Loop over the rows in legislators, and convert the values in the birth year column to integers.
# In cases where parsing fails, assign 0 as the value.

for row in legislators:
    try:
        row[7] = int(row[7])
    except:
        row[7] = 0
    print(row[7])

#### Counting_up_the_female_names ####

# Count up how many times each female name occurs in legislators. 
# First name is the second column.
# You'll need to make sure that gender (fourth column) equals "F", 
# and that birth year (eighth column) is greater than 1940.
# Store the first name key and the counts in the female_name_counts dictionary.
# You'll need to use nested if statements to first check if gender and birth year are valid, 
# and then to check if the first name is in female_name_counts.

female_name_counts = {}
male_name_counts = {}
for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        if row[1] in female_name_counts:
            female_name_counts[row[1]] = female_name_counts[row[1]] + 1
        else:
            female_name_counts[row[1]] = 1
    if row[3] == "M" and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] = male_name_counts[row[1]] + 1
        else:
            male_name_counts[row[1]] = 1

print(female_name_counts)
print(male_name_counts)

#### Practicing_with_the_None_type ####

c = None
d = "Bamboo"
c_none = c is None    #True
d_none = d is None    #False

#### Finding_how_many_times_the_top_female_names_occur ####

max_value = None

for item in female_name_counts:
    if max_value is None or female_name_counts[item] > max_value:
        max_value = female_name_counts[item]
print(max_value)

#### Practice_with_the_items_method ####

# The .items method lets us access a dictionary key and value in a loop.
for key,value in plant_types.items():
    print(key)               #key
    print(value)             #value
    print(plant_types[key])  #value

#### Finding_the_male_names_that_occur_the_most ####

top_male_names = []

male_name_counts = {}
def count_occurances(list_of_legislators):
    for row in list_of_legislators:
        if row[3] == "M" and row[7] > 1940:
            if row[1] in male_name_counts:
                male_name_counts[row[1]] = male_name_counts[row[1]] + 1
            else:
                male_name_counts[row[1]] = 1

# define function - count_occurances.
# for each item(row) in the list of (list_of_legislators).
# if gender is male and date is bigger than 1940
# if the first name is in dictionary (male_name_counts)
# then add 1 to count of that name
# else create dictionary key with item(row) first name and value = 1

count_occurances(legislators)
#print(male_name_counts)

max_val = None
for key,value in male_name_counts.items():
    if max_val is None or value > max_val:
        max_val = value
        print(key)
        print(value)
#print(max_val)

for key,value in male_name_counts.items():
    if value == 35:
        top_male_names.append(key)
#print(top_male_names)


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# Data:
# last, first, birthday, gender, type, state, party
# contains data from the very beginning of the US senate.

# eg. Bassett, Richard, 1745-04-02, M, Sen(or Rep), DE, Anti-Admin
# data is not complete. some do not have gender/ party / birthday 
# all have last, first names, type and state.

#### Find_the_different_genders ####

# We've conveniently read in the csv data for you, and it's stored in the legislators variable.
# There's an invalid value in the gender column that isn't "M" or "F".
# Our first task is going to be getting rid of the invalid values and assigning the right gender.
# In order to do that, we first need to figure out what all of the unique values in the "gender" column are.
# The value that isn't "M" or "F" will be the invalid value, and we need to replace it.

## Get all unique values in a column.

# We can use the set() function to convert lists into sets.
# Sets: Unordered collections of unique elements.
# A set is a data type, just like a list, but it only contains each value once.
car_makers = ["Ford", "Volvo", "Audi", "Ford", "Volvo"]

# Volvo and ford are duplicates
print(car_makers)

# Converting to a set
unique_car_makers = set(car_makers)
print(unique_car_makers)

# We can't index sets, so we need to convert back into a list first.
unique_cars_list = list(unique_car_makers)
print(unique_cars_list[0])

genders_list = []
unique_genders = set()
unique_genders_list = []

# Loop through the rows in legislators, and extract the gender column (fourth column)
# Append the genders to genders_list.
# Then turn genders_list into a set, and assign it to unique_genders
# Finally, convert unique_genders back into a list, and assign it to unique_genders_list.

for row in legislators:
    genders_list.append(row[3])
    
unique_genders = set(genders_list)
unique_genders_list = list(unique_genders)
print(unique_genders_list)

#### Replacing_genders ####

# Now we know that the invalid gender value is and empty string -- "".
# Sadly, most US Congresspeople (and all prior to 1917) have been male.
# Because it's going to make this exercise easier, we'll just assume that anyone with a missing gender is Male.
# At some point later on, we'll be able to predict whether a name is male or female, and we'lll revisit this exercise.

# We can replace values in a list with a for loop.
# All of the 0 values in the first column here will be replaced with a 5.
lolists = [[0,5,10], [5,20,30], [0,70,80]]
for row in lolists:
    if row[0] == 0:
        row[0] = 5

# We can see the new list.
print(lolists)

# Loop through the rows in legislators and replace any gender values of "" with "M".

for row in legislators:
    if row[3] == "":
        row[3] = "M"

print(legislators)

#### Parsing_birth_years ####

# We want to find out what names are most common for senators, but we also want to be able to filter on date if we want to.
# Naming someone Effingham was somewhat popular in the 1820's, but may not fly in the modern era.
# So we need some way to determine if a Senator was born recently, and we need a way to only select those names if we want to.
# We have a birthday column, so we should just be able to parse them out.
# Birthdays are stored in the "year-month-day" format, such as "1820-05-02".
# We should be able to split the birthday on "-", and grab the first part (the year).

birth_years = []

# Loop through the rows in legislators
# Inside the loop, get the birthday column from the row, and split the birthday.
# After splitting the birthday, get the birth year, and append it to birth_years
# At the end, birth_years will contain the birth years of all the Congresspeople in the data.

for row in legislators:
    birth_years.append((row[2]).split('-')[0]) 
 
#Takes second element of each list in legislators, splits this string by '-'. 
#There are three of these elements. We want the one at index 0.
#Which we then append to our birthyears list.
    
print(birth_years)

#### Enumerate function ####

# We're used to doing for loops like this:
a = [1,5,8]
for i in a:
	print(i)
>1
>5
>8

# What if we have two lists.
a = [1,5,8]
b = [2,10,15]
# And we want to loop through a and print out each element of a and the corresponding element of b.
#Enumerate lets you have 2 values in your for loop. the first is actually a counter.

for i,e in enumerate(a):
	print(e)
	print(i)

# for i (index - the counter),e (the normal item in a for loop) in enumerate(a):

# so first loop will print e = 1 and i = 0.
# second loop will print e = 5 and i = 1.
# thrid loop will print e = 8 and i = 2.

for i,e in enumerate(a):
	print(e)
	print(b[i])

> 1
> 2
> 5
> 10
> 8
> 15
for i,e in enumerate(a):
	print(e)
	print(b[i])
	print(a[i])

# Values e and a[i] would equal the same value.

#### Practice_with_enumerate ####

dogs = ["labrador", "poodle", "collie"]
cats = ["siamese", "persian", "somali"]

# Enumerate the dogs list, and print the values.
for i, dog in enumerate(dogs):
    # Will print the dog at the current loop iteration.
    print(dog)
    # This will equal dog.  Prints the dog at index i.
    print(dogs[i])
    # Print the cat at index i.
    print(cats[i])

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

# Use a for loop to enumerate the ships list.
# In the body of the loop, print the ship at the current index, then the car at the current index.
# Make sure you have two separate print statements.

for i, ship in enumerate(ships):
    print(ship)
    print(ships[i])
    print(cars[i])

#### Create_a_birthyear_column_with_Enumerate ####

# Now, let's add the birth years column into our data as column 8.
# We can do this by looping through the data and adding to the row.
# We can use the enumerate function to help us out.

lolists = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, row in enumerate(lolists):
    row.append(trees[i])

# Our list now has a new column containing the values from trees.
print(lolists)

# Legislators and birth_years have both been loaded in.

# Loop through the rows in legislators list, 
# and append the corresponding value in birth_years to each row.

for i, row in enumerate(legislators):
    row.append(birth_years[i])
    
print(legislators)


## Same as -- which I did all by myself :)

for row in legislators:
    row.append((row[2]).split('-')[0])
    
print(legislators)


#### List comprehension ####

l = [[1,5,8],[3,5,7],[8,10,12]]

# what we would have done.
col = []
for row in l:
	col.append(row[0])

> col = [1,3,8]

# Or we could have done

col = [row[0] for row in l]
> col = [1,3,8]

## Another example:

a = [7,10,20]
a_2 = [i*2 for i in a]

> a_2 = [14,20,40]


#### Practice_with_list_compehensions ####

# Define a list of lists
data = [["tiger", "lion"], ["duck", "goose"], ["cardinal", "bluebird"]]

# Extract the first column from the list
first_column = [row[0] for row in data]

apple_price = [100, 101, 102, 105]

# Double all of the prices in apple_price, 
# and assign the resulting list to apple_price_doubled.

apple_price_doubled = [i*2 for i in apple_price]

# Subtract 100 from all of the prices in apple_price, 
# and assign the resulting list to apple_price_lowered.

apple_price_lowered = [i-100 for i in apple_price]

#### Convert_failed_birth_years_to_integers ####

# We want to find the most common Senator names after a certain date -- let's say 1940.
# Remember that the birth years are now the last column in the legislators data.
# There's one problem -- the birth years are stored as strings, 
# but we need them to be integers so we can use booleans to pick only the ones that are greater than 1940.
# We can't use booleans to compare a string value to the integer 1940 -- the comparison wouldn't make any sense.
# Luckily, we can convert strings to ints using the int() function.

for row in legislators:
    row[7] = int(row[7])

# Hmm, but the above code fails.
# It fails because there is a value in the column that can't be converted to an int.
# Remember how some genders were missing?  It also looks like some birthdays were missing, which is giving us invalid values in the birth years column.

# We're stuck for now, but we'll learn a concept next that will help us out.

# Just hit "Run" to move on for now.

#### Try/Except statements ####

# we found errors in this statement
for row in legislators:
    row[7] = int(row[7])

# so we can use a try/except statement
for row in legislators:
	try:
		row[7] = int(row[7])
	except:
		row[7] = 0

# if what is in row[7] can be converted into an int, then it will be. if not then it'll get a 0.


#### Practice_with_try_except ####

# Cannot be parsed into an int with the int() function.
invalid_int = ""

# Can be parsed into an int.
valid_int = "10"

# Parse the valid int
try:
    valid_int = int(valid_int)
except Exception:
    # This code is never run, because there is no error parsing valid_int into an integer.
    valid_int = 0

# Try to parse the invalid int
try:
    invalid_int = int(invalid_int)
except Exception:
    # The parsing fails, so we end up here.
    # The code here will be run, and will assign 0 to invalid_int.
    invalid_int = 0

print(valid_int)
print(invalid_int)

another_invalid_int = "Oregon"
another_valid_int = "1000"

try:
    another_invalid_int = int(another_invalid_int)
except Exception:
    another_invalid_int = 0
    
try:
    another_valid_int = int(another_valid_int)
except Exception:
    another_valid_int = 0


#### The_pass_keyword ####

# The pass keyword enables us to skip adding code into the body of a statement when we don't want to.

valid_int="5"
try:
    valid_int=int(valid_int)
except Exception:

# The code above will fail, because whenever we have a colon in Python, 
# we are saying that we will have a line or lines below it, indented 4 spaces.

# We can't have zero lines inside the body of any statement ending with a colon 
# (for loop, function definition, if statement, and so on). 
# Comments don't count as lines for this purpose.

# But sometimes, such as with the except statement above, we really don't want to do anything in the body.

# This is where the pass keyword comes in handy.

valid_int="5"
try:
    valid_int=int(valid_int)
except Exception:
    pass

# The code above will work, because the pass keyword is a line in the body of the except statement.

# However, pass is a special keyword that tells Python to do nothing and keep going.

invalid_int = ""
try:
    # This parsing will fail
    invalid_int = int(invalid_int)
except Exception:
    # Nothing will happen in the body of the except statement, because we are passing.
    pass

# invalid_int still has the same value.
print(invalid_int)

# We can also use the pass statement with for loops.
# (although it's less useful in this example)
a = [1,4,5]
for i in a:
    pass

# And if statements.
if 10 > 5:
    pass

# We can use the pass keyword inside the body of any statement that ends with a colon.
valid_int = "10"

# Use a try/except block to parse valid_int into an integer.
# Use the pass keyword inside the except block.

try:
    valid_int = int(valid_int)
except Exception:
    pass

#### Convert_birth_years_to_integers ####

# The legislators variable has been loaded.

# Now that we know about the try/except statements, we can convert the birth year column (column 8) to integers.
# Loop over the rows in legislators, and convert the values in the birth year column to integers.
# In cases where parsing fails, assign 0 as the value.

for row in legislators:
    try:
        row[7] = int(row[7])
    except:
        row[7] = 0
    print(row[7])

#### Fill_in_years_without_a_value ####

# Great, we're very close to being able to find the most common name!
# The final hurdle is dealing with the cases where the birth years are 0
# We'll need to fill these in to make our results more accurate.
# The rows in legislators are listed in rough chronological order, 
# so we can fill in birth years that are 0 with the birth year of the previous row.
# This isn't perfect, but we don't have a much better way of going about this.

data = [[1,1],[0,5],[10,7]]
last_value = 0

# There are some holes in this code -- it won't work properly if the first birth year is 0, for example, but its fine for now.
# It keeps track of the last value in the column in the last_value variable.
# If it finds an item that equals 0, it replaces the value with the last value.
for row in data:
    # Check if the item is 0.
    if row[0] == 0:
        # If it is, replace it with the last value.
        row[0] = last_value
    # Set last value equal to the item -- we need to do this in order to keep track of what the previous value was, so we can use it for replacement.
    last_value = row[0]

# The 0 value in the second row, first column has been replaced with a 1.
print(data)

# Loop through legislators, and replace any values in the birth_year column that are 0 with the previous value.

for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]

#### Counting_up_the_female_names ####

# We now know enough to count up the most popular names!
# We'll start with female names, and then do male names next.
# Only names from congresspeople born after 1940 will be counted.
# We'll be counting using a dictionary -- we've done this before, but a quick refresher is to the right.

names = ["Jim", "Bob", "Bob", "JimBob", "Joe", "Jim"]
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] = name_counts[name] + 1
    else:
        name_counts[name] = 1

female_name_counts = {}

# Count up how many times each female name occurs in legislators. 
# First name is the second column.
# You'll need to make sure that gender (fourth column) equals "F", 
# and that birth year (eighth column) is greater than 1940.
# Store the first name key and the counts in the female_name_counts dictionary.
# You'll need to use nested if statements to first check if gender and birth year are valid, 
# and then to check if the first name is in female_name_counts.

female_name_counts = {}
male_name_counts = {}
for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        if row[1] in female_name_counts:
            female_name_counts[row[1]] = female_name_counts[row[1]] + 1
        else:
            female_name_counts[row[1]] = 1
    if row[3] == "M" and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] = male_name_counts[row[1]] + 1
        else:
            male_name_counts[row[1]] = 1

print(female_name_counts)
print(male_name_counts)


#### The_None_type ####

# Trying to find the max item in a list.
l = [50,80,100]
max_value = 0
for i in l:
    if i > max_value:
        max_value = i

# what if
l = [-50,-80,-100]
max_value = 0
for i in l:
    if i > max_value:
        max_value = i
#the it doesn't work.

# just like string, integer types of values. NONE is a type of value.

# here, we want it to mean no "value". it's kind of like True of False. it has a special meaning.

# If we want to check if 
a = 7
# we would do 
a is None
# rather than 
a == None

# is catches more cases. 

data = [-50,-80,-100] 
max_val = None
for i in data:
    if max_val is None or i > max_val:
        max_val = i
# the first time through the loop will set the max_val = -50.
# first time through -- if max val is none, which it is, so jumps to set max_val = i
# second time throught the loop max_val is None False, then is max_val > -50? False so do nothing.
# so at the end we get max_val = -50 which is correct.

# None, be careful to use is
# careful to use checks for None first.
# if true then the other clause is skipped.
# if we didnt use the check for none first then the i > Max_val would give an error.

#### Practicing_with_the_None_type ####

# Set a variable equal to the None type
a = None
# A normal variable
b = 1

# This is True
print(a is None)
# And this is False
print(b is None)

# a is of the None type
print(type(a))

# Assigns whether a equals None to a_none
a_none = a is None
# Evaluates to True
print(a_none)

c = None
d = "Bamboo"

# Check whether c equals None, and assign the result to c_none.
# Check whether d equals None, and assign the result to d_none.

c_none = c is None
d_none = d is None

#### Finding_maximums_with_the_none_type ####

# We know how to find the maximum value in a list or dictionary.

max_val = 0
data = [50,80,100,0,40]
for i in data:
    if i > max_val
    max_val = i
print(max_val)

# The code above will find the maximum value in the data.
# But we have to initialize max_val first to a number.

max_val = 0
data = [-10, -20, -50, -100]
for i in data:
    if i > max_val
    max_val = i
print(max_val)

# In the above example, we would get an incorrect final value for max_val, 
# because we didn't set the initial value well (0 is greater than any value in data, so it's never changed.)

# Luckily, the None type to help us out.

max_val = None
data = [-10, -20, -50, -100]
for i in data:
    # If max_val equals None, or i is greater than max_val, then set max_val equal to i.
    # This ensures that no matter how small the values in data are, max_val will always get changed to a value in the list.
    # If you are checking if a value equals None and you are using it with AND or OR, then the None check always needs to come first.
    if max_val is None or i > max_val:
        max_val = i

min_val = None
income = [100,700,100,50,100,40,56,31,765,1200,1400,32,6412,987]

# Use a for loop to set min_val equal to the smallest value in income.

for item in income:
    if min_val is None or item < min_val:
        min_val = item
        
print(min_val)

#### Finding_how_many_times_the_top_female_names_occur ####

# We now have a dictionary where the keys are first names, 
# and the values are counts of how many times female congresspeople born after 1940 had that name.
# We need to go from here to a name or names that are the most popular.
# First, let's find out the highest value (how many times the most-occuring name occurred).
# This will let us extract the name or names that occurred the most.

# female_name_counts has been loaded in.
max_value = None

# Loop through the keys in female_name_counts, and get the value associated with the key.
# Assign the value to max_value if it is larger, or if max_value is None.
# At the end of the loop, max_value will be the largest value in the dictionary.


print(female_name_counts)            # prints out dictionary

for item in female_name_counts:
    print(item)                      # prints out the key
    print(female_name_counts[item])  # prints out the value

for item in female_name_counts:
    if max_value is None or female_name_counts[item] > max_value:
        max_value = female_name_counts[item]
print(max_value)

#### Finding_the_female_names_that_occur_the_most ####

# So we now know that the names that occur the most occur 2 times.

# All we have to do now is loop through the dictionary again and extract all the names that occur twice.

# female_name_counts has been loaded in.
top_female_names = []

# Loop through the keys in female_name_counts.
# If any value equals 2, append the key to top_female_names.
# At the end, top_female_names will be a list of the most occurring female congressperson names.

for item in female_name_counts:
    if female_name_counts[item] == 2:
        top_female_names.append(item)
print(top_female_names)   

#### The items method on dictionary ####

letters = {"a":"letter",5: "not","b":"letter"}

for k in letters:
    print(k)            #keys
    print(letters[k])   #values

# the .items method lets us do this.

for k,v in letter.items():
    print(k)            #keys
    print(v)            #values

#### Practice_with_the_items_method ####

animal_types = {"robin": "bird", "pug": "dog", "osprey": "bird"}

# The .items method lets us access a dictionary key and value in a loop.
for key,value in animal_types.items():
    print(key)
    print(value)
    # This is equal to the value
    print(animal_types[key])

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

# Use the .items() method along with a for loop to loop through plant_types.
# Inside the loop, print the key, and then the value.

for key,value in plant_types.items():
    print(key)               #key
    print(value)             #value
    print(plant_types[key])  #value


#### Finding_the_male_names_that_occur_the_most ####

# Let's follow the same process we did with the 
# female names to find a list of the most common male names.

# The .items() method may make the task quicker.

###

# legislators has been loaded in.

# Loop through legislators, and count up occurances for each name 
# where the gender column equals "M" and the birth year is after 1940 occurs. 
# Store the results in a dictionary.

# Then find the highest value in that dictionary.

# Finally, loop through the dictionary and 
# append any keys where the value equals the highest value to top_male_names.

#Cleaning: append (integer) date to the end of each list.
for row in legislators:
    row.append(int((row[2]).split('-')[0]))

#Check how to build dictionary
bob_name_counts = {}
bob_name_counts["bob"] = 1
print(bob_name_counts)

###

## Trial on max_val

def find_max(dict_of_names):
    max_val = None
    print(max_val)
    for key,value in dict_of_names.items():
        if max_val is None or value > max_val:
            max_val = value

find_max(male_name_counts)
print(max_val)

#but this works...

max_val = None
for key,value in male_name_counts.items():
    if max_val is None or value > max_val:
        max_val = value
        print(key)
        print(value)


#### And the answer is...


top_male_names = []

# print(legislators)

male_name_counts = {}
def count_occurances(list_of_legislators):
    for row in list_of_legislators:
        if row[3] == "M" and row[7] > 1940:
            if row[1] in male_name_counts:
                male_name_counts[row[1]] = male_name_counts[row[1]] + 1
            else:
                male_name_counts[row[1]] = 1

# define function - count_occurances.
# for each item(row) in the list of (list_of_legislators).
# if gender is male and date is bigger than 1940
# if the first name is in dictionary (male_name_counts)
# then add 1 to count of that name
# else create dictionary key with item(row) first name and value = 1

count_occurances(legislators)
#print(male_name_counts)

max_val = None
for key,value in male_name_counts.items():
    if max_val is None or value > max_val:
        max_val = value
        print(key)
        print(value)
print(max_val)

for key,value in male_name_counts.items():
    if value == 35:
        top_male_names.append(key)
print(top_male_names)


#### Def_find_names_with_max_count ####


top_male_names = []

# print(legislators)

male_name_counts = {}
def count_occurances(list_of_legislators):
    for row in list_of_legislators:
        if row[3] == "M" and row[7] > 1940:
            if row[1] in male_name_counts:
                male_name_counts[row[1]] = male_name_counts[row[1]] + 1
            else:
                male_name_counts[row[1]] = 1
    return male_name_counts

# define function - count_occurances.
# for each item(row) in the list of (list_of_legislators).
# if gender is male and date is bigger than 1940
# if the first name is in dictionary (male_name_counts)
# then add 1 to count of that name
# else create dictionary key with item(row) first name and value = 1

count_occurances(legislators)
#print(male_name_counts)


def find_max(dict_of_names_counts):
    max_val = None
    for key,value in dict_of_names_counts.items():
        if max_val is None or value > max_val:
            max_val = value
    print(max_val)

find_max(male_name_counts)


for key,value in male_name_counts.items():
    if value == 35:
        top_male_names.append(key)
print(top_male_names)
