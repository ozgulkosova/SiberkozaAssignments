# If/ Else conditions are used to decide to do something based on something being true or false

x_ok = 3
y_ok = 7

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
#if x_ok > y_ok:
    #print(f"{x_ok} is greater than {y_ok}")
    
# if/else
#if x_ok > y_ok:
    #print(f"{x_ok} is greater than {y_ok}")
#else:
    #print(f"{y_ok} is greater than {x_ok}")  
    
#if x_ok > y_ok:
    #print(f"{x_ok} is greater than {y_ok}")
#elif x_ok == y_ok:
    #print(f"{x_ok} is equal to {y_ok}")
#else:
   # print(f"{y_ok} is greater than {x_ok}")
   
# Nested if
#if x_ok > 2:
    #if x_ok <= 5:
        #print(f"{x_ok} is greater than 2 and less than or equal to 5")

# Logical operators (and, or, not) - Used to combine conditional statements

# and
#if x_ok > 2 and x_ok <= 5:
    #print(f"{x_ok} is greater than 2 and less than or equal to 5")

# or
#if x_ok > 2 or x_ok <= 5:
    #print(f"{x_ok} is greater than 2 or less than or equal to 5")

# not
#if not(x_ok == y_ok):
   # print(f"{x_ok} is not equal to {y_ok}")


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_ok = [1,2,3,4,5]

# in
#if x_ok in numbers_ok:
    #print(x_ok in numbers_ok)

# not in
#if y_ok not in numbers_ok:
    #print(y_ok not in numbers_ok)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_ok is y_ok:
    print(x_ok is y_ok)

# is not
if x_ok is not y_ok:
    print(x_ok is not y_ok) 








