## DataQuest_ComputerScience_CIAdocuments_Unicode_20150218

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 12

# Basics: Analyze CIA documents

# Learn more about how computers store variables and unicode while analyzing excerpts from CIA reports.	

# decoding and encoding our bytes.

#####################################

Overview of Useful code:


#####################################

#### SUMMARY OF USEFUL CODE ####



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

# dataset from the CIA.
# details about torture and other illegal activity.
# all in rows and the sentences are listed.

# analyse these sentences and figure out which words occur the most frequently.
# and then track them over time.

# before we can do that we need to look at how computers store strings.
# and how those values are passed back and forth from the hard drive.

## A string is something like this
"string"

## hard drive. lets assume its a rectangle

#### Intro_to_binary ####

# Computers can't directly store values like strings or integers.
# Instead, they store information in binary -- the only valid numbers in binary are a 0 or a 1.
# This lets data be stored on devices like hard drives -- we just learned how hard drives store data.
# We normally count in base 10.
# It's called base 10 because there are 10 possible digits -- 0 through 9.
# Binary is base two, because there are only two possible digits - 0 and 1.
# Let's explore how binary numbers work.

# Let's say a is a binary number.  In python, we have to store binary numbers as strings
# Trying to say b = 10 directly will assume base 10, so strings are needed
b = "10"

# We can convert b to a binary number from a string using the int function -- the optional second argument base is set to 2 (binary is base two)
print(int(b, 2))

# Convert the binary number "100" to a base 2 integer. Assign the result to base_10_100.
base_10_100 = int("100",2)
print(type(base_10_100))


#### Binary_addition ####

# Just like with base 10 numbers, we can add binary numbers together.


# a is in base 10 -- because we have 10 possible digits, the highest value we can represent with one digit is 9
a = 9

# When we want to represent a value one higher, we need to add another digit
a += 1
# a now has two digits -- we incremented the invisible leading digit, which was 0 and is now 1, and set the last digit back to zero.
print(a)

# When we add 1 to 19, we increment the leading 1 by 1, and then set the last digit to 0, giving us 20.
a = 19
a += 1

# When we add 1 to 99, we increment the last digit by 1, and add 1 to the first digit, but the first digit is now greater than 9, so we have to increment the invisible leading digit.
a = 99
a += 1

# Binary addition works the exact same way, except the highest value any single digit can represent is 1.
b = "1"

# We'll add binary values using a binary_add function that was made just for this exercise
# It's not extremely important to know how it works right this second
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

c = binary_add(b, "1")

# We now see that c equals "10", which is exactly what happens in base 10 when we reach the highest possible digit.
print(c)

# c now equals "11"
c = binary_add(c, "1")
print(c)

# c now equals "100"
c = binary_add(c, "1")
print(c)

# Add "10" (base 2) to c.

c =  binary_add(c, "10")
print(c)


#### Converting_binary_values ####

# We saw how we could convert between bases with the int() function.
# Let's see what values in binary equal what values in base 10.

def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Start both at 0
a = 0
b = "0"

# Loop 10 times
for i in range(0, 10):
    # Add 1 to each
    a += 1
    b = binary_add(b, "1")

    # Check if they are equal
    print(int(b, 2) == a)

# The cool thing here is that a and b are always equal if you add the same amount to both
# This is because base 2 and base 10 are just ways to write numbers
# Counting 100 apples in base 2 or base 10 will always give you an equivalent result, you just have to convert between them
# We can represent any number in binary, we just need more digits than we would in base 10

# Convert "1001" to base 10. Assign the result to base_10_1001.

base_10_1001 = int("1001",2)
print(base_10_1001)
>9

## means I have a number "1001" in base 2, convert it to base 10.

base_10_1001 = int("11111111",2)
print(base_10_1001)
>255

#### Characters_to_binary ####

# Just like how integers are stored as binary, so are strings.
# Strings are split into single characters, then converted into integers, which are then converted to binary and stored.
# We'll look at simple characters first -- the so called ascii characters.
# These contain all the upper and lowercase english letters, all the digits, and a lot of punctuation symbols.

# The byte (/ˈbaɪt/) is a unit of digital information in computing and telecommunications that most commonly consists of eight bits.

# We can use the ord() function to get the integer associated with an ascii character.
ord('a')
print(ord('a'))
# Then we use the bin() function to convert to binary
# The bin function adds "0b" to the start of strings to indicate that they contain binary values
bin(ord('a'))
print(bin(ord('a')))
# ÿ is the "last" ascii character -- it has the highest integer value of any ascii character
# This is because 255 is the highest value that can be represented with 8 binary digits
ord('ÿ')
print(ord('ÿ'))
print('ÿ')
# As you can see, we get 8 1's, which shows that this is the highest possible 8 digit value
bin(ord('ÿ'))
print(bin(ord('ÿ')))

# Why is this?  It's because a single binary digit is called a bit, and computers store values in sequences of bytes, which are 8 bits together.
# You might be more familiar with kilobytes or megabytes -- a kilobyte is 1000 bytes, and a megabyte is 1000 kilobytes.
# There are 256 different ascii symbols, because the largest amount of storage any single ascii character can take up is one byte.

# Convert "w" to binary. Assign the result to binary_w.
# Convert "}" to binary. Assign the result to binary_bracket.
binary_w = bin(ord("w"))
print(binary_w)
binary_bracket = bin(ord("}"))
print(binary_bracket)


#### Intro_to_unicode ####

# You might be wondering right now what happened to all of the other characters and alphabets in the world.
# Because it only supports 255 characters, ascii can't deal with them, so a new standard was needed, called unicode.
# Unicode assigns code points to characters. In python, these code points look like this: "\u3232".
# We can use an encoding to turn these code points into binary integers.
# The most common encoding for unicode is utf-8. It tells a computer which code points are associated with which integers.
# utf-8 can encode values that are longer that one byte, enabling it to store all unicode characters.
# utf-8 encodes characters using a variable length of bytes, which means that it also supports regular ascii characters (which are one byte each).

# We can initialize unicode code points (the value for this code point is \u27F6, but you see it as a character because it is being automatically converted)
code_point = "⟶"

# This particular code point maps to a right arrow character
print(code_point)

# We can get the base 10 integer value of the code point with the ord function
print(ord(code_point))

# As you can see, this takes up a lot more than 1 byte
print(bin(ord(code_point)))

# Find the binary representation of "\u1019". Assign it to binary_1019.

code_point = "\u1019"
print(code_point)
# Get base 10 integer value of the code point with the ord function
print(ord(code_point))
# Get base 2 integer value of code point with bin and ord functions
print(bin(ord(code_point)))

binary_1019 = bin(ord(code_point))


#### Strings_with_unicode ####

# ascii is a subset of unicode. Unicode implements all of the ascii characters, as well as the additional characters that code points allow.
# This lets us create unicode strings, that have ascii and unicode characters together.
# By default in python 3, all strings are unicode, and encoded with utf-8, so we can directly use unicode code points or characters

s1 = "café"
# The \u prefix means "the next 4 digits are a unicode code point"
# It doesn't change the value at all (the last character in the string below is \u00e9)
s2 = "café"

# These strings are the same, because code points are equal to their corresponding unicode character.
# \u00e9 and é are equivalent.
print(s1 == s2)

# Make a string with mixed unicode and ascii, and assign it to s3

unicode_code_point = "\u00e9"
ascii_chars = "hello"

s3 = "caf\u00e9"
# incorrect answer

s3 = "hello မ"


#### The_bytes_type ####

# In python, there's a datatype called "bytes".
# It's like a string, except it contains encoded bytes values.
# When we create an object with a bytes type from a string, we specify an encoding (usually utf-8).
# We can then use the .encode() method to encode the string into bytes.

# We can make a string with some unicode values
superman = "Clark Kent␦"
print(superman)

# This tells python to encode the string superman into unicode using the utf-8 encoding
# We end up with a sequence of bytes instead of a string
superman_bytes = "Clark Kent␦".encode("utf-8")
print(superman_bytes)

batman = "Bruce Wayne␦"

# Encode batman with the utf-8 encoding, and assign to batman_bytes.

batman_bytes = batman.encode("utf-8")
print(batman_bytes) # b'Bruce Wayne\xe2\x90\xa6'
print(type(batman_bytes))  # class 'bytes'


#### Hexadecimal intro ####

# In the lat screen when we converted the code string instead of getting binary bytes that we were expecting we got things like:
# \xe2\x90\xa6
# these are values that correspond to the bytes in our unicode codepoint.
# our codepoint was \u2426
# python is making it easier for us to viualise what is going on here.

# \u means what ever after is codepoint
# \x is prefix means the next two digits are hexidecimal 
# \x (hexidecimal) is base 16, means that it is a very convenient mulitple of 2.
# 11111111 is the highest value we get with 8 digits in binary
# in base 16 we can do the same in 2 digits. FF = 11111111 = 255

#### Hexidecimal_conversions ####

# You might have noticed in the last screen that using .encode() turned code points into something like \xe2\x90\xa6.
# These are three hexadecimal bytes.
# The \x prefix means "the next two digits are in hexadecimal".
# Two hexadecimal digits equal 8 binary digits, because digits can have higher values in hexadecimal (base 16).
# For instance, "F" is 15 in hexadecimal, but 1111 is 15 in binary.
# Because it's shorter to display, and 4 binary digits always equal 1 hexadecimal digit,
# programs often use hexadecimal to print out values.
# This is purely for convenience.
# Let's experiment a bit with hexadecimal conversions.




# F is the highest single digit in hexadecimal (base 16)
# Its value is 15 in base 10
print(int("F", 16))

# A in base 16 has the value 10 in base 10
print(int("A", 16))

# Just like the earlier binary_add function, this adds two hex numbers
def hexadecimal_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

# When we add 1 to 9 in hexadecimal, it becomes "a"
value = "9"
value = hexadecimal_add(value, "1")
print(value)

# Add "2" to "ea" in hexadecimal. Assign the result to hex_ea.
# Add "e" to "f" in hexadecimal. Assign the result to hex_ef.

hex_ea = hexadecimal_add("ea","2")
print(hex_ea)  # ec
hex_ef = hexadecimal_add("e","f")
print(hex_ef)  # 1d


#### Hex_to_binary ####

# We can convert hexadecimal to binary pretty easily.
# We can even use the ord() and bin() functions that helped us convert code points to binary.

# One byte (8 bits) in hexadecimal (the value of the byte below is \xe2)
hex_byte = "â"

# Print the base 10 integer value for the hex byte
print(ord(hex_byte))

# This gives the exact same value -- remember than \x is just a prefix, and doesn't affect the value
print(int("e2", 16))

# Convert the base 10 integer to binary
print(bin(ord("â")))

# Convert the hexadecimal byte "\xaa" to binary. Assign the result to binary_aa.
# Convert the hexadecimal byte "\xab" to binary. Assign the result to binary_ab.

binary_aa = bin(int("aa", 16))
binary_ab = bin(int("ab", 16))


#### Bytes_and_strings ####

# Once we have an object with datatype bytes, there isn't an encoding associated, 
# so python doesn't know how to display the (encoded) code points in it.
# Because of this, we can't mix bytes objects and strings together.

hulk_bytes = "Bruce Banner␦".encode("utf-8")
print(hulk_bytes)
print(type(hulk_bytes))
# We can't mix strings and bytes
# For instance, if we try to replace the unicode ␦ character as a string, it won't work, because that value has been encoded to bytes
try:
    hulk_bytes.replace("Banner", "")
except Exception:
    print("TypeError with replacement")

# We can create objects of the bytes datatype by putting a b in front of the quotation marks in a string
hulk_bytes = b"Bruce Banner"
print(hulk_bytes)

# Now, instead of mixing strings and bytes, we can use the replace method with bytes objects instead
hulk_bytes.replace(b"Banner", b"")
print(hulk_bytes.replace(b"Banner", b""))

# Make a bytes object containing "Thor", and assign it to thor_bytes.

thor_bytes = b"Thor"


#### Decode_bytes_to_string ####

# Once we have a bytes object, we can decode it into a string using an encoding.
# We use the .decode() method to do this.

# Make a bytes object with aquaman's secret identity
aquaman_bytes = b"Who knows?"
print(type(aquaman_bytes))
# Now, we can use the decode method, along with the encoding (utf-8) to turn it into a string.
aquaman = aquaman_bytes.decode("utf-8")

# We can print the value and type out to verify that it is a string.
print(aquaman)
print(type(aquaman))

morgan_freeman_bytes = b"Morgan Freeman"

# Decode morgan_freeman_bytes using the 'utf-8' encoding. Assign the result to morgan_freeman.

morgan_freeman = morgan_freeman_bytes.decode("utf-8")
print(morgan_freeman)
print(type(morgan_freeman))


#### Read_in_file_data ####

# Now that we understand unicode, we can go ahead and read our data in.
# The data has a lot of symbols and other unicode characters, 
# so we'll learn how to deal with them as we go along.

# We can read our data in using csvreader
import csv
# When we open a file, we can specify the encoding that it's in.  In this case, utf-8
f = open("sentences_cia.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
sentences_cia = list(csvreader)

# The data is two columns
# First column is year, second is a sentence from a CIA report written that year
# Print the first column of the second row
print(sentences_cia[1][0])

# Print the second column of the second row
print(sentences_cia[1][1])

# Print first row
print(sentences_cia[0])

# Assign the second column of the tenth row in sentences_cia to sentences_ten.
sentences_ten = sentences_cia[9][1]
print(sentences_ten)


#### Convert_to_a_dataframe ####

# In order to make this easier for ourselves, let's convert our sentences to a pandas dataframe.
# Having a dataframe will make processing and analysis much simpler because we can use the .apply() method.

import csv
# Let's read in the legislators data from a few missions ago
f = open("legislators.csv", 'r', encoding="utf-8")
csvreader = csv.reader(f)
legislators = list(csvreader)
# print(legislators[1:10]) list of lists

# Now, we can import pandas and use the DataFrame class to convert the list of lists to a dataframe
import pandas as pd

legislators_df = pd.DataFrame(legislators)

# As you can see, the first row is the headers, which we don't want (it's not actually data, it's just headers)
print(legislators_df.iloc[0,:])

# In order to remove the headers, we'll subset the df and pass them in separately
# This code removes the headers from legislators, and instead passes them into the columns argument
# The columns argument specifies column names
legislators_df = pd.DataFrame(legislators[1:], columns=legislators[0])
# We now have the right data in the first row, and the proper headers
print(legislators_df.iloc[0,:])

print("________________")
# The sentences_cia data from last screen is available.

# Convert sentences_cia to a dataframe. Remember to deal with the headers properly. 
# Assign the result to sentences_cia_df.

print(sentences_cia[0])
sentences_cia_df = pd.DataFrame(sentences_cia[1:], columns = sentences_cia[0])

print(sentences_cia_df.iloc[0,:])


#### Clean_up_sentences ####

# Now that we have our data in a nice format, we need to process the strings to count up term occurences.
# First, though, we need to clean up the strings so that extraneous symbols are removed. 
# We only really care about letters, digits, and spaces.
# Luckily, we can check the integer code of each character using ord() to see if it's a character we want to keep.

# The integer codes for all the characters we want to keep
good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]

sentence_15 = sentences_cia["statement"][14]
#print(sentence_15)
# Iterate over the characters in the sentence, and only take those whose integer representations are in good_characters
# This will construct a list of single characters
cleaned_sentence_15_list = [s for s in sentence_15 if ord(s) in good_characters]

# Join the list together, separated by "" (no space), which creates a string again
cleaned_sentence_15 = "".join(cleaned_sentence_15_list)
#print(cleaned_sentence_15)

# Make a function that takes a dataframe row, 
# and then returns the cleaned up version of the "statement" column.
# Use the .apply() method on dataframes to apply the function to each row of sentences_cia.
# Assign the resulting vector to the cleaned_statement column of sentences_cia.
# You will have to initialize good_characters inside your function.

## Attempt 1

sentence_20 = sentences_cia["statement"][20]
#print(sentence_20)

cleaned_sentence_20_list = []
for item in sentence_20:
    if ord(item) in good_characters:
        cleaned_sentence_20_list.append(item)
cleaned_sentence_20 = "".join(cleaned_sentence_20_list)
#print(cleaned_sentence_20)

# 9 is missing from the list. print(ord("9")) > 57

def clean_rows(row):
    sentence_row = sentences_cia["statement"][row]
    cleaned_sentence_row_list = [s for s in sentence_row if ord(s) in good_characters]
    cleaned_sentence_row = "".join(cleaned_sentence_row_list)
    return cleaned_sentence_row

print(clean_rows(20))
print(cleaned_sentence_15)

#cleaned_statement = sentences_cia.apply(clean_rows, axis=1)

cleaned_statement_list = []
for row in sentences_cia["statement"]:
	cleaned_statement_list.append(clean_rows(row))




## Hint:
## Write a function that takes in the row as an argument. Get the "statement" value from the row.
## Create good_characters by setting the variable equal to the list of integers you see above.
## Then, do the cleaning, and return the cleaned up statement.
## Finally, use the .apply() method on sentences_cia and pass in the function, along with setting the axis to 1 (by row).
## Set the "cleaned_statement" column of sentences_cia equal to the result.


## Attempt 2

def clean_rows(row):
    sentence_row = sentences_cia["statement"][row]
    good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 
    72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 
    99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 
    116, 117, 118, 119, 120, 121, 122, 32]
    cleaned_sentence_row_list = [s for s in sentence_row if ord(s) in good_characters]
    cleaned_sentence_row = "".join(cleaned_sentence_row_list)
    return cleaned_sentence_row

sentences_cia["cleaned_statement"] = sentences_cia.apply(clean_rows, axis=1)


## Answer

def clean_statement(row):
    good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]
    statement = row["statement"]
    clean_statement_list = [s for s in statement if ord(s) in good_characters]
    return "".join(clean_statement_list)

sentences_cia["cleaned_statement"] = sentences_cia.apply(clean_statement, axis=1)


## So I made function, clean_rows, that takes a row number eg 15 or 20 and returns the cleaned statement for that row.

## when creating a function that will work with apply (all rows), this does not work.

## Write a function that takes a DataFrame row...

def function_stuff(row):
	stuff_function_on = row["stuff"]

df.apply(function_stuff, axis=1)


#### Tokenize_statements ####

# Now, we need to combine the sentences and turn them into tokens.
# The eventual goal is to count up how many times each term occurs.

# We can use the .join() method on strings to join lists together.
# The string we use the method on will be used as the separator -- the character(s) between each string when they are joined.
combined_statements = " ".join(sentences_cia["cleaned_statement"])
print(type(combined_statements)) #string

# Tokenize combined_statements by splitting it into words on spaces.
# You should end up with a list of all the words in combined_statements.
# Assign the result to statement_tokens.

statement_tokens = combined_statements.split(" ")
print(type(statement_tokens[1])) #string
print(statement_tokens[1:10]) #list of strings

# statement_tokens has been loaded in.

# Filter the tokens
# We want to count up how many times each term occurs in our data, so we can find the most common items.
# The problem is that the most common words in the English language 
# are ones that are relatively uninteresting to us right now -- 
# words like "the", "a", and so on.

# These words are called stopwords -- words that don't add much information to our analysis.
# A common way to deal with this by filtering out any words that is in a list of known stopwords.
# What we'll do for the sake of simplicity here is to filter out 
# any words that are less than 5 characters long.
# This should remove most of the least interesting words.


# Filter the statement_tokens list so that it only contains tokens 5 characters or more in length. 
# Assign the result to filtered_tokens.

filtered_tokens = []
for item in statement_tokens:
    if len(item) > 4:
        filtered_tokens.append(item)
print(filtered_tokens[1:10])

# Equivalent to:

filtered_tokens = [item for item in statement_tokens if len(item) > 4]

# count occurances of items

count_occurances = {}
for item in statement_tokens:
    if item in count_occurances:
        count_occurances[item] = count_occurances[item] + 1
    else:
        count_occurances[item] = 1

print(count_occurances)


#### Count_the_tokens ####

# Now that we've filtered the tokens, we can count up how many times each one occurs.
# The Counter object from the collections library will help us with this.
# Counter takes a list as input, and creates a dictionary where the keys are list items, 
# and the values are how many times those items appear in the list.

from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# Each of the items in the list has been counted up, and given a dictionary key
print(fruit_count)

# filtered_tokens has been loaded in


# Count up the items in filtered_tokens. Assign the result to filtered_token_counts.

filtered_token_counts = Counter(filtered_tokens)

print(filtered_token_counts)

print(filtered_token_counts["interrogation"])

count_occurances = {}
for item in statement_tokens:
    if item in count_occurances:
        count_occurances[item] = count_occurances[item] + 1
    else:
        count_occurances[item] = 1

## they give the same answer
print(count_occurances["interrogation"])  #> 391
print(filtered_token_counts["interrogation"])  #> 391


#### Most_common_tokens ####

# Now that we have a Counter object created using filtered_tokens as input, let's get the most common tokens out.

from collections import Counter
fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# We can use the most_common method of a Counter class to get the most common items
# We pass in a number, which is the number of items we want to get
print(fruit_count.most_common(2))
print(fruit_count.most_common(3))

# filtered_token_counts has been loaded in

# Get the 3 most common items in filtered_token_counts. Assign the result to common_tokens.

# from notes...
max_val = None
for key,value in filtered_token_counts.items():
    if max_val is None or value > max_val:
        max_val = value
        print(key)
        print(value)
  
# new,

common_tokens = filtered_token_counts.most_common(3)
print(common_tokens)


#### Finding_the_most_common_tokens_by_year ####

# Let's write a function to compute the most common terms by year.

# sentences_cia has been loaded in.
# It already has the cleaned_statement column.

# Write a function to find the 3 most common terms in sentences_cia in a given year (the "year" column).

# The "year" column in sentences_cia stores strings, so you'll need to pass strings into the function.
# You'll need to select the rows in sentences_cia that match that year, 
# combine the cleaned statements, 
# split into a list based on " ", 
# filter out the words with a length of less than 5, 
# make a counter object with the results, 
# and finally find the 2 most common items in the counter.

# Use the function to find the most common terms for "2000". Assign to common_2000.
# Use the function to find the most common terms for "2002". Assign to common_2002.

# possible years: 1997,1998,1999,2000,2001,2002,2010,2011,2012,2013,2014



#print(sentences_cia.loc[0]["cleaned_statement"])
# prints the firstclean statement from the df.

# step 1 get unique list of all years.
list_of_years = sentences_cia.iloc[:,0]
#print(set(list_of_years))
#print(sentences_cia["cleaned_statement"])

from collections import Counter
def most_common_terms_by_year(year):
    subset_by_year = (sentences_cia[sentences_cia["year"] == str(year)])
    combined_statements = " ".join(subset_by_year["cleaned_statement"])
    statement_tokens = combined_statements.split(" ")
    filtered_tokens = [item for item in statement_tokens if len(item) > 4]
    filtered_token_counts = Counter(filtered_tokens)
    common_tokens = filtered_token_counts.most_common(2)
    return common_tokens


common_2000 = most_common_terms_by_year("2000")
print(common_2000)
# > [('Ahmed',9), ('terrorist',9)] 

common_2002 = most_common_terms_by_year("2002")
print(common_2002)
# > [('interrogation',275), ('Zubaydah',252)] 

common_2013 = most_common_terms_by_year("2013")
print(common_2013)
# > [('Response',196), ('states',111)] 

## Answer
from collections import Counter
def find_most_common_by_year(year, sentences_cia):
    data = sentences_cia[sentences_cia["year"] == year]
    combined_statement = " ".join(data["cleaned_statement"])
    statement_split = combined_statement.split(" ")
    counter = Counter([s for s in statement_split if len(s) > 4])
    return counter.most_common(2)

common_2000 = find_most_common_by_year("2000", sentences_cia)
common_2002 = find_most_common_by_year("2002", sentences_cia)
common_2013 = find_most_common_by_year("2013", sentences_cia)