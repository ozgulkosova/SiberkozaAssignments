# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create Function
def sayHello(name):
    print(f"Hello {name}")
#sayHello("John Doe")    

# Return Values
def getSum(num1_ok, num2_ok):
    total = num1_ok + num2_ok
    return total
num_ok = getSum(5, 3)
#print(num_ok)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1_ok, num2_ok : num1_ok + num2_ok

#print(getSum(10, 3))