"""
###############################################################################
PYTHON BASICS
###############################################################################
##################################
Content:
    1. Strings, integers, floats, booleans and their methods
    2. Tuples, lists, dictionaries, sets
    3. Functions, lambda functions, generators
##################################
"""

print(__doc__)

#-----------------------------------------------------------------------------#

# 1. Strings, integers, floats, booleans and their methods

# You have numbers (Integers and Floats)
3
3.1
type(3)
type(3.1)
type(float(3))

# Math is what you would expect
1 + 1
8 - 1
10 * 2
35.5 / 5
35.5 // 5
4 % 2
5 % 2
2 ** 4
9 ** 0.5

# Enforce precedence with parentheses
1 + 3 * 2
(1 + 3) * 2

# Boolean Operators (True or False)
True
type(True)

# Note "and" and "or" are case-sensitive
True and False
True or False

# negate with not
not True
not False

# Equality is ==
1 == 1
2 == 1

# Inequality is !=
1 != 1
2 != 1

# More comparisons
10 > 1
10 < 1
2 <= 1
2 >= 1

# Comparisons can be chained!
1 < 2 < 3
2 < 3 < 2
(1 < 2 < 3) or (2 < 3 < 2)
(1 < 2 < 3) and (2 < 3 < 2)

# Strings are created with " or ' (Strings are simply text)
"This is a string"
type("This is a string")
'This is also a string'

# Strings can be added too!
'Hello' + 'World'

# Remember to add space!
'Hello ' + 'World'

# A string can be treated like a list of characters (Note: Zero-indexing!)
'This is a string'[2]

# Each type has certain methods assigned to it, e.g.,
'this is a string'.capitalize()

# format strings with the format method.
'A triangle has {} sides{}'.format(3, ', right?')

# Note: Python has a print statement
print('I'm Python. Nice to meet you!')


# What is the problem here?
print("I'm Python. Nice to meet you!")

print(1 < 2 < 3)
print(2 < 3 < 2)
print((1 < 2 < 3) or (2 < 3 < 2))
print((1 < 2 < 3) and (2 < 3 < 2))

# No need to declare variables before assigning to them.
some_var = 5

# Python immediately assigns a type to the variable
type(some_var)

# incrementing and decrementing a variable
x = 0
x = x + 1
x
# Alternatively,
x = 0
x += 1
x

#-----------------------------------------------------------------------------#

# 2. Tuples, lists, dictionaries, sets

# Lists store sequences (That is, lists can store integers, floats, or strings, or even a mix of those!)
empty_li = []
type(empty_li)

# Simple list
li = [1,2,3]
li

other_li = [4,5]
other_li + li
li + other_li

# For example, the height of a small class:
height = ['Student 1', 1.73, 'Student 2', 1.68, 'Student 3', 1.71, 'Professor', 1.75]
height

# Add stuff to the end of a list with append
height.append("TA", 1.55)
help(height.append)
# What went wrong here?

height.append("TA")
height.append(1.55)
height

# The insert method gives more control
height.insert(0, 1.86)
height.insert(0, 'me')

# More primitively:
height = height + ['me', 1.86]

# Maybe a more appropriate format is a list of lists
height_ = [['Student 1', 1.73], ['Student 2', 1.68], ['Student 3', 1.71], ['Professor', 1.75]]
height_.append(['me', 1.86])


# Access a list like you would any array (Recall: Zero-indexing!)
height[1]
height_[1]
height_[1][1]

# Assign new values to indexes that have already been initialized with =
height = ['Student 1', 1.73, 'Student 2', 1.68, 'Student 3', 1.71, 'Professor', 1.75]
height[6] = "TA"
height
height[6] = "Professor"
height

# Look at the last element
height[7]
height[-1]
height[len(height)] # Why error?
len(height)
height[len(height) - 1]

#Look at the first element
height[0]
height[-8]

# You can look at ranges with slice syntax.
# (It's a closed/open range.)
height[0:2]
students = height[0:6]
students

# Omit the beginning
height[1:]

# Omit the end
height[:7]

# Check for existence in a list with "in"
"Professor" in height

# Examine the length with "len()"
len(height)

# Remove element from list
del(height[0])
height

# Dictionaries store mappings
empty_dict = {}

# Here is a prefilled dictionary
filled_dict = {"Ja": "Yes", "Nein": "No"}
len(filled_dict)
# Look up values with []
filled_dict["Ja"]

# Check for existence of keys in a dictionary with "in"
"Ja" in filled_dict
"Yes" in filled_dict

"Ja" in filled_dict.keys()
"Yes" in filled_dict.values()


# Looking up a non-existing key is a KeyError
filled_dict["Yes"]

# set the value of a key with a syntax similar to lists
filled_dict["Vielleicht"] = "Maybe"
filled_dict

# Inverse dictionary
inv_filled_dict = {v:k for k,v in filled_dict.items()}


# A tuple is a fixed-length, immutable sequence of Python objects.
tup = 4, 5, 6
nested_tup = (4, 5, 6), (7, 8)
tup = tuple('string')
# Elements can be accessed with square brackets [] 
tup[0]
# It’s not possible to modify which object is stored in each slot    
tup[2] = False

# We can, however, add values
tup += 5, 6

# Unpacking tuples
tup = (4,5,6)
a, b, c = tup
# Suppose we do not care about the middle int
del(a,b,c)
a, _, c = tup


# Sets: Unordered collection of unique elements
my_set = {1, 2, 3}
type(my_set)

a = {'Jacket', 'Shoe', 'Gloves'}
b = {'Car', 'Bike', 'Train'}

a[0] # Why?

a.update({2})
print(a)
a.discard(2)
print(a)
c = a.union(b)
print(c)
d = a.intersection(b)
print(d)


# Let's just make a variable
some_var = 5

# Here is an if statement.
if some_var > 10:
    print("{} is larger than 10".format(some_var))
elif some_var < 10:
    print("{} is smaller than 10".format(some_var))
else:
    print("{} is 10".format(some_var))
    
#-----------------------------------------------------------------------------#

# 3. Functions, lambda functions, generators

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y

# Calling functions with parameters
add(5, 6)
help(add)
# Another way to call functions is with keyword arguments
add(y=6, x=5)

# We can use list comprehensions to loop or filter
[add(i, 10) for i in range(1, 4)]

[x for x in range(3,8) if x > 5]

# Python has many built-in functions
type(height)
max([5, 4, 2, 10, 5, 4, 6])
round(3.25)

# Use 'help' to see what the function does
help(round)
round(3.25, 1)

# Methods: Functions that belong to objects
height.index("Professor")
height.count("Professor")
sister = 'liz'
sister = sister.capitalize()

sister_ = ''
for i in range(len(sister)):
    sister_ += sister[i].capitalize()
    
sister = sister.replace("z", "sa")

# Note: Object have methods associated, depending on type
height.replace("Professor", "TA")
sister.index("z")

# Lambda functions

new_add = lambda x, y: x + y
new_add(2, 3)

# Every lambda function used could be definined properly
# but this may be inefficient

a = ['house', 'car', 'bike']
help(a.sort)
a.sort(key=lambda x: len(x))
a.sort(key=lambda x: len(x), reverse=True)

# Generators:

for i in range(4):
    print(i)

for i in range(4, 8):
    print(i)

# while loops
x = 256
total = 0
while x > 0:
    total += x
    x = x // 2
    print(x)

# You can import modules
import random
print(random.random())
import math
print(math.sqrt(16))

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))
print(floor(3.7))

# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# EXERCISE: Write a function 'is_prime' that takes in an integer
# and checks whether it is a prime number.
# It should print outputs in either case
