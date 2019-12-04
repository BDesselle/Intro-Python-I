"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
# The "os" module provides a portable way of using operating system dependent functionality.
import sys
# The "sys" module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

# Print out the command line arguments in sys.argv, one per line:
for args in sys.argv:
    print(args)

"""
"argv" returns a list of command line args passed to a python script.
"""

# Print out the OS platform you're using:
print(sys.platform)

"""
"platform" returns a string containing the platform value of your OS.
"""

# Print out the version of Python you're using:
print(sys.version)

"""
"version" returns a string containing the version number of your current python interpreter.
"""

# Print the current process ID
print(os.getpid())

"""
"getpid" returns the current process id.
"""

# Print the current working directory (cwd):
print(os.getcwd())

"""
"getcwd" returns a string representing the current working directory.
"""

# Print out your machine's login name
print("Machine: " + os.getenv('COMPUTERNAME'), "\nUser: " + os.getenv('USERNAME') )

"""
"getenv" returns a string containing the value of the environment variable key if it exists.
"""
