## DataQuest_Pandas_Titanic_MissingData_20150216

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 10

# Basics: Working with missing data (Computing_survival_percentage_by_age_group)

# Learn more about pandas and how to deal with missing data while looking at survival data from the Titanic.

#####################################

Overview of Useful code:
Find missing data, count nulls _in age column. (Finding_missing_data)
Calculations we do _with a null value also result _in a null value. (Whats_the_big_deal_with_missing_data)
The .mean() will automatically remove missing values. (Easier_ways_to_do_math)
Subset the fares column based on the pclass at each iteration. (Computing_summary_statistics)
Index _is the grouping, values _is the _object that the aggfunc will operate on. (Making_pivot_tables)
Grouping by one category, summing multiple values. (More_complex_pivot_tables)
Using the dropna method to drop _any rows containing missing values. (Drop_missing_values)
Indexing _and selecting data using .iloc _and .loc methods. (Row_indices_loc_OR_iloc)
Sometimes it _is useful to reindex, _and make new indexes starting _from Zero. (Reindexing_rows)
Using _apply functions on columns, dataframe.apply(function). (Use_the_apply_function_on_columns)
Setting axis equal to one, we can use the .apply() method to iterate over rows, _not columns.(Applying_a_function_to_a_row)
Make a pivot table to find survival chance by age group. (Computing_survival_percentage_by_age_group)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Finding_missing_data ####

import pandas as pd

f = "titanic_survival.csv"
titanic_survival = pd.read_csv(f)

print(titanic_survival["age"])
age_null = pd.isnull(titanic_survival["age"])
count = 0
for item in age_null:
    if item == True:
        count = count + 1

age_null_count = (count)
print(age_null_count)


#### Whats_the_big_deal_with_missing_data ####

import pandas as pd
mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])

# Unfortunately, mean_age is NaN.  This is because any calculations we do with a null value also result in a null value.
# What we have to do instead is filter the missing values out before we compute the mean.
age_null = pd.isnull(titanic_survival["age"])
nonnull_age = titanic_survival["age"][age_null == False]
correct_mean_age = sum(nonnull_age) / len(nonnull_age)


#### Easier_ways_to_do_math ####

# Luckily, missing data is so common that pandas automatically filters for it with some methods.

import pandas as pd
correct_mean_age = titanic_survival["age"].mean()


#### Computing_summary_statistics ####

# Passengers can be in first class (1), second class (2), or third class (3)
# Let's compute the average fare for each class
passenger_classes = [1, 2, 3]
fares_by_class = {}
for pclass in passenger_classes:
    fare_for_class = None
    fare_for_class = (titanic_survival["fare"][titanic_survival["pclass"] == pclass]).mean()
    fares_by_class[pclass] = fare_for_class

print(fares_by_class)
## Needed to subset the fares column based on the pclass at each iteration.


#### Making_pivot_tables ####

import pandas as pd
import numpy as np

# A pivot table can automatically sort, count total or give the average of the data stored in one table or spreadsheet.
# Index specifies which column to subset data based on 
# Values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)

## index is the grouping, values is the object that the aggfunc will operate on.


#### More_complex_pivot_tables ####

import numpy as np

# This will compute the mean survival chance and the mean age for each passenger class
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print(passenger_survival)

>#            age       survived 
># pclass
>#  1         39.16       0.62
>#  2         29.51       0.43
>#  3         24.82       0.26

#### Drop_missing_values ####

# Using the dropna method on pandas dataframe to drop any rows containing missing values
import pandas as pd

new_titanic_survival = titanic_survival.dropna()

# We can also use the axis argument to drop columns that have missing values.
new_titanic_survival = titanic_survival.dropna(axis=1)

# We can use the subset argument to only drop rows if certain columns have missing values.
new_titanic_survival = titanic_survival.dropna(subset=["age", "body", "home.dest"])


#### Row_indices_loc_OR_iloc ####

# .iloc works by position (row/column number)
# Using .loc instead addresses rows and columns by index, not position

if new_titanic_survival.loc[3,:]["name"] == new_titanic_survival.iloc[0,:]["name"]:
    print(".loc uses index (dataframe index), .iloc uses position (row/column numbers)")

#### Reindexing_rows ####

# Remember how new_titanic_survival didn't have sequential row indexes?
# Each row retained its original index from titanic_survival.
# Sometimes it is useful to reindex, and make new indexes starting from 0.

new_titanic_survival1 = titanic_survival.dropna(subset=["age", "boat"])
titanic_reindexed = new_titanic_survival1.reset_index(drop=True)


#### Use_the_apply_function_on_columns ####

# The first step we need to take to figure out the age breakdown is to learn about the .apply() method.
# By default, .apply() will iterate through each column in a dataframe, and perform a function on it.
# The column will be passed into the function.
# The result from the function will be combined with all of the other results, and placed into a new series.
# The function results will have the same position as the column they were generated from.

import pandas as pd

# This function counts the number of null values in a series
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

# Compute null counts for each column
column_null_count = titanic_survival.apply(null_count)


#### Applying_a_function_to_a_row ####

# By passing in the axis argument, we can use the .apply() method to iterate over rows, not columns.
# This function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)


#### Computing_survival_percentage_by_age_group ####

# Now that we have age labels for everyone, let's make a pivot table to find survival chance by age group.

import numpy as np

print(list(titanic_survival.columns.values))
age_group_survival = titanic_survival.pivot_table(index=["age_labels"], values=["survived"], aggfunc=np.mean)


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#Manifest of the Titanic

#whether they survived, the class they were in 

# Columns:  pclass, survived, name, sex, age

#             1        1       "john"   male     29

#some data is missing, age, sex, 
#some columns are based on whether the person survived

# So lots of missing data.

#### Finding_missing_data ####

# Let's take a quick look at the missing data to see how it looks.
# Missing data can be presented a few different ways.
# In python, we have the None keyword and type, which indicates no value.
# pandas uses NaN, which stands for "not a number", to indicate a missing value.
# We can also call NaN a null value.   

# Using the as keyword assigns the import to a different name, so we can reference it more easily
# In this case, instead of having to type pandas all the time, we can just type pd
import pandas as pd

# Read in the survival data
f = "titanic_survival.csv"
titanic_survival = pd.read_csv(f)

# Print out the age column
print(titanic_survival["age"])

# We can use the isnull function to find which values in a column are missing
age_null = pd.isnull(titanic_survival["age"])

# age_null is a boolean vector, and has "True" where age is NaN, and "False" where it isn't

# Count the number of null values in the "age" column.
# Assign the result to age_null_count.

count = 0
for item in age_null:
    if item == True:
        count = count + 1

age_null_count = (count)
print(age_null_count)


#### Whats_the_big_deal_with_missing_data ####

# So, we know that quite a few values are missing in the "age" column, 
# and other columns are missing data, too, but why is this a problem?
# Let's try to compute the average age of passengers on the Titanic.

## HINT: You have to subset the "age" column with the age_null vector, and select values where age_null is False.
## 		 Then, divide the sum of the new vector by the length.

## Answer: good_ages = titanic_survival["age"][age_null == False]
##		   correct_mean_age = sum(good_ages) / len(good_ages)

import pandas as pd
mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])

# Unfortunately, mean_age is NaN.  This is because any calculations we do with a null value also result in a null value.
# This makes sense when you think about it -- how can you add a null value to a known value?
print(mean_age)

# What we have to do instead is filter the missing values out before we compute the mean.
age_null = pd.isnull(titanic_survival["age"])

# Use age_null to create a vector that only contains values from the "age" column that aren't "NaN".
# Compute the mean of the new vector, and assign the result to correct_mean_age.

nonnull_age = titanic_survival["age"][age_null == False]
correct_mean_age = sum(nonnull_age) / len(nonnull_age)

print(correct_mean_age)


#### Easier_ways_to_do_math ####

# Luckily, missing data is so common that pandas automatically filters for it with some methods.
# We can use the .mean() method to compute the mean, and it will automatically remove missing values

import pandas as pd

# This is the same value that we computed in the last screen, but it's much simpler.
# The ease of using the .mean() method is great, but it's important to understand how the underlying data looks.
correct_mean_age = titanic_survival["age"].mean()

# Assign the mean of the "fare" column to correct_mean_fare.

correct_mean_fare = titanic_survival["fare"].mean()

#### Computing_summary_statistics ####

# Let's compute some more advanced statistics about the data

# Passengers are divided into classes based on the "pclass" column
# Passengers can be in first class (1), second class (2), or third class (3)
# Let's compute the average fare for each class
passenger_classes = [1, 2, 3]
fares_by_class = {}
for pclass in passenger_classes:
    fare_for_class = None
    # Insert code here to compute the average fare for pclass
    # Assign the result to fare_for_class
    fare_for_class = (titanic_survival["fare"][titanic_survival["pclass"] == pclass]).mean()
    fares_by_class[pclass] = fare_for_class

    
# The code to the right isn't complete -- 
# fill in the missing code to compute fare_for_class for the given pclass.
# When the loop is done, fares_by_class should have 1, 2, and 3 as keys, 
# with the average fares as the corresponding values.
print(titanic_survival["fare"][0:30])

print(fares_by_class)

## Needed to subset the fares column based on the pclass at each iteration.


#### Making_pivot_tables ####

# Let's compute the survival probability for each passenger class in the Titanic.
# In order to help us out, we'll use the pivot_table method on dataframes -- 
# it makes doing analysis like what we did in the last screen much simpler.
# If you're familiar with pivot tables in excel, this will look familiar.

import pandas as pd
import numpy as np

# Let's compute the survival change from 0-1 for people in each class
# The closer to one, the higher the chance people in that passenger class survived
# The "survived" column contains a 1 if the passenger survived, and a 0 if not
# The pivot_table method on a pandas dataframe will let us do this
# index specifies which column to subset data based on 
# (in this case, we want to compute the survival percentage for each class)
# values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, 
# and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)

# First class passengers had a much higher survival chance
print(passenger_survival)

# Use the pivot_table method to compute the mean "age" for each passenger class ("pclass").
# Assign the result to passenger_age.

passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc=np.mean)

print(passenger_age)

## index is the grouping, values is the object that the aggfunc will operate on.


#### More_complex_pivot_tables ####

# We can use the pivot_table method to do more advanced things than we just did.
# For starters, we can make more complex pivot tables that show multiple values at once.

import numpy as np

# This will compute the mean survival chance and the mean age for each passenger class
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print(passenger_survival)

>#            age       survived 
># pclass
>#  1         39.16       0.62
>#  2         29.51       0.43
>#  3         24.82       0.26

# Make a pivot table that computes the mean "age", survival chance("survived"), 
# and "fare" for each embarkation port ("embarked").
# Assign the result to port_stats.
# Make sure to put the values list in the same order that the columns are given here.

port_stats = titanic_survival.pivot_table(index="embarked", values=["age", "survived", "fare"], aggfunc=np.mean)

print(port_stats)


#### Drop_missing_values ####

# We looked at how to remove missing values in a vector of data, but how about in a matrix?
# We can use the dropna method on pandas dataframes to do this.
# Using the method will drop any rows that contain missing values.
# There are also ways other than removing values to deal with missing data that we'll learn later.

import pandas as pd

# Drop all rows that have missing values
new_titanic_survival = titanic_survival.dropna()

# It looks like we have an empty dataframe now.
# This is because every row has at least one missing value.
print(new_titanic_survival)

# We can also use the axis argument to drop columns that have missing values
new_titanic_survival = titanic_survival.dropna(axis=1)
print(new_titanic_survival)

# We can use the subset argument to only drop rows if certain columns have missing values.
# This drops all rows where "age" or "sex" is missing.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
print(new_titanic_survival)


# Drop all rows in titanic_survival where the columns "age", "body", 
# or "home.dest" have missing values.
# Assign the result to new_titanic_survival.

new_titanic_survival = titanic_survival.dropna(subset=["age", "body", "home.dest"])
print(new_titanic_survival)


#### Row_indices_loc_OR_iloc ####

# In pandas, dataframes and series have row indexes.
# These work just like column indexes, and can take values like numbers, characters, and strings.

# See the numbers to the left of each row?
# Those are row indexes.
# Since the data has so many columns, it is split into multiple lines, but there are only 5 rows.
#print(titanic_survival.iloc[:5,:])


new_titanic_survival = titanic_survival.dropna(subset=["body"])
# Now let's print out the first 5 rows in new_titanic_survival
# The row indexes here aren't the same as in titanic_survival
# This is because we modified the titanic_survival dataframe to generate new_titanic_survival
# The row indexes you see here are the rows from titanic_survival that made it through the dropna method (didn't have missing values in the "body" column)
# They retain their original numbering, though
#print(new_titanic_survival.iloc[:5,:])

# We've been using the .iloc method to address rows and columns
# .iloc works by position (row/column number)
# The below code prints the fourth row in the data
#print(new_titanic_survival.iloc[4,:])

# Using .loc instead addresses rows and columns by index, not position
# This actually prints the first row, because it has index 3
print(new_titanic_survival.loc[3,:])


# Assign the row with index 25 to row_index_25.
# Assign the fifth row to row_position_fifth.

if new_titanic_survival.loc[3,:]["name"] == new_titanic_survival.iloc[0,:]["name"]:
    print(".loc uses index (dataframe index), .iloc uses position (row/column numbers)")

row_index_25 = new_titanic_survival.loc[25,:]
row_position_fifth = new_titanic_survival.iloc[4,:]


#### Column_indices_loc ####

# We can also index columns using the .loc[] method.

new_titanic_survival = titanic_survival.dropna(subset=["body"])

# This prints the value in the first column of the first row
print(new_titanic_survival.iloc[0,0])

# This prints the exact same value -- it prints the value at row index 3 and column "pclass"
# This happens to also be at row 0, index 0
print(new_titanic_survival.loc[3,"pclass"])

# Assign the value at row index 1100, column index "age" to row_1100_age.
# Assign the value at row index 25, column index "survived" to row_25_survived.

row_1100_age = new_titanic_survival.loc[1100,"age"]

row_25_survived = new_titanic_survival.loc[25,"survived"]


#### Reindexing_rows ####

# Remember how new_titanic_survival didn't have sequential row indexes?
# Each row retained its original index from titanic_survival.
# Sometimes it is useful to reindex, and make new indexes starting from 0.
# To do this, we can use the reset_index() method.

# The indexes are the original numbers from titanic_survival
new_titanic_survival = titanic_survival.dropna(subset=["body"])
print(new_titanic_survival)

# Reset the index to an integer sequence, starting at 0.
# The drop keyword argument specifies whether or not to make a dataframe column with the index values.
# If True, it won't, if False, it will.
# We'll almost always want to set it to True.
new_titanic_survival = new_titanic_survival.reset_index(drop=True)
# Now we have indexes starting from 0!
print(new_titanic_survival)

# Use the dropna method to remove rows that have missing values in the "age" or "boat" columns.
# Then, reindex the resulting dataframe so the row indexes start from 0.
# Assign the final result to titanic_reindexed.

new_titanic_survival1 = titanic_survival.dropna(subset=["age", "boat"])
titanic_reindexed = new_titanic_survival1.reset_index(drop=True)
print(titanic_reindexed)


#### Use_the_apply_function_on_columns ####

# The first step we need to take to figure out the age breakdown is to learn about the .apply() method.
# By default, .apply() will iterate through each column in a dataframe, and perform a function on it.
# The column will be passed into the function.
# The result from the function will be combined with all of the other results, and placed into a new series.
# The function results will have the same position as the column they were generated from.

import pandas as pd

# Let's look at a simple example.
# This function counts the number of null values in a series
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

# Compute null counts for each column
column_null_count = titanic_survival.apply(null_count)
print(column_null_count)

# Write a function to count up the number of non-null elements in a series.
# Use the .apply() method, along with your function, to run across all the columns in titanic_survival.
# Assign the result to column_non_null_counts.


## first attempt
def non_null_count(column):
    column_null = pd.isnull(column)
    not_null = column[column_null == False]
    return len(not_null)

column_non_null_counts = titanic_survival.apply(non_null_count)
print(column_non_null_counts)


## Actual answer  >> error in instructions.
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null == False]
    return len(null)
column_not_null_count = titanic_survival.apply(not_null_count)


#### Applying_a_function_to_a_row ####

# By passing in the axis argument, we can use the .apply() method to iterate over rows, not columns.

# This function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)

# If someone is under 18, they are a "minor". 
# If they are over 18, they are an "adult". 
# If their age is missing (is null), their age is "unknown".

# Make a function that returns the string "minor" if someone is under 18, 
# "adult" if they are over 18, and "unknown" if their age is null.
# Then, use the function along with .apply() to find the right label for everyone.
# Assign the result to age_labels.
# You can use isnull to check if a value is null or not.

def categorise_age(row):
    if row["age"] < 18:
        return "minor"
    elif row["age"] >= 18:
        return "adult"
    else:
        return "unknown"
        
age_labels = titanic_survival.apply(categorise_age, axis=1)
print(age_labels)


#### Computing_survival_percentage_by_age_group ####

# Now that we have age labels for everyone, let's make a pivot table to find survival chance by age group.

# The titanic_survival variable now has the added column "age_labels", which is our age labels series from the last screen.

# Make a pivot table that computes the mean survival chance("survived"), 
# for each age group ("age_labels").
# Assign the result to age_group_survival.

import numpy as np

print(list(titanic_survival.columns.values))

age_group_survival = titanic_survival.pivot_table(index=["age_labels"], values=["survived"], aggfunc=np.mean)

