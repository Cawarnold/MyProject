## DataQuest_MatPlotLib_ForestFires_PlottingData_20150217

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 11

# Basics: What are some characteristics of forest fires?

# Learn the basics of making charts and graphs while visualizing forest fire data from Montesinho National Park

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# Going to analyse forest fire data from Montesinho, Portugal.

# Park has been split up into a 9x9 grid. 

# 5
# 4
# 3
# 2
# 1
#   1  2  3  4  5 ...

# x and y coordinates.

# Columns:   x-axis, y-axis, month, dayofweek,  temp, windspeed, rain, area
#if area was very small, then area would get 0.

# a few basics on plotting.
# we use x and y in plots.
# 2 dimensional - refers to 2 values which are paired. 

# In python, we start with a blank canvas, which gets drawn on using commands.

# so once, we're done with one plot we'll need to clear the first plot.

#### Making_a_scatter_plot ####

# A scatter plot is used to show the relationship between two variables --- in our case, two columns of data.
# A scatter plot can show a general trend between two variables, and can help to make sense of messy data.

import matplotlib.pyplot as plt

# Let's say that we want to graph weight vs height.
weight = [600,150,200,300,200,100,125,180]

# Height is in inches
height = [60,65,73,70,65,58,66,67]

# Now let's make a plot.
# The first input will be the x-axis, and the second will be the y-axis.
plt.scatter(weight, height)
plt.show()

# Don't forget to clear the figure after showing it!
plt.clf()

# Let's get data on airline trip length in minutes vs cost in dollars.
airline_trip_length = [100,500,200,800,300,100]
airline_trip_cost = [200,1000,500,3000,1000,300]

# Create a scatterplot that graphs airline_trip_length on the x-axis, 
# and airline_trip_cost on the y-axis.

plt.scatter(airline_trip_length, airline_trip_cost)
plt.show()

# Don't forget to clear the figure after showing it!
plt.clf()



