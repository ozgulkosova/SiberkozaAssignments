# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_ok = 1            #int
# y_ok = 2.5          #float
# name_ok = "Ozgul"   #str
# is_cool_ok = True   #bool

# Multiple Assignment

x_ok, y_ok, name_ok, is_cool_ok = (1, 2.5, "Ozgul", True)

# Basic Math

a_ok = x_ok + y_ok

print(x_ok, y_ok, name_ok, is_cool_ok, a_ok)
print(type(x_ok))

#Casting

x_ok = str(x_ok)
y_ok = int(y_ok)
z_ok = float(y_ok)

print(type(x_ok))
print(type(y_ok), y_ok)
print(type(z_ok), z_ok)















