# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ok = "Ozgul"
age_ok = 40

# Concatenate

#print("Hello, my name is " + name_ok + " and I am " + str(age_ok))

# String Formatting



# Argument by Position

#print("My name is {name_ok} and I am {age_ok}".format(name_ok=name_ok, age_ok=age_ok))

# F-Strings (3.6+)

#print(f"Hello, My name is {name_ok} and I am {age_ok}")

# String Methods

s_ok = "hello world"

# Capitaalize String

print(s_ok.capitalize())
print(s_ok.upper())
print(s_ok.lower())
print(s_ok.swapcase())
print(s_ok.replace("world", "everyone"))
print(s_ok.startswith("hello"))
print(s_ok.endswith("d"))
print(s_ok.split())
print(s_ok.find("e"))
print(s_ok.isalnum())
print(s_ok.isnumeric())
print(s_ok.isalpha())









