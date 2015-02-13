## DataQuest_Numpy_Alcohol_Consumption_20150210

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 8

# Basics: Finding out about world alcohol consumption (Finding_the_country_that_drinks_the_least)

# Learn about numpy, matrices, and vectors while finding out with country drinks the most (and least!).   

#####################################

Overview of Useful code:
Reading data into numpy. (Reading_data_into_numpy)
Reading formatted data _type into numpy, dtype. (Fixing_the_data_types)
Indexing data _with array equals matix[rows,columns]. (Indexing_the_data)
Vectors, Indexing _and slicing. (Vectors)
Array, finding the dimensions _with shape method. (Array_shape)
Use booleans to check _if a vector equals X. (Boolean_elements)
Subset vectors based on booleans. (Subsets_of_vectors)
Subsetting multiple conditions _with the ampersand. (Subsets_with_multiple_conditions)
Convert datatype to floats. (Convert_a_column_to_floats)
Replace each value depending on condition. (Replace_values_in_an_array)
Replace bad values then convert them to floats. (Convert_the_alcohol_consumption_column_to_floats)
Compute the total value of a column using the .sum method. (Compute_the_total_alcohol_consumption)
Compute the total amount of alcohol the average Algerian drank _in _1985.(Finding_how_much_alcohol_a_person_in_a_country_drank_in_a_year)
Creating a function to find this total. (A_function_to_sum_alcohol_consumption_by_country_and_year)
Find the country _with the lowest amount of alcohol consumed per person _in _1989. (Finding_the_country_that_drinks_the_least)
Find the country _with the highest amount of alcohol consumed per person _in _1989. (Finding_the_country_that_drinks_the_most)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Reading_data_into_numpy ####

import numpy
alcohol_file = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(alcohol_file, delimiter=",")


#### Fixing_the_data_types ####

import numpy
alcohol_file = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(alcohol_file, delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol[:100]) # Prints first 100 rows of the data


#### Indexing_the_data ####

# Assign the amount of alcohol Uruguayans drank in other beverages per capita 
# in 1986 to uruguay_other_1986. This is the second row in the data.
# Assign the whole fourth row to row_four.
# Assign the whole year column to years

uruguay_other_1986 = world_alcohol[1,4]
row_four = world_alcohol[3,:]
years = world_alcohol[:,0]

# array = matix[rows,columns] 


#### Vectors ####

# Countries is a vector.
countries = world_alcohol[:,2]
# We can index a vector with only one number.
print(countries[0])
# We can also slice vectors to get some of the values in the vector.
print(countries[1:10])


#### Array_shape ####

# Print the shape of the world alcohol matrix.
print(world_alcohol.shape)
# We can do the same with a vector, but they only have one dimension, so only one number is printed.
print(world_alcohol[1,:].shape)


#### Boolean_elements ####

years_1984 = (world_alcohol[:,0] == "1984")
# years_1984 is a new vector with 'True/False' values.


#### Subsets_of_vectors ####

# We can subset vectors based on boolean vectors like the ones we generated in the last screen.
beer = (world_alcohol[:,3] == "Beer")
print(world_alcohol[:,3][beer])
# The code above will select and print only the elements in the fourth column whose value is "Beer".

# Subset the third column of world_alcohol on whether the value is "Algeria". 
country_algeria = (world_alcohol[:,2][world_alcohol[:,2] == "Algeria"])


#### Subsets_with_multiple_conditions ####

algeria_1985_boolean = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == "1985")
print(algeria_1985_boolean)
> [False False ... False False]
# If both vectors are True at index 1, then the resulting vector will be True at index 1.
# If either vector is False at index 1, the result will be False at index 1.

# Assign all rows where the country is "Latvia", the year is "1989", and the type of alcohol is "Wine" to latvia_1989_wine.
latvia_1989_wine_booleans = ((world_alcohol[:,2] == "Latvia") & (world_alcohol[:,0] == "1989") & (world_alcohol[:,3] == "Wine"))
latvia_1989_wine = (world_alcohol[latvia_1989_wine_booleans,:])


#### Convert_a_column_to_floats ####

# Let's convert the column to floats.
alcohol_numbers = world_alcohol[:,4].astype(float)
# Hmm, but the above code fails with an error!


#### Replace_values_in_an_array ####

# We can replace values in a numpy array by just assigning to them with the equals sign.
world_alcohol[:,4][world_alcohol[:,4]=='0'] = '10'

#### Convert_the_alcohol_consumption_column_to_floats ####

# Now that you know what the bad value is, we can replace it and then convert the column to floats.
bad_value = ''
alcohol_consumption_float_column = None
# Replace all the values in the alcohol consumption column (column 5) that equal bad_value with '0'.
# Then convert all of the values in the column to floats, 
world_alcohol[:,4][world_alcohol[:,4] == bad_value] = "0"
alcohol_consumption_float_column = world_alcohol[:,4].astype(float)


#### Compute_the_total_alcohol_consumption ####

# We can compute the total value of a column using the sum method.
total_alcohol = 0
total_alcohol = alcohol_consumption.sum()
print(total_alcohol)


#### Finding_how_much_alcohol_a_person_in_a_country_drank_in_a_year ####

# We can subset a vector with another vector, as we learned earlier.
# This means that we can find the total alcohol consumed by any given country in any given year now.
algeria_1985 = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == '1985')
# Subset the alcohol consumption vector with our boolean, and get the sum.
# The sum is the total amount of alcohol and average Algerian drank in 1985.
algeria_1985_alcohol = alcohol_consumption[algeria_1985].sum()


#### A_function_to_sum_alcohol_consumption_by_country_and_year ####

# Now that we know how to find the total alcohol consumption of the average person in a country in a given year, 
# we can make a function out of it.
def calculate_consumption(country, year):
    country_year = alcohol_consumption[((world_alcohol[:,2] == country) & (world_alcohol[:,0] == year))]
    country_year_alcohol = country_year.sum()
    return country_year_alcohol

india_1989_alcohol = calculate_consumption("India","1989")
print(india_1989_alcohol)


#### Finding_the_country_that_drinks_the_least ####

# We can now loop over our dictionary keys to find the country with the lowest amount of alcohol consumed per person in 1989.

lowest_country = None
lowest_consumption = None

for key,value in country_consumption_1989.items():
    #print(key,value)
    if lowest_consumption is None or value < lowest_consumption:
        lowest_consumption = value
        lowest_country = key

lowest_country_list = []
for key,value in country_consumption_1989.items():
    if value == lowest_consumption:
        lowest_country_list.append(key)

print(lowest_consumption)
print(lowest_country_list)
print(lowest_country)


#### Finding_the_country_that_drinks_the_most ####

highest_country = None
highest_consumption = None

for key,value in country_consumption_1989.items():
    if highest_consumption is None or value > highest_consumption:
        highest_consumption = value
        highest_country = key



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# The dataset:

# Year, Region (aggregate of country), Country, Type, Amount (Ethanol)
# 1960 , Americas,  Canada, Type, Amount 

# For anybody over 15 years old.

# First we need to learn about the module numpy.
    
    # a table is a type of array and it is a matrix type of array.

#    0       1       2
# 0 Year  Region  Country
# 1 1960 Americas Canada
# 2 1968   

#### Reading_data_into_numpy ####

# numpy is a python module that has a lot of functions for working with data.
# If you want to do serious work with data in python, you'll be using a lot of numpy.
# We'll work through importing numpy and loading in a csv file.

# Importing numpy is the same as other imports.
import numpy

# We'll get our nfl filename from before.
# Note that we don't need to use the open function to open it -- numpy will take care of that.

f = "nfl.csv"
# for_my_data = open("C:\Users\Christian\Anaconda\MyPractice_20141009\DataQuest_testing_Numpy_Pandas\hello.txt","r")

# The genfromtxt function in numpy is used to read files.
# delimiter is a named keyword argument specifying that commas separate the data fields (we have a csv file, which means comma separated values).
nfl = numpy.genfromtxt(f, delimiter=",")
print(nfl)

# Import the data in "world_alcohol.csv" into the variable world_alcohol.

file = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(file, delimiter=",")


#### Fixing_the_data_types ####

# If you looked at the data you read in last screen, you may have noticed that it looked very strange.
# This is because genfromtxt reads the data into a numpy array.
# Every element in an array has to be the same data type.
# So everything is a string, or everything is an integer, and so on.

# numpy tried to convert all of our data to floats, which caused the values to become strange.
# We'll need to specify the data type when we read our data in so we can avoid that.

import numpy

f = "nfl.csv"
# Using the dtype keyword argument with the str type tells numpy that everything we are reading in is a string.
# "U75" tells numpy to load the file as strings.
# The "U" refers to unicode (a type of string), and the 75 is the maximum length of a string element in the data.
# While we're at it, let's also skip the header.
# We can add the optional skip_header keyword argument, and set it equal to the number of header rows to skip (1).
nfl = numpy.genfromtxt(f, delimiter=",", dtype="U75", skip_header=1)

# Read in the "world_alcohol.csv" data to world_alcohol, using the str datatype.
# Be sure to skip the header row.

file = "world_alcohol.csv"
world_alcohol = numpy.genfromtxt(file, delimiter=",", dtype="U75", skip_header=1)

print(world_alcohol[:100]) # Prints first 100 rows of the data


#### Indexing_the_data ####

# Now that we know how to read in a file, let's start pulling values out.
# Remember how all elements in a matrix have an index?
# We can print the item at row 1, column 2, by typing print world_alcohol[0,1]

# The columns are Year, Region, Country, Beverage type, and Number of liters of pure alcohol drunk per person
# The print function below prints the number of liters of pure alcohol vietnamese drank in wine in 1986.
print(world_alcohol[0,4])

# The Beverage type can take the values "Beer", "Wine", "Spirits", and "Other"

# If we want to grab a whole row, we replace the column number with a colon, which means "get all of the columns"
print(world_alcohol[0,:])

# If we want to grab a whole column, we do the same thing with the row number.
countries = world_alcohol[:,2]

print(world_alcohol[0,1])

# Assign the amount of alcohol Uruguayans drank in other beverages per capita 
# in 1986 to uruguay_other_1986. This is the second row in the data.
# Assign the whole fourth row to row_four.
# Assign the whole year column to years

print(world_alcohol[1,4])
print(world_alcohol[3,:])
print(world_alcohol[:,0])
uruguay_other_1986 = world_alcohol[1,4]
row_four = world_alcohol[3,:]
years = world_alcohol[:,0]

# array = matix[rows,columns] 

print(type(world_alcohol[1,4]))    # > class numpy.str_
print(type(world_alcohol[3,:]))    # > class numpy.ndarray
print(type(world_alcohol[:,0]))    # > class numpy.ndarray


#### Vectors ####

# When we grab a whole row or column from the matrix, we actually end up with a vector.
# Just like a matrix is a 2-dimensional array because it has rows and columns, a vector is a 1-dimensional array.
# Vectors are similar to python lists in that they can be indexed with only one number.
# Think of a vector as just a single row, or a single column

# Countries is a vector.
countries = world_alcohol[:,2]

# We can index a vector with only one number.
print(countries[0])
print(countries[10])

# We can also slice vectors to get some of the values in the vector.
# The result is a new, smaller, vector.
# Slicing gets values from the first index up to but not including the second index.
print(countries[1:10])
print(countries[50:70])

# Assign index 30 in the years column to years_30.
# Assign from index 80 to index 200, inclusive, in the years columns to years_80_200.
# Assign from index 100 to index 103, inclusive, in the years columns to years_100_103.

years = world_alcohol[:,0]

years_30 = years[30]
years_80_200 = years[80:201]
years_100_103 = years[100:104]

#### Array_shape ####

# All arrays, whether they are 1-dimensional (vectors), two dimensional (matrices), 
# or even larger, have a number of elements in each dimension.
# For example, a matrix may have 200 rows and 10 columns.
# We can use the shape method to find these dimensions

# Print the shape of the world alcohol matrix.
# The first number is the number of rows, and the second is the number of columns
print(world_alcohol.shape)

# We can do the same with a vector, but they only have one dimension, so only one number is printed.
print(world_alcohol[1,:].shape)

# Assign the shape of the first column in world_alcohol to column_one_shape. The first column has index 0.
# Assign the shape of the tenth row in world_alcohol to row_ten_shape. The tenth row has index 9.

column_one_shape = world_alcohol[:,0].shape
row_ten_shape = world_alcohol[9,:].shape

print(column_one_shape)
print(row_ten_shape)


#### Boolean_elements ####

# We can also use boolean statements on arrays to get truth values.
# The interesting part about this is that the booleans are computed elementwise.
world_alcohol[:,3] == "Beer"
# The above code will actually compare each element of the fourth column of world_alcohol, 
# check if it equals "Beer", and create a new vector with the True/False values.

# This will get the first 10 items in the fourth column of world alcohol.
# This is the type column.
selected_types = world_alcohol[:,3][0:10]
print(selected_types)
# This will create a vector that contains True if the item at that position equal "Beer", and False if not.
# The vector is then printed.
# Note how the first three values are False, because the element in the position does not equal "Beer".
# The fourth and fifth are "True".
print(selected_types == "Beer")

# Create a vector that checks if the values in column one equal "1984". 
# Assign the vector to years_1984.
# Create a vector that checks if the values in column three equal "Canada". 
# Assign the vector to countries_canada.

years_1984 = (world_alcohol[:,0] == "1984")
countries_canada = (world_alcohol[:,2] == "Canada")

#### Subsets_of_vectors ####

# We can subset vectors based on boolean vectors like the ones we generated in the last screen.
beer = (world_alcohol[:,3] == "Beer")
print(world_alcohol[:,3][beer])
# The code above will select and print only the elements in the fourth column whose value is "Beer".
# world_alcohol[:,3][beer] goes through each position in the fourth column vector (from 0 to the last index), 
# and checks if the beer vector is True at the same position. If the beer vector is True, 
# it assigns the element of the fourth column at that position to the subset. 
# If the beer vector is False, the element is skipped.

# Select the first 10 values in the "type" column
types = world_alcohol[:,3][0:10]
print(types)

# Create a boolean vector that contains True or False indicating whether each element in types == "Beer"
beer_boolean = types == "Beer"
print(beer_boolean)

# Subset the types vector using the beer_boolean
# We end up with only two entries, corresponding to the entries in the types vector that have the "Beer" value
print(types[beer_boolean])
print(world_alcohol[:,3][0:10][world_alcohol[:,3][0:10] == "Beer"])
# Subset the third column of world_alcohol on whether the value is "Algeria". 
# Assign the result to country_algeria.
# Subset the first column of world_alcohol on whether the value is "1987". 
# Assign the result to year_1987.

print(world_alcohol[1])
country_algeria = (world_alcohol[:,2][world_alcohol[:,2] == "Algeria"])
year_1987 = (world_alcohol[:,0][world_alcohol[:,0] == "1987"])
print(country_algeria)
print(year_1987)

#### Subsets of matrices ####

# We can subset a matrix in the same way that we can subset a vector.
beer = (world_alcohol[:,3] == "Beer")
print(world_alcohol[beer,:])

# The above code will print all of the rows in world_alcohol where the "Type" column equals "Beer"
# Note how because matrices are indexed using two numbers, we are substituting the boolean vector beer for the first number.
# We can alter the second number to select different columns.

beer = (world_alcohol[:,3] == "Beer")
print(world_alcohol[beer,1])
# The above code would select the second column where the "Type" column equals "Beer"


# wine_rows now contains only rows where the beverage type is wine.
wine = world_alcohol[:,3] == "Wine"
wine_rows = world_alcohol[wine,:]

# wine_rows is still a matrix, so we can index it as such.
# Just like we can slice vectors, we can slice matrix rows or columns.
# In the below statement, we print all of the columns in the first 10 rows of wine_rows.
print(wine_rows[0:10,:])

# Assign all of the rows where the country equals "Turkey" to turkey_rows.
# Assign the first 10 rows where the year equals "1985" to rows_1985.
# Note that variable names in python can't start with numbers, so we can't start our name with 1985.

turkey = world_alcohol[:,2] == "Turkey"
turkey_rows = world_alcohol[turkey,:]
print(turkey_rows)

year_1985 = world_alcohol[:,0] == "1985"
r_1985 = world_alcohol[year_1985,:]
rows_1985 = (r_1985[0:10,:])

#Or filling in the different parts:
rows_1985 = (world_alcohol[(world_alcohol[:,0] == "1985"),:][0:10,:])


#### Subsets_with_multiple_conditions ####

# So now we can find all of the rows that correspond to "Algeria", for example.
# But what if what we really want is to find all the rows for "Algeria" in "1985"?
# We'll have to use multiple conditions to generate our vector.

algeria_1985_boolean = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == "1985")

print(algeria_1985_boolean)

> [False False ... False False]

# The code above will generate a boolean that uses multiple conditions.
# How it works is that the parentheses specify that the two component vectors should be generated first. (order of operations)
# Then the two vectors will be compared index by index. 
# If both vectors are True at index 1, then the resulting vector will be True at index 1.
# If either vector is False at index 1, the result will be False at index 1.

# Here's an expanded example:
boolean_1985 = (world_alcohol[:,0] == "1985")
algeria_boolean = (world_alcohol[:,2] == "Algeria")
algeria_1985_boolean = boolean_1985 & algeria_boolean

# We can add more than 2 conditions if we want -- we just have to put an & symbol between each one.
# The resulting vector will contain True in the position corresponding to rows where all conditions are True, 
# and False for rows where any condition is False.


# Boolean vector corresponding to Canada and 1986.
canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986")

# We can then use canada_1986 to subset a matrix -- it's just a normal boolean vector
print(world_alcohol[canada_1986,:])

# Assign all rows where the country is "Yemen" and the year is "1987" to yemen_1987.
# Assign all rows where the country is "Latvia", the year is "1989", 
# and the type of alcohol is "Wine" to latvia_1989_wine.

yemen_1987_booleans = (world_alcohol[:,2] == "Yemen") & (world_alcohol[:,0] == "1987")
latvia_1989_wine_booleans = ((world_alcohol[:,2] == "Latvia") & (world_alcohol[:,0] == "1989") & (world_alcohol[:,3] == "Wine"))

yemen_1987 = (world_alcohol[yemen_1987_booleans,:])
latvia_1989_wine = (world_alcohol[latvia_1989_wine_booleans,:])


#### Convert_a_column_to_floats ####

# We now know almost everything we need to compute how much alcohol the people in a country drank in a given year!
# But there are a couple of things we need to work through first.
# First, we need to convert the "Liters of alcohol drunk" column (the fifth one) to floats.
# We need to do this because they are strings now, and we can't take the sum of strings.
# Because they aren't numeric, their sum wouldn't make much sense.
# We can use the astype method on the array to do this

# Let's convert the column to floats.
alcohol_numbers = world_alcohol[:,4].astype(float)

# Hmm, but the above code fails with an error!
# It looks like some of the values in the column can't be converted to floats.
# We'll find out how we can figure out if values are failing in the next screen.
# For now, just hit Run.


#### Replace_values_in_an_array ####

# There are values in our alcohol consumption column that are preventing us from converting the column from floats from strings.
# In order to fix this, we first have to learn how to replace values.
# We can replace values in a numpy array by just assigning to them with the equals sign.

world_alcohol[:,4][world_alcohol[:,4]=='0'] = '10'

# The code above will replace any item in the alcohol consumption column that contains '0' 
# (remember that the world alcohol matrix is all string values) with '10'.


# Let's say the US invades Canada (not that they should)
# This will replace all instances of "Canada" in the country column with "United States of America"
world_alcohol[:,2][world_alcohol[:,2] == "Canada"] = "United States of America"
print(world_alcohol[:,2][world_alcohol[:,2] == "Canada"])

# We don't have to subset before we replace
# Trinidad and Tobago can invade the whole world, and replace all countries
world_alcohol[:,2] = "Trinidad and Tobago"
print(world_alcohol[:,2][0:10])

# Replace all instances of '1986' in the year column (column 1) with '2014'.
# Replace all the values in the type column (column 4) with 'Grog' (pirates have taken over the world).

world_alcohol[:,0][world_alcohol[:,0] == "1986"] = "2014"
world_alcohol[:,3] = "Grog"


#### Convert_the_alcohol_consumption_column_to_floats ####

# Now that you know what the bad value is, we can replace it and then convert the column to floats.

bad_value = ''
alcohol_consumption_float_column = None

# Replace all the values in the alcohol consumption column (column 5) that equal bad_value with '0'.
# Then convert all of the values in the column to floats, 
# and assign the result to alcohol_consumption_float_column.
# At the end, alcohol_consumption_float_column should contain a column of floats.

world_alcohol[:,4][world_alcohol[:,4] == bad_value] = "0"

alcohol_consumption_float_column = world_alcohol[:,4].astype(float)

print(type(alcohol_consumption_float_column))
# > class numpy.ndarray
for item in alcohol_consumption_float_column:
    print(type(item))
# > class numpy.float64


#### Compute_the_total_alcohol_consumption ####

# We can compute the total value of a column using the sum method.

# We've read the alcohol consumption column (converted to floats) into the alcohol_consumption variable.
total_alcohol = 0

# Use the sum method to store the sum of the alcohol consumption column into the total_alcohol column
total_alcohol = sum(alcohol_consumption)
print((total_alcohol))
> 3908.96

total = 0.00
for i in alcohol_consumption:
    total = total + i
print(total)
> 3908.96

## Broken??     ---   Worked!

total_alcohol = 0
total_alcohol = alcohol_consumption.sum()
print(total_alcohol)


#### Finding_how_much_alcohol_a_person_in_a_country_drank_in_a_year ####

# We can subset a vector with another vector, as we learned earlier.
# This means that we can find the total alcohol consumed by any given country in any given year now.

# Create a boolean vector that contains True where year is 1985 and the country is Algeria.
algeria_1985 = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == '1985')

# Subset the alcohol consumption vector with our boolean, and get the sum.
# The sum is the total amount of alcohol and average Algerian drank in 1985.
algeria_1985_alcohol = alcohol_consumption[algeria_1985].sum()

# Assign the total amount of alcohol an average person 
# in "Canada" drank in "1986" to canada_1986_alcohol.
# Assign the total amount of alcohol an average person 
# in "Trinidad and Tobago" drank in "1987" to trinidad_1987_alcohol.

canada_1986 = alcohol_consumption[((world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986"))]
canada_1986_alcohol = canada_1986.sum()
print(canada_1986_alcohol)

trinidad_1987 = alcohol_consumption[((world_alcohol[:,2] == "Trinidad and Tobago") & (world_alcohol[:,0] == "1987"))]
trinidad_1987_alcohol = trinidad_1987.sum()
print(trinidad_1987_alcohol)


#### A_function_to_sum_alcohol_consumption_by_country_and_year ####

# Now that we know how to find the total alcohol consumption of the average person in a country in a given year, we can make a function out of it.
# A function will make it easier for us to calculate the alcohol consumption for all countries.

def calculate_consumption(country, year):
    country_year = alcohol_consumption[((world_alcohol[:,2] == country) & (world_alcohol[:,0] == year))]
    country_year_alcohol = country_year.sum()
    # Fill in the rest of the function here.
    # Assume that country and year are strings.
    # You'll also need to delete the "pass" keyword.
    # The alcohol consumption column and the world_alcohol matrix are both loaded.
    #pass
    return country_year_alcohol
    

# Fill in the rest of the calculate_consumption function.
# Then use the function to calculate how much alcohol people
# in "India" drank in "1989" on average, and store the result in india_1989_alcohol.

india_1989_alcohol = calculate_consumption("India","1989")
print(india_1989_alcohol)


#### Finding_the_country_that_drinks_the_least ####

# We can now loop over our dictionary keys to find the country with the lowest amount of alcohol consumed per person in 1989.

# country_consumption_1989 has been loaded in for you.
lowest_country = None
lowest_consumption = None

# Loop over the keys in country_consumption_1989 
# and find the country where the average person drank the least in 1989.
# To do this, you'll need to use a for loop, and keep track of the lowest value and country.
# Assign the lowest value to lowest_consumption, 
# and the country with the lowest value to lowest_country.
# Check the hint if you need help.

for key,value in country_consumption_1989.items():
    #print(key,value)
    if lowest_consumption is None or value < lowest_consumption:
        lowest_consumption = value

lowest_country = []
for key,value in country_consumption_1989.items():
    if value == lowest_consumption:
        lowest_country.append(key)

print(lowest_consumption)
print(lowest_country)

## But this also worked:

for key,value in country_consumption_1989.items():
    #print(key,value)
    if lowest_consumption is None or value < lowest_consumption:
        lowest_consumption = value
        lowest_country = key

#### Finding_the_country_that_drinks_the_most ####

# country_consumption_1989 has been loaded in for you.
highest_country = None
highest_consumption = None

# Loop over the keys in country_consumption_1989 
# and find the country where the average person drank the most in 1989.
# To do this, you'll need to use a for loop, and keep track of the highest value and country.
# Assign the highest value to highest_consumption, 
# and the country with the highest value to highest_country.
# Check the hint if you need help.

for key,value in country_consumption_1989.items():
    if highest_consumption is None or value > highest_consumption:
        highest_consumption = value
        highest_country = key

highest_country_consumption = []
for key,value in country_consumption_1989.items():
    if highest_consumption == value:
        highest_country_consumption.append(key)
print(highest_country)
print(highest_consumption)
print(highest_country_consumption)


