"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %.2f, z is "%s"' % (x, y, z))

"""
Printf-style String Formatting
We use the modulus operator (%) to signify the start of a specifier followed by a character that determines the formatting that will be applied

#####Conversions#####
%d  |  Signed integer decimal
%f  |  Floating point decimal format
%s  |  String (converts any python object using str())
#####Conversions#####
"""

# Use the 'format' string method to print the same thing
str = 'x is {:d}, y is {:.2f}, z is "{:s}"'
print(str.format(x, y, z))

"""
"format" works almost identically to the "printf" method of formatting. Instead of using the modulus operator we use the the ":" character to signify the start of a specifier
"""

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y:.2f}, z is "{z}"')
