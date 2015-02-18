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
plt.clf()


#### Plotting_fire_data ####

# Now, that we know how to make scatter plots, let's make a couple that describe our fire data.

import matplotlib.pyplot as plt
# The forest fire data has been loaded into the forest_fires variable as a pandas dataframe.
# We can plot the X column from the dataframe against the Y column.
# This will show us the spatial positions of all the fires on a 10x10 grid.
plt.scatter(forest_fires["X"], forest_fires["Y"])
plt.show()

# And clearing the figure
plt.clf()

# Plot the "wind" column on the x axis and the "area" column on the y axis.
# Plot the "temp" column on the x axis and the "area" column on the y axis.

plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.show()
plt.clf()
plt.scatter(forest_fires["temp"], forest_fires["area"])
plt.show()
plt.clf()


#### Making_a_line_chart ####

# Another type of chart is a line chart.
# This is similar to a scatter plot, but the points are connected into a line.
# This generally makes sense for trends and other data that have a clear direction.

import matplotlib.pyplot as plt
# We can use the plt.plot() function to make a line plot.
plt.plot(forest_fires["temp"], forest_fires["area"])
plt.show()
plt.clf()

# Hmm, the above plot looks really strange (check in the plots area to look for yourself)
# The reason it does is because we didn't sort based on the x-axis variable first.
# If we don't sort, points are placed wherever they occur in the data, 
# which means lines can be drawn all across the figure.
# Sorting puts all of the values in the order of the x axis, which means a line is drawn from left to right.
forest_fires = forest_fires.sort(["temp"])
plt.plot(forest_fires["temp"], forest_fires["area"])
plt.show()
plt.clf()

# The above plot looks much better!

# Plot "rain" on the x axis and "area" on the y axis.
# Plot "wind" on the x axis and "area" on the y axis.
# Remember to sort on the x-axis values first!

forest_fires = forest_fires.sort(["rain"])
plt.plot(forest_fires["rain"], forest_fires["area"])
plt.show()
plt.clf()

forest_fires = forest_fires.sort(["wind"])
plt.plot(forest_fires["wind"], forest_fires["area"])
plt.show()
plt.clf()


#### Labeling_the_chart ####

# Let's add some axis labels and titles to our charts.

import matplotlib.pyplot as plt

# Make a scatter plot of X and Y fire positions
plt.scatter(forest_fires["X"], forest_fires["Y"])

# Set the x axis label
plt.xlabel('X position in grid')
# Set the y axis label
plt.ylabel('Y position in grid')
# Set the title
plt.title("Grid positions of fires in Montesinho national park")
plt.show()
plt.clf()

# Make a scatterplot with the "wind" column on the x axis and the "area" column on the y axis.
# Give the chart the title "Wind speed vs fire area", 
# the y axis label "Area consumed by fire", 
# and the x axis label "Wind speed when fire started".

plt.scatter(forest_fires["wind"], forest_fires["area"])

# Set the x axis label
plt.xlabel('Wind speed when fire started')
# Set the y axis label
plt.ylabel('Area consumed by fire')
# Set the title
plt.title("Wind speed vs fire area")
plt.show()
plt.clf()


#### Nicer_looking_plots ####

import matplotlib.pyplot as plt

# Print all available styles
print(plt.style.available)

# Use the ggplot style for plotting
plt.style.use('ggplot')

plt.scatter(forest_fires["wind"], forest_fires["area"])
# This plot looks a lot better!
plt.show()
plt.clf()

# Switch to the "fivethirtyeight" style.
# Plot "rain" on the x axis and "area" on the y axis.

plt.style.use('fivethirtyeight')
plt.scatter(forest_fires["rain"], forest_fires["area"])
# This plot looks a lot better!
plt.show()
plt.clf()


#### Making_a_bar_plot ####

# The last type of plot we'll look at right now is the bar plot.
# Bar plots graph categories and their values against each other.
# For example, we can graph month against the area that fires consumed in that month.

import matplotlib.pyplot as plt
import numpy
# The pivot_table method will return a new array containing a summary of the data.
# This pivot table will have the Y position of the fire as the index, 
# and the average area of forest burned per fire as the values.
# It will return a vector, or one dimensional array.
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)

import matplotlib.pyplot as plt
plt.style.use("ggplot")

# This gets the index values of the vector, in this case, the sorted y positions
y_index = area_by_y.index
plt.bar(y_index, area_by_y)
plt.show()
plt.clf()

# Make a bar plot with "X" on the x axis, and "area" on the y axis.
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
print(area_by_x)
x_index = area_by_x.index
print(x_index)
plt.style.use("ggplot")
plt.bar(x_index, area_by_x)
plt.show()
plt.clf()




