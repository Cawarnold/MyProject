## DataQuest_Pandas_Nutritious_Foods_20150212

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 9

# Basics: Finding the most (and least) nutritious foods

# Learn about pandas and vector operations while analyzing US Department of Agriculture (USDA) data to find the most nutritious foods.	

#####################################

Overview of Useful code:
Use .iloc to extract values based on i,j row,column locations. (Indexing_data_with_pandas)
Index a series (one dimensional array). (Index_a_series)
Get columns _with their names, instead of only by numbers. (Get_column_by_name)
Get multiple columns by passing _in a _list of names. (Getting_multiple_columns_by_name)
We can do math _with vectors, going through each value at each position. (Math_with_columns_CalculatedFields)
We can also do math _with a vector (column) _and a scalar (single numbers). (Math_with_scalars)
Sort the dataframe by the values _in a column using .sort method. (Sorting_columns)
Sorting multiple columns _with the .sort method. (Multicolumn_sort)
We can construct a rating _and recommend the highest value. (Creating_a_rating)
Normalization of ratings means adjusting values measured on different scales to a notionally common scale. (Normalising_columns)
Normalise the values before creating a rating. (Making_a_better_rating)
Normalise multiple columns _with _for loop. (Normalizing_multiple_columns_for_loop)
Finding the .sum() of _all rows _and colummns. (Finding_the_amount_of_vitamins)
Adding a new column to the dataframe. (Adding_a_new_column)
Construct a nutritional rating using columns _and scalars. (Making_a_nutritional_index)
Using the .sort method, now find the most nutritious foods. (Finding_the_most_nutritious_foods)
Using the .sort method, now find the least nutritious foods. (Finding_the_least_nutritious_foods)

#####################################

#### SUMMARY OF USEFUL CODE ####

# Import pandas
import pandas
# Read "food_info.csv" info food_info.
food_info = pandas.read_csv("food_info.csv")


#### Indexing_data_with_pandas ####

pandas_dataframe.iloc[0,0]   # value from row 1, column 1 of pandas_dataframe
pandas_dataframe.iloc[:,0]   # series of every row, column 1
pandas_dataframe.iloc[0,:]   # series of row 1, every column


#### Index_a_series ####

# What we call a vector or a one-dimensional array is called a series in pandas.
# We index a series without using .iloc[].

# This is a series.
first_row = food_info.iloc[0,:]

# Get the first ten items in the first row.  Note how we index the series.
first_ten_items_in_first_row = first_row[0:10]

# Equivalent to the above two statements, just condensed.
first_ten_items_in_first_row = food_info.iloc[0,:][0:10]


#### Get_column_by_name ####

# First we can get the names of all the columns (in order)
print(list(food_info.columns.values))

sodium_column = food_info["Sodium_(mg)"]


#### Getting_multiple_columns_by_name ####

zinc_and_copper = food_info[['Zinc_(mg)', 'Copper_mg)']]


#### Math_with_columns_CalculatedFields ####

total_fat = food_info["FA_Sat_(g)"] + food_info["FA_Mono_(g)"] + food_info["FA_Poly_(g)"]

grams_of_protein_per_calorie = food_info["Protein_(g)"] / food_info["Energ_Kcal"]

grams_of_protein_squared = food_info["Protein_(g)"] * food_info["Protein_(g)"]

non_sugar_carbs = food_info["Carbohydrt_(g)"] - food_info["Sugar_Tot_(g)"]


#### Math_with_scalars ####

# A scalar is a 1 dimensional phrysical quantity - or a number. eg. 1000
food_info["Iron_(mg)"] / 1000


#### Sorting_columns ####

# The first argument to the .sort method is a list of columns to sort by.
# The other argument is named, and specifies the sort order of each of the columns.
descending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[False])


#### Multicolumn_sort ####

# The first column in the list will be sorted on first. 
# Any rows that have the same value for the first column will be sorted based on the second column, 
# We can specify different sort orders for each column using the ascending argument.
ascending_fat_then_ascending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, True])


#### Creating_a_rating ####

# To construct a rating for each food based on a criteria.
# Then we can recommend the food that scores the highest.
new_rating = (food_info["Protein_(g)"]*2)+(food_info["Lipid_Tot_(g)"]*(-1))


#### Normalising_columns ####

# One of the simplest ways to normalize a column is to divide all of the values by the maximum value in the column.
# It will change all of the values to be between 0 and 1.
normalized_vitamin_c =  food_info["Vit_C_(mg)"] / food_info["Vit_C_(mg)"].max()


#### Making_a_better_rating ####

# We just have to normalize the columns that we are interested in before we create the rating.
normalized_protein =  food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_lipid_fat =  food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
better_protein_rating = (normalized_protein*2) + (-1*normalized_lipid_fat)

#### Normalizing_multiple_columns_for_loop ####

# All columns is a list of all the columns in the food_info dataframe.
all_columns = list(food_info.columns.values)

# Remove the "NDB_No" and "Shrt_Desc" columns from all_columns
# Then, use a for loop to normalize all the other columns

numeric_columns = all_columns[2:]
for column in numeric_columns:
    food_info[column] = food_info[column] / food_info[column].max()


#### Finding_the_amount_of_vitamins ####

# Now that we normalized all of the columns, we're well on our way to making a nutritional rating.
# In order to get there, let's create a sum of all the vitamin columns.
# Most methods on pandas dataframes can operate on series, or on dataframes.
# Let's take the .sum() method as an example.
# On a series, it gives you the total of all the values in the series.
# When used on a dataframe, it takes the optional axis keyword argument.
# When axis is 0, it gives you a new series with the sums of all of the columns in the dataframe.
# When axis is 1, it gives you a new series with sums of all of the rows in the dataframe.

vitamin_columns = ['Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)',
 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 
 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 
 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU', 'Vit_K_(mcg)']

vitamin_totals = food_info[vitamin_columns].sum(axis=1)
print(vitamin_totals)      # The sum of vitamins for each food.

vitamin_columns_total = food_info[vitamin_columns].sum(axis=0)
print(vitamin_columns_total)     # The sum of foods for each vitamin.


#### Adding_a_new_column ####

# The below code assigns double the amount of lipids to the "double_fat" column in food_info.
food_info["double_fat"] = food_info["Lipid_Tot_(g)"] * 2

food_info["vitamin_totals"] = food_info[vitamin_columns].sum(axis=1)



#### Making_a_nutritional_index ####

# We've normalized the values in vitamin_totals, and assigned it to the "vitamin_totals" column in food_info.
# Let's construct a nutritional rating using the amount of vitamins, fats, protein, sugar, fiber, and cholesterol.

nutritional_rating = None

nutritional_rating = ((food_info["vitamin_totals"]*3) + 
(food_info["Lipid_Tot_(g)"]*(-2)) + 
(food_info["Protein_(g)"]*3) + 
(food_info["Sugar_Tot_(g)"]*(-1)) +
(food_info["Fiber_TD_(g)"]*(1)) +
(food_info["Cholestrl_(mg)"]*(-2)))


#### Finding_the_most_nutritious_foods ####

# We've read the nutritional rating series from the last screen to the "nutritional_rating" column in food_info.
# Now, lets see if we can use it to find the most nutritious foods.

most_nutritious_foods = []

sorted_food = food_info.sort(['nutritional_rating'], ascending = [False])
top_3 = sorted_food.iloc[0:3][["Shrt_Desc","nutritional_rating"]]
most_nutritious_foods = list(top_3["Shrt_Desc"])
print(most_nutritious_foods)


#### Finding_the_least_nutritious_foods ####

# Let's do the same as in the last screen, but find the least nutritious foods.

least_nutritious_foods = []

# Find the three least nutritious foods by sorting food_info using the "nutritional_rating" column.
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to least_nutritious_foods
# If least_nutritious_foods isn't a list at the end, use the list() function to turn it into one.

sorted_food = food_info.sort(['nutritional_rating'], ascending = [True])
top_3 = sorted_food.iloc[0:3][["Shrt_Desc","nutritional_rating"]]
least_nutritious_foods = list(top_3["Shrt_Desc"])



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


#### Math_with_columns_CalculatedFields ####

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

# Let's assume that Superman is three times more interested in foods having a lot of protein than he is worried about them having too much fat.
# We can "weight" the protein number by his criteria, or multiply it by three.
# First we'll calculate the weighted value for protein.
weighted_protein = food_info["Protein_(g)"] * 3

# And now the weighted value for fat.
# We'll give fat a weight of -1, because he wants to avoid foods that have a lot of it, but he cares about foods having a lot of protein three times as much.
weighted_fat = -1 * food_info["Lipid_Tot_(g)"]

# We can construct our rating by just adding the weighted values.
initial_rating = weighted_protein + weighted_fat

# Let's say Superman now decides that the food having a lot of protein 
# is only twice as important as the food not being too fatty.

# Construct the new rating, and assign it to new_rating

new_rating = (food_info["Protein_(g)"]*2)+((-1)*food_info["Lipid_Tot_(g)"])


#### Normalizing values ####

# normalization of ratings means adjusting values measured on different scales to a notionally common scale.

# There are various normalizations in statistics – 
# nondimensional ratios of errors, residuals, means and standard deviations, which are hence scale invariant.

#### Normalising_columns ####

# One of the simplest ways to normalize a column is to divide all of the values by the maximum value in the column.
# It will change all of the values to be between 0 and 1.
# It doesn't work so well with negative values, but we don't have any (you can't have negative amounts of protein, fat, etc).
# This isn't necessarily the best way to normalize, and we'll learn some better methods soon.

# We can use the max() method to find the maximum value in a column.
max_protein = food_info["Protein_(g)"].max()

# And then we can divide the column by the scalar.
normalized_protein = food_info["Protein_(g)"] / max_protein

# See how all the values are between 0 and 1 now?
print(normalized_protein[0:20])

# Normalize the values in the "Vit_C_(mg)" column, and assign the result to normalized_vitamin_c
# Normalize the values in the "Zinc_(mg)" column, and assign the result to normalized_zinc

normalized_vitamin_c =  food_info["Vit_C_(mg)"] / food_info["Vit_C_(mg)"].max()
normalized_zinc =  food_info["Zinc_(mg)"] / food_info["Zinc_(mg)"].max()


#### Making_a_better_rating ####

# We now know enough to construct a better rating for our friend Superman.
# We just have to normalize the columns that we are interested in before we create the rating.

better_protein_rating = None

# Superman is twice as interested in a food having a lot of protein
# than he is in it having too much fat.
# Construct a rating with these new criteria, and assign it to better_protein_rating.
# Make sure to normalize the protein ("Protein_(g)") and fat ("Lipid_Tot_(g)") columns first!

normalized_protein =  food_info["Protein_(g)"] / food_info["Protein_(g)"].max()

normalized_lipid_fat =  food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

better_protein_rating = (normalized_protein*2) + (-1*normalized_lipid_fat)
print(better_protein_rating)


#### Normalizing_multiple_columns_for_loop ####

# Now, let's say we want to construct a total nutrition rating that takes all the columns into account.
# In order to do this, we would have to normalize each of the columns, which is a huge pain.
# An easier way is to use a for loop to normalize each column.
# The "NDB_No" and "Shrt_Desc" columns (first two) can't be normalized, because they aren't nutritional values. 
# The first one is the ID number of the food, and the second is the name.

column_list = ["Energ_Kcal", "Protein_(g)"]

# This will loop through column_list, and normalize each of the columns in it.
for column in column_list:
    food_info[column] = food_info[column] / food_info[column].max()

# All columns is a list of all the columns in the food_info dataframe.
all_columns = list(food_info.columns.values)
print(all_columns)

# Remove the "NDB_No" and "Shrt_Desc" columns from all_columns
# Then, use a for loop to normalize all the other columns

numeric_columns = all_columns[2:]
for column in numeric_columns:
    food_info[column] = food_info[column] / food_info[column].max()


#### Finding_the_amount_of_vitamins ####

# Now that we normalized all of the columns, we're well on our way to making a nutritional rating.
# In order to get there, let's create a sum of all the vitamin columns.
# Most methods on pandas dataframes can operate on series, or on dataframes.
# Let's take the .sum() method as an example.
# On a series, it gives you the total of all the values in the series.
# When used on a dataframe, it takes the optional axis keyword argument.
# When axis is 0, it gives you a new series with the sums of all of the columns in the dataframe.
# When axis is 1, it gives you a new series with sums of all of the rows in the dataframe.

column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']

# Let's sum the amount of fiber and sugar in each of the foods.
row_total = food_info[column_list].sum(axis=1)

# This gives us a sum for each row in the data
print(row_total)

# Let's sum up the total amount of fiber and sugar across all the foods.
column_total = food_info[column_list].sum(axis=0)
print(column_total)

vitamin_columns = ['Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU', 'Vit_K_(mcg)']


# Sum up the amount of vitamins in each food 
# (using the vitamin_columns list to get columns from the dataframe), 
# and assign the result to vitamin_totals.
# You'll need to sum the total in each row.

vitamin_totals = food_info[vitamin_columns].sum(axis=1)
print(vitamin_totals)      # The sum of vitamins for each food.

vitamin_columns_total = food_info[vitamin_columns].sum(axis=0)
print(vitamin_columns_total)     # The sum of foods for each vitamin.


#### Adding_a_new_column ####

# We can add a column to a dataframe by assigning to it.
food_info["double_fat"] = food_info["Lipid_Tot_(g)"] * 2
# The above code assigns double the amount of lipids to the "double_fat" column in food_info.

food_info["double_protein"] = food_info["Protein_(g)"] * 2

# We've read the vitamin_totals variable from the last screen in.
# Assign vitamin_totals to the "vitamin_totals" column in food_info.

vitamin_columns = ['Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU', 'Vit_K_(mcg)']

food_info["vitamin_totals"] = food_info[vitamin_columns].sum(axis=1)

#or

food_info["vitamin_totals"] = vitamin_totals


#### Making_a_nutritional_index ####

# We've normalized the values in vitamin_totals, and assigned it to the "vitamin_totals" column in food_info.
# Let's construct a nutritional rating using the amount of vitamins, fats, protein, sugar, fiber, and cholesterol.

nutritional_rating = None

# Give the "vitamin_totals" column a weight of 3,
# the "Lipid_Tot_(g)" column a weight of -2, 
# the "Protein_(g)" column a weight of 3, 
# the "Sugar_Tot_(g)" column a weight of -1, 
# the "Fiber_TD_(g)" a weight of 1, 
# and the "Cholestrl_(mg)" column a weight of -2.

# Construct a rating using the above weights, and assign it to nutritional_rating.

nutritional_rating = ((food_info["vitamin_totals"]*3) + 
(food_info["Lipid_Tot_(g)"]*(-2)) + 
(food_info["Protein_(g)"]*3) + 
(food_info["Sugar_Tot_(g)"]*(-1)) +
(food_info["Fiber_TD_(g)"]*(1)) +
(food_info["Cholestrl_(mg)"]*(-2)))


#### Finding_the_most_nutritious_foods ####

# We've read the nutritional rating series from the last screen to the "nutritional_rating" column in food_info.
# Now, lets see if we can use it to find the most nutritious foods.

most_nutritious_foods = []

# Find the three most nutritious foods by sorting food_info using the "nutritional_rating" column.
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to most_nutritious_foods.
# If most_nutritious_foods isn't a list at the end, use the list() function to turn it into one.

sorted_food = food_info.sort(['nutritional_rating'], ascending = [False])
top_3 = sorted_food.iloc[0:3][["Shrt_Desc","nutritional_rating"]]
print(top_3)

most_nutritious_foods = list(top_3["Shrt_Desc"])
print(most_nutritious_foods)
print(type(most_nutritious_foods))

# ^ Works ^

## Official Answer

sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[False])
most_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
most_nutritious_foods = list(most_nutritious_foods)


#### Finding_the_least_nutritious_foods ####

# Let's do the same as in the last screen, but find the least nutritious foods.

least_nutritious_foods = []

# Find the three least nutritious foods by sorting food_info using the "nutritional_rating" column.
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to least_nutritious_foods
# If least_nutritious_foods isn't a list at the end, use the list() function to turn it into one.

sorted_food = food_info.sort(['nutritional_rating'], ascending = [True])
top_3 = sorted_food.iloc[0:3][["Shrt_Desc","nutritional_rating"]]
least_nutritious_foods = list(top_3["Shrt_Desc"])
