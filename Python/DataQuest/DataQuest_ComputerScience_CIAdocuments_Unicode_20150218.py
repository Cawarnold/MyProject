## DataQuest_ComputerScience_CIAdocuments_Unicode_20150218

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 12

# Basics: Analyze CIA documents

# Learn more about how computers store variables and unicode while analyzing excerpts from CIA reports.	


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








