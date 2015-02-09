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

def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

# Find the sum of the "arr_delay" column.
# Then, divide it by the sum of the "arr_del15" column to get 
# the average number of minutes a plane was delayed.
# Assign the result to average_delay_time

average_delay_time = None
arr_delays = []
arr_del15 = []
for i,row in enumerate(flight_delays):
    arr_delays.append(int(row[column_number_from_name("arr_delay")]))
    arr_del15.append(int(row[column_number_from_name("arr_del15")]))
total_arr_delays = sum(arr_delays)
total_arr_del15 = sum(arr_del15)
print(total_arr_delays)
print(total_arr_del15)

average_delay_time = total_arr_delays / total_arr_del15
print(average_delay_time)

#### Making_a_function_to_calculate_the_delay ####

# There are a few more columns that we'll need to calculate the sum of, 
# and its getting a bit tedious to keep typing the same few commands.
# Let's make a function to save ourselves time.


def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

# Make a function that takes a column name as input, and returns the column sum.
# Then use the function to take the sum of the "weather_delay" column, 
# and divide it by the sum of the "arr_del15" column.
# Assign the result to average_weather_delay_time.

def calc_sum_of(column_name):
    list_of_values = []
    for i,row in enumerate(flight_delays):
        list_of_values.append(int(row[column_number_from_name(column_name)]))
    total = sum(list_of_values)
    return total
print(calc_sum_of("arr_del15"))
print(calc_sum_of("weather_delay"))

average_weather_delay_time = calc_sum_of("weather_delay") / calc_sum_of("arr_del15")
print(average_weather_delay_time)


#### Named and optional arguements to functions ####

#so far we've done

def add(x,y):
    return x+y
add(10,5)
#since 10 is assigned first it goes to the x
#since 5 is assigned second it goes to the y
> 15

# we can refer to these arguments by name, not just by position
add(y = 10, x = 5)
# the benefits: gies you extra flexibility. and let you make arguments optional.
# when you start naming arguments youmust name all arguments for python to read it.

# Optional Args: division funtion
def div(x,y=1):
    return x/y

div(1)
> 1/1 = 1

div(0.5,0.5)
> 1   # as 0.5 overrides the y = 1.

#### Named_arguments_to_functions ####

# We can use named keyword arguments to pass input to a function.

def divide(x, y):
    return x/y

# Use positional arguments, which will implicitly pass 10 to x and 5 to y.
print(divide(10,5))

# Use named arguments, which will pass the values to the named variable.
print(divide(y=10, x=5))

# If we use named arguments, the order doesn't matter
print(divide(x=5, y=10))

# But we can't have any positional arguments after we use a named argument
print(divide(y=20, x=5))
print(divide(x=100, y=30))

# Fix the statements above so the code runs properly.
# The first statement should divide 5 by 20, and the second should divide 100 by 30.

#### Optional_arguments_to_a_function ####

# We can also specify default values in a function definition that make the arguments optional.
# You can't have an optional argument before a non-optional argument, just like named keywords.

def multiply(a, b=2, c=1):
    return a * b * c

# This will multiply 5 * 2 * 1
print(multiply(5))

# This will multiply 6 * 4 * 1
print(multiply(5, 4))

# This will multiply 5 * 2 * 1
print(multiply(a=5))

# This will multiply 6 * 2 * 4
print(multiply(a=6, c=4))

# Invalid, because we didn't fill the a variable, which doesn't have a default.
print(multiply(a=4,b=3))

# Invalid, because we didn't fill the a variable.
print(multiply(a=3,c=3))

# Fix the last two statements so that they work properly.
# The first statement should multiply 4 * 3 * 1
# The second statement should multiply 3 * 2 * 3

#### Finding_delay_by_carrier ####

# Now that we know about optional and keyword arguments, 
# let's make a function that can find the average delay for a given airport.

# Fill in the rest of the find_average_delay function.
# You can calculate average delay time by dividing the "arr_delay" column by the "arr_del15" column.
# The "carrier" column can be used to subset by carrier.
# Then use the function to assign the average delay time to average_delay_time.
# Use the function again to assign the average delay time on carrier
# AA" to american_airlines_average_delay_time


def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

print(column_names)
print(flight_delays[1])

def calc_sum_of(column_name):
    list_of_values = []
    for i,row in enumerate(flight_delays):
        list_of_values.append(int(row[column_number_from_name(column_name)]))
    total = sum(list_of_values)
    return total

print(calc_sum_of("arr_delay")/calc_sum_of("arr_del15"))

def find_average_delay(carrier_name=None):
    if carrier_name is None:
        arr_delay = calc_sum_of("arr_delay") 
        arr_del15 = calc_sum_of("arr_del15")
        average_delay_time = arr_delay / arr_del15
    else:
        arr_delay_list = []
        arr_del15_list = []
        for i, row in enumerate(flight_delays):
            if row[column_number_from_name("carrier")] == carrier_name:
                arr_delay_list.append(int(row[column_number_from_name("arr_delay")]))
                arr_del15_list.append(int(row[column_number_from_name("arr_del15")]))
                arr_delay = sum(arr_delay_list)
                arr_del15 = sum(arr_del15_list)
                #arr_delay = calc_sum_of("arr_delay")   #for some reason this doesn't work?
                #arr_del15 = calc_sum_of("arr_del15")   #same
                average_delay_time = arr_delay / arr_del15
    return average_delay_time
    # Remove the pass keyword and fill in the rest of this function.
    # If no carrier is provided, it should find the average delay for all carriers.
    # Otherwise, it should find the average delay for that carrier.
    # pass

average_delay_time = (find_average_delay())
print(average_delay_time)
american_airlines_average_delay_time = (find_average_delay(carrier_name = "AA"))
print(american_airlines_average_delay_time)


## Answer

def find_average_delay(carrier_name=None):
    total_delayed_flights = 0
    total_delay_time = 0
    delay_time_column = column_number_from_name("arr_delay")
    delay_number_column = column_number_from_name("arr_del15")
    carrier_column = column_number_from_name("carrier")
    for row in flight_delays:
        if carrier_name is None or row[carrier_column] == carrier_name:
            total_delayed_flights += float(row[delay_number_column])
            total_delay_time += float(row[delay_time_column])
    return total_delay_time / total_delayed_flights

average_delay_time = find_average_delay()
american_airlines_average_delay_time = find_average_delay("AA")


#### Finding_average_delay_for_each_carrier ####

# Now that we have a function to find the delay for a given carrier, we can find the delays for each carrier.

def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

def find_average_delay(carrier_name=None):
    total_delayed_flights = 0
    total_delay_time = 0
    delay_time_column = column_number_from_name("arr_delay")
    delay_number_column = column_number_from_name("arr_del15")
    carrier_column = column_number_from_name("carrier")
    for row in flight_delays:
        if carrier_name is None or row[carrier_column] == carrier_name:
            total_delayed_flights += float(row[delay_number_column])
            total_delay_time += float(row[delay_time_column])
    return total_delay_time / total_delayed_flights

# Create a list of the unique carrier names.
# Then call the find_average_delay function for each carrier.
# Set the carriers as keys in the delays_by_carrier dictionary, 
# with the values being the average delay times.

carrier_names_list = []
unique_carrier_names = set()
unique_carrier_names_list = []
for row in flight_delays:
    carrier_names_list.append(row[column_number_from_name("carrier")])
unique_carrier_names = set(carrier_names_list)
unique_carrier_names_list = list(unique_carrier_names)
print(unique_carrier_names_list)

delays_by_carrier = {}
for item in unique_carrier_names_list:
    delays_by_carrier[item] = find_average_delay(item)

print(delays_by_carrier)

