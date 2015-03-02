## DataQuest_Statistics_NBAplayers_SdevCorr_20150302

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 14

# Basics: Look at NBA player data

# Learn about standard deviation and correlation while looking at data from the National Basketball League (NBA).	


#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####

# NBA data, basketball.

#2013 to 2014 season
# each row is a player
# each column is data about how they played in season
# columns such as, pts, shots, ...


#### The_mean_as_the_center ####

# We have looked briefly at the mean before, but it has an interesting property.
# If we subtract the mean of a set of numbers from each of the numbers, the differences will always add up to zero.
# This is because the mean is the "center" of the data. 
# All of the differences that are negative will always cancel out all of the differences that are positive.
# Let's look at some examples to verify this.
# Let's also get familiar with the mathematical symbol for the mean -- x¯x¯x¯ -- 
# this symbol means "the average of all the values in x". 
# The fact that x is lowercase but bold means that it is a vector. The bar over top means "the average of".

# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  Try changing the values around and verifying that it equals 0 if you want.
print(sum(differences))

# We can use the median function from numpy to find the median
# The median is the "middle" value in a set of values -- if you sort the values in order, it's the one in the center 
# (or the average of the two in the center if there are an even number of items in the set)
# You'll see that the differences from the median don't always add to 0.  
# You might want to play around with this and think about why that is.
from numpy import median


# Find the median of the values list. Assign the result to values_median.
# Subtract the median from each element in values. Sum up all of the differences, 
# and assign the result to median_difference_sum.

values_median = median(values)

differences1 = [item - values_median for item in values]
median_difference_sum = (sum(differences1))
print((sum(differences1)))


#### Finding_variance ####

# Let's look at variance in the data.
# Variance tells us how "spread out" the data is around the mean.
# We looked at kurtosis earlier, which measures the shape of a distribution.
# Variance directly measures how far from the mean the average element in the data is.
# We calculate variance by subtracting every value from the mean, squaring the results, and averaging them.
# Mathemically, this looks like σ2=∑i=1n(xi−x¯)2nσ2=∑i=1n(xi−x¯)2nσ2=∑i=1n(xi−x¯)2n. 
# σ2σ2σ2 is variance, ∑ni=1∑ni=1∑ni=1 means "the sum from 1 to n", where n is the number of elements in a vector. 
# The formula does the exact same thing we just described, but is the most common way to show it.
# The "pf" column in the data is the total number of personal fouls each player had called on them in the season -- 
# let's look at its variance.

import matplotlib.pyplot as plt
import pandas as pd
# The nba data is loaded into the nba_stats variable.
# Find the mean value of the column
pf_mean = nba_stats["pf"].mean()
# Initialize variance at zero
variance = 0
# Loop through each item in the "pf" column
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value
    difference = p - pf_mean
    # Square the difference -- this ensures that the result isn't negative
    # If we didn't square the difference, the total variance would be zero
    # ** in python means "raise whatever comes before this to the power of whatever number is after this"
    square_difference = difference ** 2
    # Add the difference to the total
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])
print(variance)


# Compute the variance of the "pts" column in the data -- this it total points scored.
# Assign the result to point_variance.

pts_mean = nba_stats["pts"].mean()
variance = 0
for player in nba_stats["pts"]:
    difference = player - pts_mean
    square_difference = difference ** 2
    variance = variance + square_difference
point_variance = variance / len(nba_stats["pts"])
print(point_variance)   #220836


#### Order_of_operation ####

# We've been multiplying and dividing values, but we haven't really discussed order of operations yet.
# Order of operations define which mathematical operations occur in which sequence.
# Think about 2 * 5 - 1 -- depending on whether we do the multiplication first, or the subtraction first, the result will change.
# If we multiply first, we get 10 - 1, which equals 9.
# If we subtract first, we get 2 * 4, which equals 8.
# We definitely want the results of these operations to be consistent -- we don't want to sometimes get 8, and sometimes get 9.
# Because of this, we have an order of operations.
# At the top is raising something to a power (x ** y), then multiplication (x * y) and division (x / y) are equal, 
# and then addition (x + y) and subtraction (x - y) are equal.
# So raising something to a power will always happen first, then any multiplication/division, and last any addition/subtraction.
# We'll play around with this to get a better feel for it.

# You might be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication first, or the division first -- the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction -- otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2 -- the result is the same (2/2 == 2 * 1/2)
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same thing is true for subtraction and addition
# In this case, we need to convert subtraction into adding a negative number -- if we don't we'll end up subtracting more than we expect
b = 10 - 8 + 5
# Add -8 instead of subtracting 8
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = 10 / 2 + 5
d = 3 - 1 / 2 * 2

# Attempt 1
c = (10 * 2) + 5
d = (3 - 1) / (2 * 2)

print(c)
print(d)


# Change the mathematical operations around so that c equals 25, and d equals .5.

# If you change the addition in the formula for c to multiplication, you get 25.
# If you change the multiplication in the formula for d to subtraction, you get .5.

# Answer
c = 10 / 2 * 5
d = 3 - 1 / 2 - 2
print(c)


#### Using_parentheses ####

# Parentheses can be used to "override" the order of operations and make something happen first.
# For example 10 - 2 / 2 will equal 9, because the division happens before the subtraction.
# If we write (10 - 2) / 2, the parentheses "force" the part inside to happen first, so we end up with 5/2.


a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the order of operations is used inside to determine the order.
a_paren = 50 * (50 - 10 / 5)

b = 10 * 10 + 100
c = 8 - 6 * 100

# Use parentheses to make b equal 1100.
# Use parentheses to make c equal 200.

b = 10 * (10 + 100)
c = (8 - 6) * 100
print(b)
print(c)


#### Fractional_powers ####

# Before we explore variance a little more, let's take a quick look at exponents.
# We did difference ** 2 in the last screen, which squared the difference -- this is equal to difference * difference.
# We could cube the difference by doing difference ** 3 -- this is equal to difference * difference * difference.
# This same pattern holds true as we raise to higher powers, like 4, 5, and so on.
# We can also take roots of numbers with the same syntax.
# difference ** (1/2) will take the square root -- we need to put the fraction in parentheses 
# because raising a value to a power always happens first normally.
# difference ** (1/3) will take the cube root. And so on with smaller fractions.

a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)

# Raise 11 to the fifth power. Assign the result to e.
# Take the fourth root of 10000. Assign the result to f.

print(a,b,c,d)
print(d == 4)   #False

e = 11 ** 5
f = 10000 ** (1/4)

print(e,f)


#### Calculating_standard_deviation #####

# A commonly used way to refer to how far data points are from the mean is called standard deviation.
# It is typical to measure what percentage of the data is within 1 standard deviation of the mean,
# or two standard deviations of the mean.
# Standard deviation is a very useful concept, and is a great way to measure how spread out data is.
# Luckily for us, standard deviation is just the square root of the variance.
# Here's the mathematical formula for standard deviation -- 
# σ=∑i=1n(xi−x¯)2n−−−−−−−−−−−⎷σ=∑i=1n(xi−x¯)2n−−−−−−−−−−−⎷σ=∑i=1n(xi−x¯)2n−−−−−−−−−−−⎷

# Attempt 1

# The nba stats are loaded into the nba_stats variable.

# Make a function that calculates the standard deviation of a given column in the nba_stats data.
# Use the function to calculate the standard deviation for the minutes played column ("mp"). 
# Assign the results to mp_dev.
# Use the function to calculate the standard deviation for the assists column ("ast"). 
# Assign the results to ast_dev.

print(type(nba_stats))

import numpy
import pandas as pd

def st_dev_nba(col_name):
    col_mean = nba_stats[str(col_name)].mean()
    variance = 0
    for player in nba_stats[str(col_name)]:
        difference = player - col_mean
        square_difference = difference ** 2
        variance = variance + square_difference
    col_variance = variance / len(nba_stats[str(col_name)])
    return col_variance
    
print(st_dev_nba("pts"))

mp_dev = st_dev_nba("mp")
ast_dev = st_dev_nba("ast")

print(mp_dev, "\n", ast_dev)  # 220836.996, 803399.676, 17130.436

# Errors because this ^^^ is actually the deviation.

# Attempt 2

def st_dev_nba(col_name):
    col_mean = nba_stats[str(col_name)].mean()
    variance = 0
    for player in nba_stats[str(col_name)]:
        difference = player - col_mean
        square_difference = difference ** 2
        variance = variance + square_difference
    col_variance = variance / len(nba_stats[str(col_name)])
    col_standard_deviation = col_variance ** (1/2)
    return col_standard_deviation

mp_dev = st_dev_nba("mp")
ast_dev = st_dev_nba("ast")

print(mp_dev, "\n", ast_dev)   # 896.326, 130.883


#### Find_standard_deviation_distance ####

# Calculate how many standard deviations a data point is from the mean

# The standard deviation is very useful because it lets us compare points in a distribution to the mean.
# We can say that a certain point is "two standard deviations away from the mean".
# This gives us a way to compare how spread out values are across different charts.














