## DataQuest_Airline_Delays_20150206

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 7

# Basics: Which airline is delayed the most?

# Learn more about indexing, keyword arguments, and the break keyword while finding out which airlines have the most delays.

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####




########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# Airline flight delays
# FAA, US flights

# sample row:
# Carrier      Name                 arr_del15          airport      arrival_delay        arrivals      other columns
#   AA        American Airlines      2,000               JFK          100,000              10,000         ...

# arr_del15 = total number of flights that are arriving to a certain airport that are delayed for more than 15 mins
# arrival_delay = total number of minutes that planes were delayed. Only planes delayed for more that 15 minutes.

# about 1000 rows

# We're going to calculate stuff like:
# how much planes are delayed on average.
# the worst carrier to fly on


#### Writing_a_while_loop ####

# Before we dive into analyzing the data, we need to learn a few more things about loops.
# A for loop isn't the only kind of loop.
# One other type of loop is called a while loop.
# It will keep running the loop as long as the condition specified is True.

x = 2
while x == 2:
    print x

# The code above will run forever, because the loop will keep testing to see if x equals 2, and it will always return True.

# You have to be careful not to get into an infinite loop, or a loop that runs forever, when you use a while loop

x = 2
while x == 3:
    print x

#The code above won't run at all, because x will never equal three

x = 3
# The loop body will execute three times.  Once when x == 3, once when x == 4, and once when x == 5.
# Then x < 6 will evaluate to False, and it will stop.
# 3, 4, and 5 will be printed out.  Try it out in debug mode if you want a closer look.
while x < 6:
    print(x)
    # Using += is a shorter way of saying x = x + 1.  It will add one to x.
    x += 1

b = 10

# Create a while loop that tests if b is greater than 5. 
# If it is, the loop body should print b out, then subtract one from it.

while b > 5:
    print(b)
    b = b - 1 


#### Using_the_break_keyword ####

# The break keyword can be used to stop a loop early.
# This can be useful in for loops when something happens inside the loop that makes us need to end it early.

dog_available = False
desired_dog = "Great Dane"
available_dogs = ["Labrador", "Poodle", "Sheepdog", "Great Dane", "Pomeranian"]
for dog in available_dogs:
    if dog == desired_dog:
        dog_available = True
        break

# The code above will check to see if the desired_dog is available, and stop looping if it is found.

available_count = 0
desired_dog = "Great Dane"
available_dogs = ["Labrador", "Poodle", "Sheepdog", "Great Dane", "Pomeranian", "Great Dane", "Collie"]

# Let's say we are searching for two dogs of the same breed to adopt.
# We'll loop through the dogs.
for dog in available_dogs:
    # If our desired dog is found.
    if dog == desired_dog:
        # Increment the counter.
        available_count += 1
        # We only want two dogs, so we can stop searching after we find them.
        if available_count == 2:
            break

tiger_count = 0
desired_tiger = "Bengal"
available_tigers = ["Bengal", "Dressed up poodle", "Siberian", "Sumatran", "Bengal", "Housecat", "Hobbes"]

# Let's say we want two "Bengal" tigers from available_tigers for our nature reserve.
# Write a for loop that breaks after finding two, and increments tiger_count when it finds one

for tiger in available_tigers:
    while tiger_count < 2:
        if tiger == desired_tiger:
            tiger_count = tiger_count + 1

#### Finding_a_column_number_from_a_name ####

# We'll skip the process of reading the file in.
# The data is in the flight_delays variable, and the column names are in the column_names variable.
# So far, we've been numbering columns and selecting them using numbers, 
# but it can get pretty painful to do this when there are more than 10 columns.
# One fix for this is to refer to the columns by name, and write a function that returns a column number for a given column name.

# It's pretty easy to get a column name from a column number.
# The third column contains the carrier (same as the airline).
print(column_names[2])

# Write a function that will get the column number from the column name.
# Use it to get the column number for the "arr_delay" column and assign it to the arr_delay variable.
# Use it to get the column number for the "weather_delay" column and assign it to the weather_delay variable.


def col_number(col_name):
    for i, column in enumerate(column_names):
        if column == col_name:
            return i

arr_delay = col_number("arr_delay")
print(arr_delay)
weather_delay = col_number("weather_delay")
print(weather_delay)

## Official answer
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

#### Using_negative_indexing ####

# We can index lists with negative values.
# Positive indexes start getting values from the beginning of a list, but negative indexes get values from the end of a list.

# Prints the last row in flight_delays
print(flight_delays[-1])

# Prints the second to last row in flight_delays
print(flight_delays[-2])

# Prints the third to last and second to last rows in flight_delays (remember that slicing only goes up to but not including the second number)
# This will get the rows at index -3 and -2
print(flight_delays[-3:-1])

# Use negative indexing to assign the third to last row in flight_delays to third_to_last.
# Use negative slicing to assign the fourth, third, and second to last rows in flight_delays to end_slice

third_to_last = flight_delays[-3]
end_slice = flight_delays[-4:-1]


#### Indexing_up_to_the_end_or_from_the_beginning ####

# When we take a slice, we can leave one of the numbers blank.

# Leaving the first number in the slice blank means "start from the beginning of the list, inclusive"
# This code will get the rows at index 0, 1, 2, 3, and 4.
first_five_rows = flight_delays[:5]

# We can also leave the last number blank to get all rows up to and including the last one.
# This will get the rows at index -5, -4, -3, -2, and -1
last_five_rows = flight_delays[-5:]

# Assign the first 10 rows of flight_delays to first_ten_rows.
# Assign the last 10 rows of flight_delays to last_ten_rows.

first_ten_rows = flight_delays[:10]
print(first_ten_rows)
last_ten_rows = flight_delays[-10:]
print(last_ten_rows)


#### Finding_the_percentage_of_delayed_flights ####

# We can now find the percentage of flights that are delayed.

def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

# Get the column number of the arr_flight column
# This column counts the total number of arriving flights for a carrier in a given airport
arr_flights_column = column_number_from_name("arr_flights")

# Extract all of the values in the column using a list comprehension
# We need to convert the values to float because they are strings initially
arr_flights = [float(row[arr_flights_column]) for row in flight_delays]

# Now we can use the sum() function to add together all of the values.
total_arriving_flights = sum(arr_flights)

# Sum together the values in the "arr_del15" column. 
# This is the total number of arriving flights in each airport that were delayed more than 15 minutes.
arr_del15_column = column_number_from_name("arr_del15")
arr_del15 = [float(row[arr_del15_column]) for row in flight_delays]
total_arr_del15 = sum(arr_del15)
# Then, divide the number of delayed flights by total_arriving_flights. 
# Assign the result to delayed_percentage.

delayed_percentage = (total_arr_del15/total_arriving_flights)
print(delayed_percentage)

#### Finding_the_average_delay_time ####

# The total amount of time (in minutes) that planes for a given carrier were delayed at a given airport is in "arr_delay" column.






















