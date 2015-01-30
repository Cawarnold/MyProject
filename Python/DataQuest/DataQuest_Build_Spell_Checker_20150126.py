## DataQuest_Build_Spell_Checker_20150122

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Basics: Build a Spell Checker --- (Finding_spelling_mistakes)

#####################################

Overview of Useful code:

String split some text. (Tokenizing_the_file)
Replace punctuation _from strings. (Replace_punctuation)
Making _all the text lowercase. (Lowercasing_the_words)
Creating a Function. (Making_a_basic_function)
Types of errors. Syntax Error. (Types_of_errors_SyntaxError)
Types of errors. Index Error. (Types_of_errors_IndexError)
Function that removes the Punctuation _from strings _in a _list. (Remove_punctuation_from_list_of_strings)
Function that removes the Punctuation _and makes lowercase. (Making_a_function_to_lowercase_input)
Read dictionary, normalise strings. (Reading_in_and_normalizing_the_dictionary)
Scrpit of how to find spelling mistakes. (Finding_spelling_mistakes)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### Tokenizing_the_file ####

# We can split strings into lists with the .split() method.
f = open("story.txt","r")
story = f.read()
tokenized_story = story.split(" ")


#### Replace_punctuation ####

# We can use the .replace function to replace punctuation in a string.

no_punctuation_tokens = []

for tokens in tokenized_story:
    tokens = tokens.replace(".", "")
    no_punctuation_tokens.append(tokens)
# Do not need to loop through each character in each token (item) in list.
print(no_punctuation_tokens)


#### Lowercasing_the_words ####

# We can use the .lower function to make all characters lower case
lowercase_tokens = []

for token in no_punctuation_tokens:
    token = token.lower()
    lowercase_tokens.append(token)
print(lowercase_tokens)


#### Making_a_basic_function ####

# "def" means define a new function.
# def function_name(arguements)
# return means the function will output this. (return always goes inside a function)

# Define a function that takes degrees in fahrenheit as an input, and return degrees celsius

def convert(degrees_f):
    return (degrees_f - 32)/1.8
 
celsius_100 = convert(100)
celsius_150 = convert(150)
print(celsius_100)

#### Types_of_errors_SyntaxError ####

# Syntax errors occur when something is typed incorrectly (statements misspelled, quotes missing, and so on)

#### Types_of_errors_IndexError ####

# Index errors occur when a list index that doesn't exist is referenced.


#### Remove_punctuation_from_list_of_strings ####

# no_punctuation_tokens = []

# All the tokens from Julius's story are in the tokenized_story variable.
# Write a function that removes all punctuation from an input string.
# Then loop over tokenized_story and call the function to remove the punctuation from each token.
# Append the tokens to no_punctuation_tokens.

def remove_punctuation_from_list_of_strings(list_of_words):
    for token in list_of_words:
        token = token.replace(".","")
        token = token.replace(",","")
        token = token.replace("'","")
        token = token.replace(";","")
        token = token.replace(":","")
        token = token.replace("/n","")
        token = token.replace("\n","")
        no_punctuation_tokens.append(token)
    return no_punctuation_tokens

no_punctuation_tokens = []
print(remove_punctuation_from_list_of_strings(tokenized_story))


#### Making_a_function_to_lowercase_input ####

def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_tokens = []
for item in tokenized_story:
    item = remove_punctuation(item)
    normalized_tokens.append(item)
print(normalized_tokens)

#### Reading_in_and_normalizing_the_dictionary ####

def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_dictionary_tokens = []

file_dict = open("dictionary.txt","r")
dictionary = file_dict.read()
token_dict = dictionary.split(" ")

for token in token_dict:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)

print(normalized_dictionary_tokens)


#### Finding_words_that_arent_spelled_correctly ####

potential_misspellings = []
correctly_spelled = []

for item in normalized_story_tokens:
    if item in normalized_dictionary_tokens:
        correctly_spelled.append(item)
    else:
        potential_misspellings.append(item)

print(potential_misspellings)

print("CORRECTLY SPELLED:", correctly_spelled)

#### Finding_spelling_mistakes ####

def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

f = open("story.txt","r")
story = f.read()
tokenized_story = story.split(" ")
normalized_story_tokens = []
for token in tokenized_story:
    token = normalize(token)
    normalized_story_tokens.append(token)

file_dict = open("dictionary.txt","r")
dictionary = file_dict.read()
token_dict = dictionary.split(" ")
normalized_dictionary_tokens = []
for token in token_dict:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)

potential_misspellings = []
correctly_spelled = []

for item in normalized_story_tokens:
    if item in normalized_dictionary_tokens:
        correctly_spelled.append(item)
    else:
        potential_misspellings.append(item)

print(potential_misspellings)

print("CORRECTLY SPELLED:", correctly_spelled)


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# The stroy is in a text file. 
# So we will be reading in the file and parsing out the file.

#### Reading_the_file_in ####

# The story is stored in the file "story.txt".

# The story is stored in the "story.txt" file.
# Open the file and read the contents into the story variable.

f = open("story.txt","r")
story = f.read()

f.close


#### Tokenizing_the_file ####

# We can split strings into lists with the .split() method.
# If we use a space as the input to .split(), it will split based on the space.
text = "Bears are probably better than sharks, but I can't get close enough to one to be sure."
tokenized_text = text.split(" ")

# The story is loaded into the story variable.
# Tokenize the story, and store the tokens into the tokenized_story variable.

print(story)
tokenized_story = story.split(" ")
print(tokenized_story)


#### Replace_punctuation ####

# We can use the .replace function to replace punctuation in a string.
text = "Who really shot John F. Kennedy?"
text = text.replace("?", "?!")

# The question mark has been replaced with ?!.
print(text)

# We can replace strings with blank spaces, meaning that they are just removed.
text = text.replace("?", "")

# The question mark is gone now.
print(text)

no_punctuation_tokens = []

# Replace all of the punctuation in each of the tokens.
# You'll need to loop through tokenized_story to do so.
# You'll need to use multiple replace statements, one for each punctuation character to replace.
# Append the token to no_punctuation_tokens once you are done replacing characters.

for tokens in tokenized_story:
    tokens = tokens.replace(".", "")
    tokens = tokens.replace(",", "")
    tokens = tokens.replace("'", "")
    tokens = tokens.replace(";", "")
    tokens = tokens.replace(":", "")
    tokens = tokens.replace("\n\n", "")
    no_punctuation_tokens.append(tokens)

# Do not need to loop through each character in each token (item) in list.

print(no_punctuation_tokens)

#### Lowercasing_the_words ####

# We can make strings all lowercase using the .lower() method.
text = "MY CAPS LOCK IS STUCK"
text = text.lower()

# The text is much nicer to read now.
print(text)

lowercase_tokens = []

# Loop through the tokens and lowercase each one.
# Append each token to lowercase_tokens when you're done lowercasing.

for token in no_punctuation_tokens:
    token = token.lower()
    lowercase_tokens.append(token)
print(lowercase_tokens)

#### Functions ####

a = 50
b = 10
c = 80

# All in faenheight, now we want to convert to celcius.

list_celcius = [a,b,c]

for items in list_celcus:
	# do maths.

# "def" means define a new function.
# def function_name(arguements)
# return means the function will output this. (return always goes inside a function)

def convert_f_to_c(degrees):
	return (degrees - 32)/1.8

a = 50
a = convert_f_to_c(a)

# convert_f_to_c(a) calls the function and applies it the the valiable a.

# def convert(arg0,arg1,arg2)

# a = convert(arg0,arg1,arg2)

# these args correspond by index, ie by position. "Positional Argument"

#### Making_a_basic_function ####

# A simple function that takes in a number of miles, and turns it into kilometers
# The input at position 0 will be put into the miles variable.
def miles_to_km(miles):
    # return is a special keyword that indicates that the function will output whatever comes after it.
    return miles/0.62137

# Returns the number of kilometers equivalent to one mile
print(miles_to_km(1))

# Convert a from 10 miles to kilometers
a = 10
a = miles_to_km(a)

# We can convert and assign to a different variable
b = 50
c = miles_to_km(b)

fahrenheit = 80
celsius = (fahrenheit - 32)/1.8

# Define a function that takes degrees in fahrenheit as an input, and return degrees celsius

def convert(degrees_f):
    return (degrees_f - 32)/1.8
    
celsius_100 = convert(100)
celsius_150 = convert(150)

print(celsius_100)

#### Function Introduction ####

def split_string(text):
    return text.split(" ")

sally = "Sally sells seashells by the seashore."
# This splits the string into a list.
print(split_string(sally))

# We can assign the output of a function to a variable.
sally_tokens = split_string(sally)

lowercase_me = "I wish I was in ALL lowercase"

# Make a function that takes a string as input and outputs a lowercase version.
# Then use it to turn the string lowercase_me to lowercase.
# Assign the result to lowercased_string.

def lowc(any_string):
    return any_string.lower()

lowercased_string = lowc(lowercase_me)
print(lowercased_string)


#### Types_of_errors_SyntaxError ####

# Sometimes, you will have problems with your code that cause python to throw an exception.
# Don't worry, it happens to all of us many times a day.
# An exception means that the program can't run, so you'll get an error in the results view instead of the normal output.
# There are a few different types of exceptions.
# The first we'll look at is a SyntaxError.
# This means that something is typed incorrectly (statements misspelled, quotes missing, and so on)

a = ["Errors are no fun!", "But they can be fixed", "Just fix the syntax and everything will be fine"]
b = 5

for item in a:
    if b == 5:
        print(item)

# Syntax errors occur when something is typed incorrectly (statements misspelled, quotes missing, and so on)

#Ran Debug mode to see what line the errors were occuring

## Original Code >> 

5 = a

if a == 6 
    print("6 is obviously the best number")
print("What's going on, guys?")
else:
    print("I never liked that 6")

## Fixed Code >>

a = 5

if a == 6:
    print("6 is obviously the best number")
    print("What's going on, guys?")
else:
    print("I never liked that 6")

#### Types_of_errors_IndexError ####

# Index errors occur when a list index that doesn't exist is referenced.

# An index error is when a nonexistent index in a list is accessed.

## Original Code >> 

the_list = ["Harrison Ford", "Mark Hammil"]
print(the_list[3])
another_list = ["Jabba"]
print(another_list[1])

## Fixed Code >>

the_list = ["Harrison Ford", "Mark Hammil"]
print(the_list[1])
another_list = ["Jabba"]
print(another_list[0])


#### Multi_line_functions ####

# Make a function that counts up all the values in a list
# If you define "tally = 0" outside the function, you wouldn't be able to access it inside the function.
# Any variable that you want to use in the function, assume single use.

def total(values):
    tally = 0
    for v in values:
        tally = tally + v
    return tally

# Any time we call the total function we get the tally (sum) of the values.

print("tally = ",total([2,5,8]))
>> tally = 15

####

# Functions can have multiple lines in the function body.
def do_math(number):
    # Multiply the number by 10
    number = number * 10
    # Add 20 to the number
    number = number + 20
    return number

print(do_math(20))
a = do_math(10)

#### Remove_punctuation_function ####

# no_punctuation_tokens = []

# All the tokens from Julius's story are in the tokenized_story variable.
# Write a function that removes all punctuation from an input string.
# Then loop over tokenized_story and call the function to remove the punctuation from each token.
# Append the tokens to no_punctuation_tokens.

def remove_punctuation_from_list_of_strings(list_of_words):
    for token in list_of_words:
        token = token.replace(".","")
        token = token.replace(",","")
        token = token.replace("'","")
        token = token.replace(";","")
        token = token.replace(":","")
        token = token.replace("/n","")
        token = token.replace("\n","")
        no_punctuation_tokens.append(token)
    return no_punctuation_tokens

no_punctuation_tokens = []
print(remove_punctuation_from_list_of_strings(tokenized_story))

#### Making_a_function_to_lowercase_input ####

# This is our function to remove punctuation.
def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

# We've read the tokens from Julius's story into the tokenized_story variable.
# Can you add to the remove_punctuation function so it also lowercases the tokens?
# Then loop over the tokens in tokenized_story, normalize them with the function, and append them to normalized_tokens.
normalized_tokens = []

# The remove_punctuation function is to the right.
# Can you add to it so that it also makes the output lowercase?
# Then loop over the tokens in tokenized_story and normalize them with the function.
# Append the tokens to normalized_tokens when you're done.

for item in tokenized_story:
    item = remove_punctuation(item)
    normalized_tokens.append(item)

print(normalized_tokens)

#### Multiple Arguments ####

def search(item1,item2,values):
    found = False
    if item1 in values:
        found = True
    return found

# how does python know which argument to assign to which variable.

search(1,2,[3,4,5])
> True

# item1 will be assign 1 because they are both at position 0, item2 will be assigned item2 (position/index=1)
# values will be assign this list, because they are in index = 2.

# when we call this search function we will get True, because 1 is in the values list.

#### Practice_multiple_argument_functions ####

# This function takes two arguments, at positions 0 and 1
def divide(x,y):
    return x/y

# 5 is assigned to x, and 1 is assigned to y based on positions
print(divide(5,1))

# 1 is assigned to x, and 5 is assigned to y based on positions.
print(divide(1,5))

# Create a multiply function that takes in x, y, and z argument.
# The function should return x * y * z
# Assign the values of multiply(10,3,5) to a
# Assign the values of multiply(20,-1,3) to b

def multiply(x,y,z):
    return (x*y*z)

a = multiply(10,3,5)
b = multiply(20,-1,3)
print(a)
print(b)

#### Reading_in_and_normalizing_the_dictionary ####

def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_dictionary_tokens = []

# Read in the dictionary from the "dictionary.txt" file.
# Split it into tokens based on the space character.
# Normalize each token using the normalize function.
# Append the normalized tokens to normalized_dictionary_tokens

file_dict = open("dictionary.txt","r")
dictionary = file_dict.read()
token_dict = dictionary.split(" ")

for token in token_dict:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)

print(normalized_dictionary_tokens)


#### Finding_words_that_arent_spelled_correctly ####

potential_misspellings = []
correctly_spelled = []

normalized_story_tokens
normalized_dictionary_tokens

# The normalized story tokens are in normalized_story_tokens, 
# and the normalized dictionary tokens are in normalized_dictionary_tokens.
# Loop through the story tokens, and check if each token is in the dictionary.
# If the token is in normalized_dictionary_tokens, append it to correctly_spelled
# If it isn't, append it to potential_misspellings.

for item in normalized_story_tokens:
    if item in normalized_dictionary_tokens:
        correctly_spelled.append(item)
    else:
        potential_misspellings.append(item)

print(potential_misspellings)

print("CORRECTLY SPELLED:", correctly_spelled)



























