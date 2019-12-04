"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

-Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
print(x + int(y))

"""
The "int()" function converts the specified value into a number.

#####Syntax#####
int(value, base)
#####Syntax#####

#####Params#####
value  |  A number or string that can be converted into an integer number
base   |  A number representing the number format. Default value: 10
#####Params#####
"""


# Write a print statement that combines x + y into the string value 57
print(str(x) + y)

"""
The "str()" function converts the specified value into a string.

#####Syntax#####
str(object, encoding=encoding, errors=errors)
#####Syntax#####

#####Params#####
object    |  Any object. Specifies the object to convert into a string
encoding  |  The encoding of the object. Default is UTF-8
errors    |  Specifies what to do if the decoding fails
#####Params#####
"""
