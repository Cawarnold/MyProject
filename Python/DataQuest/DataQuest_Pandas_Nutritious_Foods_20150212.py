## DataQuest_Pandas_Nutritious_Foods_20150212

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 8

# Basics: Finding the most (and least) nutritious foods

# Learn about pandas and vector operations while analyzing US Department of Agriculture (USDA) data to find the most nutritious foods.	

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# USDA, US dept of Agriculture

# each column is a different item that appears in a food.

# Name_of_food, Protein (g) , Calcium(mg), Fat_Sat(g), ...
# Butter      , 0.85        ,  24        , 51 ....
# ...

# Find the most nutritious foods.

# pandas builds on numpy.


#### Read in a CSV file ####

# Let's get started using pandas. Because pandas builds on numpy, some things will be familiar, but others will take some time to get used to.
# The first step, as always, is reading in a csv file.
# With pandas, we'll need to use the read_csv method.
# With pandas, the equivalent of a two-dimensional numpy array, or matrix, is called a dataframe.

# Import pandas
import pandas

# Read in the world_alcohol.csv data from earlier.
world_alcohol = pandas.read_csv("world_alcohol.csv")

# Read "food_info.csv" info food_info.
food_info = pandas.read_csv("food_info.csv")


#### Indexing_data_with_pandas ####

# Indexing data with pandas
# Indexing in pandas is slightly different from in numpy.
# We need to use the .iloc[] method (note how it uses square brackets instead of parentheses).

numpy_array[0,0]
numpy_array[:,0]
numpy_array[0,:]

# The above lines of code will get the first element of the first row, the whole first column, 
# and the whole first row from a numpy array, respectively.

pandas_dataframe.iloc[0,0]
pandas_dataframe.iloc[:,0]
pandas_dataframe.iloc[0,:]

# The above is the equivalent indexing in a pandas dataframe.

# The food_info data has been loaded in.
# Print the first element in the first row.
print(food_info.iloc[0,0])

# Print the whole first row.
print(food_info.iloc[0,:])

# Assign the second row of food_info to the variable second_row.
second_row = food_info.iloc[1,:]

# Assign the tenth row of food_info to the variable tenth_row.
tenth_row = food_info.iloc[9,:]


#### Index_a_series ####

# What we call a vector or a one-dimensional array is called a series in pandas.
# We index a series without using .iloc[].

# This is a series.
first_row = food_info.iloc[0,:]

# Get the first ten items in the first row.  Note how we index the series.
first_ten_items_in_first_row = first_row[0:10]

# Equivalent to the above two statements, just condensed.
first_ten_items_in_first_row = food_info.iloc[0,:][0:10]
print(first_ten_items_in_first_row)

# Assign the first 20 items in the second row to first_20_items_in_second_row.
# Assign the first 10 items in the first column to first_10_items_in_first_column.

first_20_items_in_second_row = food_info.iloc[1,:][0:20]
first_10_items_in_first_column = food_info.iloc[:,0][0:10]

print(food_info.iloc[1,:][0:20])
print(type(food_info.iloc[1,:][0:20]))   # class 'pandas.core.series.Series'
print(type(food_info.iloc[1,:]))         # class 'pandas.core.series.Series'


#### Get_column_by_name ####

# One cool thing about pandas is that we can get columns with their names, instead of only by number.

# First we can get the names of all the columns (in order)
print(list(food_info.columns.values))

# Then we can get a column by name.
print(food_info["Protein_(g)"][0:10])

# And again.
sodium_column = food_info["Sodium_(mg)"]

# Assign the FA_Sat_(g) column to the variable saturated_fat.
# Assign the Cholestrl_(mg) to the variable cholesterol.

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]


#### Getting_multiple_columns_by_name ####

# We can get a single column by passing in a name, but we can also get multiple columns by passing in a list of names.

# This will get just the fiber and sugar columns from the data.
column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']
fiber_and_sugar = food_info[column_list]


# Assign the 'Zinc_(mg)' and 'Copper_(mg)' columns to zinc_and_copper.
# Assign the 'Selenium_(mcg)' and 'Thiamin_(mg)' columns to selenium_and_thiamin.
# Make sure that you get the columns in order (zinc and selenium come first).

# zinc_and_copper = food_info[['Zinc_(mg)', 'Copper_(mg)']]
# selenium_and_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]

zinc_and_copper = food_info[['Zinc_(mg)', 'Copper_mg)']]
selenium_and_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]


#### Math_with_columns_(CalculatedFields) ####

# We can do math with vectors (or, as we are more familiar with them as, columns).
# Adding two columns will go through and add each value at each position to the corresponding value in the same position.
# First, the values at index 0 will be added, then the values at index 1, and so on.
# At the end, you'll have a new vector with all of the sums.
# In order to do this kind of math, the vectors all need to be the same length (have the same number of elements).

# Adding up all of the fat columns.
total_fat = food_info["FA_Sat_(g)"] + food_info["FA_Mono_(g)"] + food_info["FA_Poly_(g)"]

# We can also divide.
grams_of_protein_per_calorie = food_info["Protein_(g)"] / food_info["Energ_Kcal"]

# We can also multiply
grams_of_protein_squared = food_info["Protein_(g)"] * food_info["Protein_(g)"]

# And subtract
non_sugar_carbs = food_info["Carbohydrt_(g)"] - food_info["Sugar_Tot_(g)"]


# Assign the number of grams of protein per gram of water 
# ("Protein_(g)" column divided by "Water_(g)" column) to grams_of_protein_per_gram_of_water.

# Assign the total amount of calcium and iron
# ("Calcium_(mg)" column plus "Iron_(mg)" column) to milligrams_of_calcium_and_iron.

print(type(food_info))      # class 'pandas.core.frame.DataFrame'
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]


#### Math_with_scalars ####

# A scalar is a 1 dimensional phrysical quantity - or a number. eg. 1000
# We can also do math with a vector (column) and a scalar (single numbers).
food_info["Iron_(mg)"] / 1000
# The statement above will divide each item in the "Iron_(mg)" column by 1000, converting the values from milligrams to grams.
# Multiplying by scalars can be a good way to manipulate values in columns.

# Divide the protein column by a scalar to get kilograms.
protein_kilograms = food_info["Protein_(g)"] / 1000

# Subtract 5 grams from carbohydrates.
lowered_carbs = food_info["Carbohydrt_(g)"] - 5

# Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams 
# (divide the column by 1000).
# Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams 
# (multiply the column by 1000).

sodium_grams = food_info["Sodium_(mg)"] / 1000

sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000


#### Sorting_columns ####

# We can also sort the dataframe by the values in a column.
# To do this, we use the .sort method, which returns a new dataframe sorted according to the specified criteria.

# Sort foods by amount of fat.
# The first argument to the sort method is a list of columns to sort by.
# For now, we are only sorting by a single column, so there is only one argument.
# The other argument is named, and specifies the sort order of each of the columns.  
# /True means the columns should be ascending (smallest value first, then increase)
# False means that they should be descending (largest value first, then decrease)
descending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[False])

# Print the most fatty food in the data.
#print(descending_fat.iloc[0,:])

# We can reverse the sort order.
ascending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[True])

# The least fatty food has no fat at all
#print(ascending_fat.iloc[0,:])

# Sort by the amount of "Sodium_(mg)", with the largest value on top (descending sort). 
# Assign the result to descending_sodium.
# Sort by the amount of "Vit_C_(mg)", with the smallest value on top (ascending sort). 
# Assign the result to ascending_vitamin_c.

descending_sodium = food_info.sort(["Sodium_(mg)"], ascending=[False])
ascending_vitamin_c = food_info.sort(["Vit_C_(mg)"], ascending=[True])
print(descending_sodium)
print(ascending_vitamin_c)


#### Multicolumn_sort ####

# We only sorted on the value of a single column before, but we can also sort based on multiple columns.
# The first column in the list will be sorted on first. 
# Any rows that have the same value for the first column will be sorted based on the second column, 
# and so on until all of the given columns are used.
# We can specify different sort orders for each column using the ascending argument.

# The food at the first row will be the one with the least fat.
# If there is a tie (several foods have no fat), it will be the food with 0 fat and the least sodium.
ascending_fat_then_ascending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, True])

# It's different than what we got when we just sorted on fat
print(ascending_fat_then_ascending_sodium.iloc[0,:])

# The food at the first row will be the one that has the most sodium, out of all the foods with 0 fat.
ascending_fat_then_descending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, False])

# Unsurprisingly, this is table salt
print(ascending_fat_then_descending_sodium.iloc[0,:])

# Perform a multicolumn sort on food_info, with the first column being "Sugar_Tot_(g)" ascending, 
# and the second being "Zinc_(mg)" descending. 
# Assign the result to ascending_sugar_then_descending_zinc.

# Perform a multicolumn sort on food_info, with the first column being "Cholestrl_(mg)" descending, 
# and the second being "Protein_(g)" ascending. 
# Assign the result to descending_cholesterol_then_ascending_protein.

ascending_sugar_then_descending_zinc = food_info.sort(["Sugar_Tot_(g)","Zinc_(mg)"], ascending=[True,False])
descending_cholesterol_then_ascending_protein = food_info.sort(["Cholestrl_(mg)","Protein_(g)"],ascending=[False,True])


#### Creating_a_rating ####

# Let's say that we have a friend, Superman, who's trying to gain muscle, 
# and so he wants to eat foods that have a lot of protein.
# But he's also very health conscious, so he wants to avoid fat.
# We could sort based on those two columns and give him an answer, 
# but what if he cares more about a food having a lot of protein than it being too fatty?
# What we need to do is construct a rating for each food based on Superman's criteria.
# Then we can recommend the food that scores the highest.




