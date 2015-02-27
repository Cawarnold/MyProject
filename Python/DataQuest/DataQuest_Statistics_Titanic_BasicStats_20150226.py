## DataQuest_Statistics_Titanic_BasicStats_20150226

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 13

# Basics: Looking at Titanic survival data (Calculating_basic_stats_for_age)

# Learn the basics of statistics while looking at survival data from the Titanic.

#####################################

Overview of Useful code:
Statistics _is, at the core, about counting _and measuring. (Equal_interval_scales)
Make a line plot _with discrete _and conitinuous data. (Discrete_and_continuous_scales)
Scales can also have a zero point at different places. (Scale_starting_points)
Compute the average value of _all the survey responses. (Ordinal_scales)
We can also have categorical scales, that have category labels. (Categorical_scales)
Frequency histogram that helps us visualize counts of data. (Frequency_histograms)
Histograms use something called bins to count up values. (Histogram_bins)
Histogram shapes can show you how the data _is distibuted. (Skew)
Histogram shapes can show you how the data _is distibuted. (Kurtosis)
Histogram shapes can show you how the data _is distibuted. (Modality)
Central tendancy measures how likely points _in the data are to cluster around a central point. (Measures_of_central_tendancy_mean)
Central tendancy measures how likely points _in the data are to cluster around a central point. (Measures_of_central_tendancy_median)

Using .dropna to clean the missing data. (Cleaning_missing_titanic_data)
Analyse the cleaned data using a histogram, the mean _and the median. (Plotting_age)
Calculate the mean, median, skew, kurtosis of age, _from the clean titanic survival data. (Calculating_basic_stats_for_age)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Equal_interval_scales ####

# Statistics is, at the core, about counting and measuring.
# In order to do both effectively, we have to define scales on which we can count.
# One type of scale is called equal interval.

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]

# Compute the mean of car_speeds and assign it to mean_car_speed.
# Compute the mean of earthquake_intensities and assign the result to mean_earthquake_intensities. 
# This value will not be meaningful, because we can't average values on a logarithmic scale this way.

import pandas as pd
mean_car_speed = sum(car_speeds) / len(car_speeds)
print(mean_car_speed)

mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)
print(mean_earthquake_intensities)


#### Discrete_and_continuous_scales ####

# Scales can be discrete or continuous

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]  #continuous
cars_in_parking_lot = [5,6,4,2,1,7,8]     #discrete

import matplotlib.pyplot as plt

# Make a line plot with day_numbers on the x axis and snail_crawl_length on the y axis.
# Make a line plot with day_numbers on the x axis and cars_in_parking_lot on the y axis.

plt.plot(day_numbers, snail_crawl_length)
plt.show()
plt.clf()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()
plt.clf()


##### Scale_starting_points ####

# Scales can also have a zero point at different places.
# Think of the number of cars in a parking lot.
# Zero cars in the lot means that there are absolutely no cars at all in the lot, so absolute zero is at 0 cars. 
# You can't have negative cars.
# Now, think of degrees fahrenheit.
# Zero degrees doesn't mean that there isn't any warmth -- the degree scale can also be negative, 
# and absolute zero (when there is no warmth at all) is at -459.67 degrees.
# Scales that don't have their absolute zero point at 0 don't enable us to take meaningful ratios.

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]

# You can convert a scale that doesn't have absolute zero at zero to a scale that does 
# by substracting absolute zero from all of the values on the scale.

population_zero = yearly_town_population
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]


#### Ordinal_scales ####

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]

# Compute the average value of all the survey responses, and assign it to average_smoking.

# You'll want to make a new list that assigns 0 to any response in survey_responses that is "none", 
# 1 to any response that is "a few", and so on.
# Then, calculate the sum of that list, and divide by the length to get the average response.

survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)

list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.


#### Categorical_scales ####

# We can also have categorical scales, that have category labels.
# One example is gender, which can be male or female.
# There isn't an ordering between male and female -- one is not greater than or less than the other, so it's not an ordinal scale.

gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]

# You can use a list comprehension to filter out the values in savings where the corresponding gender is "male" or "female". 
# You can do this by looping over the range() from 0 to the length of gender.

# Answer
male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)


#### Frequency_histograms ####

# There's a plot called a frequency histogram that helps us visualize counts of data a lot better.
# The idea is to count up how many times a value occurs in a list, then graph the values on the x-axis, and the counts on the y-axis.

# Let's say that we watch cars drive by, and measure average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()
plt.clf()



#### Histogram_bins ####

# Histograms use something called bins to count up values.

average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()
plt.clf()
plt.clf()

# Plot a histogram of average_speed with only 2 bins.
plt.hist(average_speed, bins=2)
plt.show()
plt.clf()


#### Skew ####

import matplotlib.pyplot as plt

# This plot is negatively skewed.
plt.hist(test_scores_negative)
plt.show()
plt.clf()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew

positive_skew = skew(test_scores_positive)
print(positive_skew)    #0.585
negative_skew = skew(test_scores_negative)
print(negative_skew)    #-0.563
no_skew = skew(test_scores_normal)
print(no_skew)          #0.0124


#### Kurtosis ####

# Kurtosis measures whether the distribution is short and flat, or tall and skinny.

import matplotlib.pyplot as plt

# This plot is short, making it platykurtic
# See how the values are distributed pretty evenly, and there isn't a huge cluster in the middle?
# Students had a wide variation in their performance
plt.hist(test_scores_platy)
plt.show()
plt.clf()

# This plot is tall, and is leptokurtic
# Most students did very similarly to the others
plt.hist(test_scores_lepto)
plt.show()
plt.clf()

# This plot is in between, and is mesokurtic
plt.hist(test_scores_meso)
plt.show()
plt.clf()

# We can measure kurtosis with the kurtosis function
# Negative values indicate platykurtic distributions, 
# positive values indicate leptokurtic distributions, 
# and values close to 0 are mesokurtic
from scipy.stats import kurtosis

kurtosis_platykurtic = kurtosis(test_scores_platy)
print(kurt_platy)	# -0.9498
kurtosis_leptokurtic = kurtosis(test_scores_lepto)
print(kurt_lepto)	# 0.00396
kurtosis_mesokurtic = kurtosis(test_scores_meso)
print(kurt_meso)	#-0.0561


##### Modality ####

# Modality is another parameter of distributions.
# Modality refers to the number of modes, or peaks, in a distribution.
# Real-world data often is unimodal (only has one mode)

import matplotlib.pyplot as plt

# This plot has two peaks, and is bimodal
# This could happen if one group of students learned the material, and one learned something else, for example.
plt.hist(test_scores_bi)
plt.show()
plt.clf()

# Often, the best way to detect multimodality is to observe the plot.

# Plot test_scores_multi, which has four peaks.
plt.hist(test_scores_multi)
plt.show()
plt.clf()


#### Measures_of_central_tendancy_mean ####

# Central tendancy measures how likely points in the data are to cluster around a central point.
# The mean is just the sum of all the elements in an array divided by the number of elements.

import matplotlib.pyplot as plt
# We're going to put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot
plt.axvline(mean_test_score)
plt.show()
plt.clf()

mean_normal = test_scores_normal.mean()
print(mean_normal)		# 50.200
mean_negative = test_scores_negative.mean()
print(mean_negative)	# 82.809
mean_positive = test_scores_positive.mean()
print(mean_positive)	# 16.816


#### Measures_of_central_tendancy_median ####

# Another measure of central tendency is the median.
# This is the midpoint of an array.
# You have to sort the array, and then take the value in the middle.
# If two values are in the middle (if there are an even number of items in the array), then you take the mean of the two middle values.
# The median is less sensitive to very large or very small values (outliers), and is a more realistic center of the distribution.

# Let's plot the mean and median side by side in a negatively skewed distribution.
import numpy
import matplotlib.pyplot as plt

plt.hist(test_scores_negative)
median = numpy.median(test_scores_negative)
plt.axvline(median, color="b")
plt.axvline(test_scores_negative.mean(), color="r")
plt.show()
plt.clf()

# Plot a histogram for test_scores_positive.
# Add in a blue line for the median.
# Add in a red line for the mean.
plt.hist(test_scores_positive)
plt.axvline(numpy.median(test_scores_positive), color = "b")
plt.axvline(test_scores_positive.mean(), color = "r")
plt.show()
plt.clf()


#### Cleaning_missing_titanic_data ####


print(titanic_survival.shape)
# Remove the NaN values in the "age" and "sex" columns.
# Assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
print(new_titanic_survival.shape)


#### Plotting_age ####

# Now that we have cleaned up data, let's analyze it.

# The cleaned up data has been loaded into the titanic_survival variable
import matplotlib.pyplot as plt
import numpy

# Plot a histogram of the "age" column in titanic_survival.
# Add in a blue line for the median.
# Add in a red line for the mean.

plt.hist(titanic_survival["age"])
plt.axvline(numpy.median(titanic_survival["age"]),color = "b")
plt.axvline((titanic_survival["age"]).mean(),color = "r")

plt.show()
plt.clf()


#### Calculating_basic_stats_for_age ####

# The age distribution was very interesting, and showed that a lot of people in their 20s-40s were travelling without children.
# Now that we know what the distribution looks like, let's calculate the parameters and central tendency measures.

# The cleaned up data has been loaded into the titanic_survival variable

# Assign the mean of the "age" column of titanic_survival to mean_age.
# Assign the median of the "age" column of titanic_survival to median_age.
# Assign the skew of the "age" column of titanic_survival to skew_age.
# Assign the kurtosis of the "age" column of titanic_survival to kurtosis_age.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

mean_age = (titanic_survival["age"]).mean()
median_age = np.median(titanic_survival["age"])

skew_age = skew(titanic_survival["age"])
kurtosis_age = kurtosis(titanic_survival["age"])

print(mean_age)       # 29.88
print(median_age)     # 28.0
print(skew_age)       # 0.407
print(kurtosis_age)   # 0.141




########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#### Equal_interval_scales ####

# Statistics is, at the core, about counting and measuring.
# In order to do both effectively, we have to define scales on which we can count.
# One type of scale is called equal interval.
# Think of the speed of a car. 5 miles per hour is 5 miles per hour, no matter what the current speed is.
# The difference between 60 and 55 miles per hour will always equal the difference between 10 and 5 miles per hour in real-world terms.
# Another type of scale is a logarithmic scale.
# The difference between a 6 and a 5 on the Richter scale is more than the difference between a 4 and 5.
# This is because each number on the Richter scale means that the earthquake had 10 times the shaking amplitude of the previous number.
# So, a 6 is 10 times more powerful (technically, powerful is the wrong term, but it makes explaining easier) than a 5,
# which is 10 times more powerful than a 4. A 6 is 100 times as powerful as a 4.
# We can calculate the mean of values on an equal interval scale by adding up all the values and dividing by the number of values.
# We could do the same for values on a non-equal interval scale, but the results wouldn't be meaningful, 
# because of the differences between units.

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]

# Compute the mean of car_speeds and assign it to mean_car_speed.
# Compute the mean of earthquake_intensities and assign the result to mean_earthquake_intensities. 
# This value will not be meaningful, because we can't average values on a logarithmic scale this way.

import pandas as pd

mean_car_speed = sum(car_speeds) / len(car_speeds)
print(mean_car_speed)

mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)
print(mean_earthquake_intensities)


#### Discrete_and_continuous_scales ####

# Scales can be discrete or continuous
# Think of someone marking down the number of inches a snail crawls in a day.
# The snail could crawl 1 inch, 2 inches, 1.5 inches, 1.51 inches, or any other number, and it would be a valid observation.
# This is because inches is a continuous scale, and even fractions of an inch are possible.
# Now, think of someone counting the number of cars in a parking lot each day.
# 1 car, 2 cars, and 10 cars are valid measurements, but 1.5 cars isn't.
# Having half of a car isn't a meaningful quantity, as cars are understood to be discrete -- 
# you can't have 52% of a car, you either have a car, or you don't.
# You can still average items on discete scales -- 
# you could say "1.75 cars are in this parking lot each day, on average", 
# but any daily value for number of cars in the parking lot would need to be a whole number.


day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt

# Make a line plot with day_numbers on the x axis and snail_crawl_length on the y axis.
# Make a line plot with day_numbers on the x axis and cars_in_parking_lot on the y axis.

plt.plot(day_numbers, snail_crawl_length)
plt.show()
plt.clf()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()
plt.clf()


##### Scale_starting_points ####

# Scales can also have a zero point at different places.
# Think of the number of cars in a parking lot.
# Zero cars in the lot means that there are absolutely no cars at all in the lot, so absolute zero is at 0 cars. 
# You can't have negative cars.
# Now, think of degrees fahrenheit.
# Zero degrees doesn't mean that there isn't any warmth -- the degree scale can also be negative, 
# and absolute zero (when there is no warmth at all) is at -459.67 degrees.
# Scales that don't have their absolute zero point at 0 don't enable us to take meaningful ratios.
# If 4 cars parked in the lot yesterday, and 8 park today, I can safely say that twice as many cars are in the lot today.
# But, if it was 32 degrees fahrenheit yesterday, and it is 64 degrees today, I can't say that it is twice as warm today as yesterday.

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]

# Convert the values in fahrenheit_degrees so that absolute zero is at the value 0. 
# If you think this is already the case, don't change anything. 
# Assign the result to degrees_zero.
# Convert the values in yearly_town_population so that absolute zero is at the value 0. 
# If you think this is already the case, don't change anything. 
# Assign the result to population_zero.


#Attempt 1
degrees_zero = [(item - 459.67) for item in fahrenheit_degrees]
print(degrees_zero)

population_zero = yearly_town_population
print(population_zero)

# Hint
# You can convert a scale that doesn't have absolute zero at zero to a scale that does 
# by substracting absolute zero from all of the values on the scale.

# Answer
population_zero = yearly_town_population
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]


#### Ordinal_scales ####

# So far, we've looked at equal interval and discrete scales, where all of the values are numbers.
# But, we can also have ordinal scales, where items are ordered by rank.
# For example, we could ask people how many cigarettes they smoke per day, and the answers could be "none", "a few", "some", "a lot".
# These answers don't map exactly to numbers of cigarettes, but we know that "a few" is more than "none".
# This is an ordinal rating scale, and we can assign numbers to the answers, in order, to make them easier to work with.
# We could map 0 to "none", 1 to "a few", 2 to "some", and so on.

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]

# Assign the number that indicates its position on the scale to each survey response 
# ("none" is 0, and so on).

# Compute the average value of all the survey responses, and assign it to average_smoking.

# My Answer

sum_of_survey = 0
count = 0
for item in survey_responses:
    count = count + 1
    if item == "none":
        sum_of_survey = sum_of_survey + 0
    elif item == "a few":
        sum_of_survey = sum_of_survey + 1
    elif item == "some":
        sum_of_survey = sum_of_survey + 2
    elif item == "a lot":
        sum_of_survey = sum_of_survey + 3
    else:
        item = "missing scale"

print(sum_of_survey)
print(count)
average_smoking = sum_of_survey / count
print(average_smoking)

# Hint
# You'll want to make a new list that assigns 0 to any response in survey_responses that is "none", 
# 1 to any response that is "a few", and so on.
# Then, calculate the sum of that list, and divide by the length to get the average response.

# DataQuest Answer
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)

list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.


#### Categorical_scales ####

# We can also have categorical scales, that have category labels.
# One example is gender, which can be male or female.
# There isn't an ordering between male and female -- one is not greater than or less than the other, so it's not an ordinal scale.
# You'll encounter categories a lot, and usually you'll use them to split data into groups.


# Let's say that these lists are both columns in a matrix.  Index 0 in both is the first row, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]

# Compute the average savings for everyone who is "male". 
# Assign the result to male_savings.
# Compute the average savings for everyone who is "female". 
# Assign the result to female_savings.

# My Answer 1
sum_male_savings = 0
sum_female_savings = 0
count_male_savings = 0
count_female_savings = 0
for i, item in enumerate(gender):
    if item == "male":
        sum_male_savings = sum_male_savings + savings[i]
        count_male_savings = count_male_savings + 1
    else:
        sum_female_savings = sum_female_savings + savings[i]
        count_female_savings = count_female_savings + 1

male_savings = sum_male_savings / count_male_savings

female_savings = sum_female_savings / count_female_savings

# Hint
# You can use a list comprehension to filter out the values in savings where the corresponding gender is "male" or "female". 
# You can do this by looping over the range() from 0 to the length of gender.

# Answer
male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)

# deconsructed:

male_savings_list = []
female_savings_list = []

for i in range(0, len(gender)):
    if gender[i] == "male":
        male_savings_list.append(savings[i])

for i in range(0, len(gender)):
    if gender[i] == "female":
        female_savings_list.append(savings[i])

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)


#### Frequency_histograms ####

# Remember how statistics is all about counting? 
# There's a plot called a frequency histogram that helps us visualize counts of data a lot better.
# The idea is to count up how many times a value occurs in a list, and then graph the values on the x-axis, and the counts on the y-axis.
# This lets us better understand how values fall in datasets.

# Let's say that we watch cars drive by, and measure average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()
plt.clf()

# Let's say we measure student test scores, from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]

# Plot a histogram of student_scores.
plt.hist(student_scores)
plt.show()
plt.clf()


#### Histogram_bins ####

# You may have noticed in the last screen that all of the values were plotted.
# Histograms use something called bins to count up values.
# If the x-axis ranges from 0 to 10, and we have 10 bins, the first bin would be 0-1, the second would be 1-2, and so on.
# If we have 5 bins, the first would be 0-2, the second would be 2-4, and so on.
# Any values in the list that fall within the bin would increase the count of the bin by one.
# Bins allow us to better understand the shape and distribution of the data than graphing every count individually.
# In the last screen, the default number of bins for a matplotlib plot is 10, 
# and we had less values than that, so all the values were shown.
# We'll experiment a bit with different numbers of bins to get a better intuition of how they work.

average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()
plt.clf()

# As you can see, the values in the list are counted into the nearest bin.
# If we have less bins, each bin will have a higher count 
# (because it's showing all of the values that fall into it)
# With more bins, the counts are less, because each bin contains less values.
plt.hist(average_speed, bins=4)
plt.show()
plt.clf()

# Plot a histogram of average_speed with only 2 bins.
plt.hist(average_speed, bins=2)
plt.show()
plt.clf()


#### Skew ####

# Now that we know how to make histograms, notice how the plots have a "shape" to them?
# These shapes are important, and can show you distributional parameters of the data.
# The first parameter we'll look at is called skew.

# Some numpy arrays are already loaded in, and we'll make some plots with them.
# The arrays contain student test scores from an exam, on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there is a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot is negatively skewed.
plt.hist(test_scores_negative)
plt.show()
plt.clf()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This is positively skewed.
plt.hist(test_scores_positive)
plt.show()
plt.clf()

# This plot has no skew either way -- most of the values are in the center, 
# and there is no long slope either way.
# Is is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()
plt.clf()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew,
# and close to zero means no skew.
from scipy.stats import skew

# Assign the skew of test_scores_positive to positive_skew.
# Assign the skew of test_scores_negative to negative_skew.
# Assign the skew of test_scores_normal to no_skew.

positive_skew = skew(test_scores_positive)
print(positive_skew)    #0.585
negative_skew = skew(test_scores_negative)
print(negative_skew)    #-0.563
no_skew = skew(test_scores_normal)
print(no_skew)          #0.0124


#### Kurtosis ####

# Another parameter of a distribution is called kurtosis.
# Kurtosis measures whether the distribution is short and flat, or tall and skinny.
# "Shorter" distributions have a lower maximum frequency, but higher subsequent frequencies.

import matplotlib.pyplot as plt

# This plot is short, making it platykurtic
# See how the values are distributed pretty evenly, and there isn't a huge cluster in the middle?
# Students had a wide variation in their performance
plt.hist(test_scores_platy)
plt.show()
plt.clf()

# This plot is tall, and is leptokurtic
# Most students did very similarly to the others
plt.hist(test_scores_lepto)
plt.show()
plt.clf()

# This plot is in between, and is mesokurtic
plt.hist(test_scores_meso)
plt.show()
plt.clf()

# We can measure kurtosis with the kurtosis function
# Negative values indicate platykurtic distributions, 
# positive values indicate leptokurtic distributions, 
# and values close to 0 are mesokurtic
from scipy.stats import kurtosis

# Assign the kurtosis of test_scores_platy to kurt_platy.
# Assign the kurtosis of test_scores_lepto to kurt_lepto.
# Assign the kurtosis of test_scores_meso to kurt_meso.

kurt_platy = kurtosis(test_scores_platy)
print(kurt_platy)	# -0.9498
kurt_lepto = kurtosis(test_scores_lepto)
print(kurt_lepto)	# 0.00396
kurt_meso = kurtosis(test_scores_meso)
print(kurt_meso)	#-0.0561


##### Modality ####

# Modality is another parameter of distributions.
# Modality refers to the number of modes, or peaks, in a distribution.
# Real-world data often is unimodal (only has one mode)

import matplotlib.pyplot as plt

# This plot has one mode, making it unimodal
plt.hist(test_scores_uni)
plt.show()
plt.clf()

# This plot has two peaks, and is bimodal
# This could happen if one group of students learned the material, and one learned something else, for example.
plt.hist(test_scores_bi)
plt.show()
plt.clf()

# More than one peak means that the plot is multimodal
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to observe the plot.


# Plot test_scores_multi, which has four peaks.
plt.hist(test_scores_multi)
plt.show()
plt.clf()


#### Measures_of_central_tendancy ####

# Now that we know how to measure parameters of a distribution, let's look at central tendency measures.
# These measure how likely points in the data are to cluster around a central point.
# The first one we'll look at is the mean.
# We've taken the mean before, but we'll look more closely at what it is.
# The mean is just the sum of all the elements in an array divided by the number of elements.

import matplotlib.pyplot as plt
# We're going to put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure
plt.show()
plt.clf()

# When we plot test_scores_negative, a very negatively skewed distribution, 
# we see that the mean is pulled to the left by the small values there.
# The mean can be changed easily by very large or very small values.
# This can make it misleading with distributions that are very skewed, 
# when we expect the mean to be the center.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())
plt.show()
plt.clf()

# We can do the same with the positive side
# See how the very high values pull the mean to the right more than you would expect?
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()
plt.clf()


# Compute the mean of test_scores_normal, and assign to mean_normal.
# Compute the mean of test_scores_negative, and assign to mean_negative.
# Compute the mean of test_scores_positive, and assign to mean_positive.

mean_normal = test_scores_normal.mean()
print(mean_normal)		# 50.200
mean_negative = test_scores_negative.mean()
print(mean_negative)	# 82.809
mean_positive = test_scores_positive.mean()
print(mean_positive)	# 16.816


#### The_median ####

# Another measure of central tendency is the median.
# This is the midpoint of an array.
# You have to sort the array, and then take the value in the middle.
# If two values are in the middle (if there are an even number of items in the array), then you take the mean of the two middle values.
# The median is less sensitive to very large or very small values (outliers), and is a more realistic center of the distribution.

# Let's plot the mean and median side by side in a negatively skewed distribution.
# Sadly, numpy arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# See how the median is further to the right than the mean?
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()
plt.clf()

# Plot a histogram for test_scores_positive.
# Add in a blue line for the median.
# Add in a red line for the mean.

plt.hist(test_scores_positive)

plt.axvline(numpy.median(test_scores_positive), color = "b")
plt.axvline(test_scores_positive.mean(), color = "r")

plt.show()
plt.clf()


#### Titanic Data ####

# Now we know some basic statistics, we can apply them to a dataset
# The titanic data is passenger data,

#### Plotting_titanic_data ####

# Before we dive into cleaning up the data, let's take a look at why we need to deal with the missing values.

# The titanic data is loaded into the titanic_survival variable, which is a pandas dataframe
# See the values that show up as NaN in the age column?  Those were missing in the original dataset
# NaN stands for not a number
print(titanic_survival["age"])

# Now let's try plotting with the NaN values
import matplotlib.pyplot as plt
plt.hist(titanic_survival["age"])

# The above will fail with an error
# This is because we can't plot a value that doesn't exist (NaN)
# We need to deal with those values before we can proceed


#### Cleaning_missing_titanic_data ####

# Now that we know some statistics, let's practice on our Titanic data.
# Our data is a manifest of all the passengers on the Titanic, a ship that sunk in April 1912.
# It contains passenger names, ages, and other information (such as whether or not they survived).
# Unfortunately, not all data is available -- some passengers don't have an age or other information listed.
# Before we can analyze the data, we have to do something about the missing rows.
# The easiest way to deal with them is to just remove all rows with missing data.
# This isn't necessarily the best solution in all cases, but we'll learn about other ways to handle this later on.

# Luckily, pandas dataframes have a method that can drop rows that have missing data
# Let's look at how big the dataframe is first
print(titanic_survival.shape)

# There were 1310 passengers on the titanic, according to our data
# Now let's drop any row with missing data
# The dropna method on dataframes will do this for us
# Any row with any missing values will be removed
new_titanic_survival = titanic_survival.dropna()

# Hmm, it looks like we were too zealous with dropping rows with na values
# We now have no rows in our dataframe
# This is because some of the later columns, which aren't immediately relevant to our analysis, 
# have a lot of missing values
print(new_titanic_survival.shape)

# We can use the subset keyword argument to the dropna method to only drop rows 
# if there are na values in certain columns
# This will drop any row where the embarkation port (where people boarded the Titanic), 
# or cabin number is missing
new_titanic_survival = titanic_survival.dropna(subset=["embarked", "cabin"])

# This is much better -- we have removed only the rows that we need to remove.
print(new_titanic_survival.shape)

# Remove the NaN values in the "age" and "sex" columns.
# Assign the result to new_titanic_survival.

new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
print(new_titanic_survival.shape)


#### Plotting_age ####

# Now that we have cleaned up data, let's analyze it.

# The cleaned up data has been loaded into the titanic_survival variable
import matplotlib.pyplot as plt
import numpy

# Plot a histogram of the "age" column in titanic_survival.
# Add in a blue line for the median.
# Add in a red line for the mean.

plt.hist(titanic_survival["age"])
plt.axvline(numpy.median(titanic_survival["age"]),color = "b")
plt.axvline((titanic_survival["age"]).mean(),color = "r")

plt.show()
plt.clf()


#### Calculating_basic_stats_for_age ####

# The age distribution was very interesting, and showed that a lot of people in their 20s-40s were travelling without children.
# Now that we know what the distribution looks like, let's calculate the parameters and central tendency measures.

# The cleaned up data has been loaded into the titanic_survival variable

# Assign the mean of the "age" column of titanic_survival to mean_age.
# Assign the median of the "age" column of titanic_survival to median_age.
# Assign the skew of the "age" column of titanic_survival to skew_age.
# Assign the kurtosis of the "age" column of titanic_survival to kurtosis_age.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

mean_age = (titanic_survival["age"]).mean()
median_age = np.median(titanic_survival["age"])

skew_age = skew(titanic_survival["age"])
kurtosis_age = kurtosis(titanic_survival["age"])

# mean() is a method
# median, skew, kurtosis are functions

print(mean_age)       # 29.88
print(median_age)     # 28.0
print(skew_age)       # 0.407
print(kurtosis_age)   # 0.141




########################################################################################################################
########################################################################################################################
########################################################################################################################

#### NOTES ON PYTHON FUNCTIONS ####

#### Data_structures ####

# The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
# Add an item to the end of the list; equivalent to a[len(a):] = [x].

list.extend(L)
# Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x)
# Return the number of times x appears in the list.

list.sort(cmp=None, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
# Reverse the elements of the list, in place.



##### Methods_or_functions ####

# Python method, eg numpy's mean is calculated like
import numpy
mean_of_series = series.mean()

# Python function, eg numpy's median is calculated like

import numpy
mean_of_series = median(series)

