## DataQuest_Name_of_US_Congresspersons_20150202

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Basics: What should you name your kid if you want them to be a US Congressperson?

# Learn about the enumerate function, list comprehensions, try/except blocks, and the None type while finding the most common names for US Congressman/Congresswomen.

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####




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

#### Create_a_birthyear_column ####

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

#### Convert_birth_years_to_integers ####

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








