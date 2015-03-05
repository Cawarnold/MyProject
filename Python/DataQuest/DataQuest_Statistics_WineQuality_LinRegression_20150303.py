## DataQuest_Statistics_WineQuality_LinRegression_20150303

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 15

# Basics: Predicting wine quality

# Learn about linear regression while predicting how highly experts would rate white wines.

# Next: https://learningwithdata.wordpress.com/2015/02/21/introduction-to-bayes-theorem-with-python/

# Connect with GitHub - https://dataquest.io/creator/github_link

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####

# we have some data on wine quality

# Each row is a different wine
# Each Column is an attribute of that wine

# Columns include: density, ph, alcohol, quality(rating_by_expert-1to10)

# goint to try to predict the quality using the different columns here
## Linear Regression, allows us to compare two sets of values, 
## train an algoritm to predict new values.

# eg. use density, feed in density data. feed in quality. pedict quality based on density.

#### Drawing_Lines ####

# Before we get started with linear regression, let's take a look at how to draw lines.
# The simplest possible line is y=x. 
# This means that the value of a point on the y-axis is the same as the corresponding value on the x-axis.

## Turn python list into numpy array using np.asarray

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
# Going by our formula, every y value at a position is the same as the x-value in the same position.
# We could write y = x, but let's write them all out to make this more clear.
y = [0, 1, 2, 3, 4, 5]

# As you can see, this is a straight line that passes through the points (0,0), (1,1), (2,2), and so on.
plt.plot(x, y)
plt.show()
plt.clf()

# Let's try a slightly more ambitious line.
# What if we did y = x + 1?
# We'll make x an array now, so we can add 1 to every element more easily.
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 1

# y is the same as x, but every element has 1 added to it.
print(y)

# This plot passes through (0,1), (1,2), and so on.
# It's the same line as before, but shifted up 1 on the y-axis.
plt.plot(x, y)
plt.show()
plt.clf()

# By adding 1 to the line, we moved what's called the y-intercept -- where the line intersects with the y-axis.
# Moving the intercept can shift the whole line up (or down when we subtract).


# Plot the equation y = x - 1, using the existing x variable.
# Plot the equation y = x + 10, using the existing x variable.

y = x - 1
plt.plot(x, y)
plt.show()
plt.clf()

y = x + 10
plt.plot(x, y)
plt.show()
plt.clf()


#### Working_with_slope ####

# Now that we have a way to move the line up and down, what about the steepness of the line?
# This was unchanged earlier -- the values on the line always went up 1 on the y-axis every time they went up 1 on the x-axis.
# What if we want to make a line that goes up 2 numbers on the y-axis every time it goes up 1 on the x-axis?
# This is where slope comes in. The slope is multiplied by the x-value to get the new y value.
# It looks like this: y=mx. 
# If we set the slope, m, equal to 2, we'll get what we want.

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y = 2 * x

# See how this line is "steeper" than before?  The larger the slope is, the steeper the line becomes.
# On the flipside, fractional slopes will create a "shallower" line.
# Negative slopes will create a line where y values decrease as x values increase.
plt.plot(x, y)
plt.show()
plt.clf()

# Plot the equation y = 4x, using the existing x variable.
# Plot the equation y = .5x, using the existing x variable.
# Plot the equation y = -2x, using the existing x variable.

y = 4 * x
plt.plot(x, y)
plt.show()
plt.clf()

y = (0.5) * x
plt.plot(x, y)
plt.show()
plt.clf()

y = (-2) * x
plt.plot(x, y)
plt.show()
plt.clf()


##### Starting_out_with_linear_regression ####

# In the last mission, we did some work with the r-value. 
# The r-value indicates how correlated two variables are. 
# This can range from no correlation to a negative correlation to a positive correlation.
# The more correlated two variables are, the easier it becomes to use one to predict the other. 
# For instance, if I know that how much I pay for my steak is highly positively correlated to the size of the steak (in ounces),
# I can create a formula that helps me predict how much I would be paying for my steak.
# The way we do this is with linear regression. 
# Linear regression gives us a formula, where if we plug in the value for one variable, we get the value for the other variable.

# The equation to create the formula takes the form y=mx+b.
# You might recognize pieces of this equation from the past two screens -- 
# we're just adding the intercept and slope into one equation.
# This equation is saying 
# "the predicted value of the second variable (y) is equal to the value of the first variable (x) times slope plus the intercept".
# We have to calculate values for m and b before we can use our formula.
# We'll calculate slope first -- 
# the formula is cov(x,y)σx2, 
# which is just the covariance of x and y divided by the variance of x.
# We can use the cov function to calculate covariance, and the .var() method on pandas series to calculate variance.


# The wine quality data is loaded into wine_quality
from numpy import cov

# Calculate the slope you would need to predict the "quality" column (y) using the "density" column (x).
# Assign the slope to slope_density.

import pandas as pd
# y = mx + b
# m = cov(x,y) / var(x)

y = wine_quality["quality"]
x = wine_quality["density"]

m = cov(x,y)[0,1] / x.var()
slope_density = m
print(m)


#### Finishing_linear_regression ####

# Now that we can calculate the slope for our linear regression line, we just need to calculate the intercept.
# The intercept is just how much "higher", or "lower" the average y point is than our predicted value.
# We can compute the intercept by taking the slope we calculated and doing this: y¯−mx¯. 
# So we just take the mean of the y values, and then subtract the slope times the mean of the x values from that.
# Remember that we can calculate the mean by using the .mean() method.

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()
  
# y = mx + b
# b = y¯ - mx¯ = mean(y) - m * mean(x)

def calc_intercept(x,y):
    return y.mean() - (calc_slope(x,y) * x.mean())
    
slope_density = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept_density = calc_intercept(wine_quality["density"], wine_quality["quality"])

print("y = ", slope_density, "x + ",intercept_density)    # y = -90.942 x + 96.277


#### Making_predictions ####

# Now that we've computed our slope and our intercept, we can make predictions about the y-values from the x-values.
# In order to do this, we go back to our original formula: y=mx+b, 
# and just plug in the values for m and b.
# We can then compute predicted y-values for any x-value. 
# This lets us make predictions about the quality of x-values that we've never seen. 
# For example, a wine with a density of .98 isn't in our dataset, 
# but we can make a prediction about what quality a reviewer would assign to a wine with this density.
# Depending on how correlated the predictor and the value being predicted are, the predictions may be good or bad.
# Let's look at making predictions now, and we'll move on to figuring out how good they are.

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

def calc_intercept(x,y):
    return y.mean() - (calc_slope(x,y) * x.mean())

slope_density = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept_density = calc_intercept(wine_quality["density"], wine_quality["quality"])

def predict_y_given_x(x_value):
    y = slope_density*x_value + intercept_density
    return y

print(predict_y_given_x(0.04)) # predict quality, given density.  # 92.639

#### Apply Function

#### Apply method

# Command

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

def calc_intercept(x,y):
    return y.mean() - (calc_slope(x,y) * x.mean())

slope_density = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept_density = calc_intercept(wine_quality["density"], wine_quality["quality"])

def function_stuff(row):
    return ((slope_density)*row["density"] + (intercept_density))

# apply method to each row of dataframe.
wine_quality['predicted_quality'] = wine_quality.apply(function_stuff, axis=1)
print(wine_quality['predicted_quality'])

print((wine_quality['predicted_quality'])==((slope_density)*wine_quality["density"]+(intercept_density))) #True



#### Answer

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

# Calculate the intercept given the x column, y column, and the slope
def calc_intercept(x, y, slope):
  return y.mean() - (slope * x.mean())
  
slope = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept = calc_intercept(wine_quality["density"], wine_quality["quality"], slope)

def compute_predicted_y(x):
  return x * slope + intercept

predicted_quality = wine_quality["density"].apply(compute_predicted_y)


#### My Answer, and proof that I'm right!

from numpy import cov

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

def calc_intercept(x,y):
    return y.mean() - (calc_slope(x,y) * x.mean())

slope_density = calc_slope(wine_quality["density"], wine_quality["quality"])
intercept_density = calc_intercept(wine_quality["density"], wine_quality["quality"])

def predict_y_given_x(row):
    return ((slope_density)*row + (intercept_density))

# apply method to each row of dataframe.
predicted_quality = wine_quality["density"].apply(predict_y_given_x)
print(type(predicted_quality))

def function_stuff(row):
    return ((slope_density)*row["density"] + (intercept_density))

# apply method to each row of dataframe.
wine_quality['predicted'] = wine_quality.apply(function_stuff, axis=1)

import pandas as pd
predicted_quality_1 = pd.Series([item for item in wine_quality['predicted']])
print(type(predicted_quality_1))

for i, item in enumerate(predicted_quality_1):
    print(item == predicted_quality[i])  ##True

predicted_quality = predicted_quality_1  # Previous Error because answer wanted pd.Series not a list.


#### Finding_error ####

# Now that we know how to make a regression line manually, let's look at an easier way to do it, using a function from scipy.
# The linregress function makes it simple to do linear regression.
# Now that we know a simpler way to do linear regression, let's look at how to figure out if our regression is good or bad.
# We can plot out our line and our actual values, and see how far apart they are on the y-axis.
# We can also compute the distance between each prediction and the actual value -- these distances are called residuals.
# If we add up the sum of the squared residuals, we can get a good error estimate for our line.
# We have to add the squared residuals, because just like differences from the mean, the residuals add to 0 if they aren't squared.

# To put it in math terms, the sum of squared residuals is:
# ∑i=1n(yi−y^i)2. 
# y^i (y hat i) is the predicted y value at position i.


from scipy.stats import linregress

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- 
# for now, don't worry about them.

# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)				#-90.94
print(intercept)			#98.27

print(r_value)				#-0.307
print(p_value)				#1.727
print(stderr_slope)			#4.027

# Using the given slope and intercept, calculate the predicted y values.
# Subtract each predicted y value from the corresponding actual y value, 
# square the difference, and add all the differences together.
# This will give you the sum of squared residuals. Assign this value to rss.

# overview:  predicted_y = slope * actual_x + intercept
# overview: rss = (sum(predicted_y - actual_y)**2)

slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

def predict_y_given_x(row):
    return ((slope)*row + (intercept))
    
predicted_quality = wine_quality["density"].apply(predict_y_given_x)  # is a pandas series
actual_quality = wine_quality["quality"] # is a pandas series
print(type(actual_quality) == type(predicted_quality))

rss = 0
for i, item in enumerate(predicted_quality):
    rss = rss + (actual_quality[i] - predicted_quality[i])**2
    
print(rss)					#3478.689

## CORRECT!

# Answer:
import numpy
predicted_y = numpy.asarray([slope * x + intercept for x in wine_quality["density"]])   #is a numpy array
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)


#### Standard_error ####

# From the sum of squared residuals, we can get to the standard error. 
# The standard error is similar to the standard deviation, 
# but it tries to make an estimate for the whole population of y-values -- 
# even the ones we haven't seen yet that we may want to predict in the future.

# The standard error lets us quickly determine how good or bad a linear model is at prediction.
# The equation for standard error is √RSS/n−2.
# You take the sum of squared residuals, divide by the number of y-points minus two, and then take the square root.
# You might be wondering about why 2 is subtracted -- 
# this is because of differences between the whole population and a sample. This will be explained in more depth later on.

# standar_error = √(RSS/(n-2))


from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)


# Calculate the standard error using the above formula.

# Calculate what percentage of actual y values are within 1 standard error of the predicted y value. 
# Assign the result to within_one.
# Calculate what percentage of actual y values are within 2 standard errors of the predicted y value. 
# Assign the result to within_two.
# Calculate what percentage of actual y values are within 3 standard errors of the predicted y value. 
# Assign the result to within_three.

# Assume that within means "up to and including", 
# so be sure to count values that are exactly 1, 2, or 3 standard errors away.

actual_y = wine_quality["quality"]

standard_error = (rss/(len(actual_y)-2))**(1/2)

print(standard_error)           #0.8429

# (list_actual_y - (list_predicted_y)*(+-1)) / (list_predicted_y)*(+-1)

## Notes to help understand what they are asking for:
##for x in list_of_xs:
##    if actual_value <= predicted_y*(+-1 standarderror)
##        list_of_actual_values_in append(x)
        

within_one_percentage_list = [item for i,item in enumerate(actual_y) if abs(item - predicted_y[i]) <= 1*standard_error]
within_two_percentage_list = [item for i,item in enumerate(actual_y) if abs(item - predicted_y[i]) <= 2*standard_error]
within_tre_percentage_list = [item for i,item in enumerate(actual_y) if abs(item - predicted_y[i]) <= 3*standard_error]

#within one/two/three standard errors of predicted y values.
within_one = len(within_one_percentage_list) / len(actual_y)
within_two = len(within_two_percentage_list) / len(actual_y)
within_three = len(within_tre_percentage_list) / len(actual_y)

print("within one standard error", within_one, "two", within_two, "three", within_three)

# within one standard error = 0.684565
# within two standard error = 0.935688
# within three standard error = 0.99367


## CORRECT!

# Answer:

stderr = (rss / (len(wine_quality["quality"]) - 2)) ** .5

def within_percentage(y, predicted_y, stderr, error_count):
  within = stderr * error_count

  differences = abs(predicted_y - y)
  lower_differences = [d for d in differences if d <= within]

  within_count = len(lower_differences)
  return within_count / len(y)

within_one = within_percentage(wine_quality["quality"], predicted_y, stderr, 1)
within_two = within_percentage(wine_quality["quality"], predicted_y, stderr, 2)
within_three = within_percentage(wine_quality["quality"], predicted_y, stderr, 3)




####

# Regressions line: Predict y using y = mx + b, m is the slope, b is the intercept
# the slope, m,is calculated as covariance of x and y divided by the variance of x: cov(x, y) / var(x)
# the intercept, b, is calculated as the mean of y minus the slope times the mean of x: y¯−mx¯

# Residual sum of squares: rss checks the error between the prediction using y = mx + b and the actual values.
# rss is calculated by summing (the predicted values of y minus the actual values of y) squared. 

# overview: regression_line = y = mx + b
# overview: slope = m = cov(x,y) / var(x)
# overview: intercept = b = y¯ - mx¯ = mean(y) - m * mean(x)
# overview: predicted_y = slope * actual_x + intercept
# overview: rss = (sum(predicted_y - actual_y)**2)
# overview: standar_error = (rss/(n-2))**(1/2)
