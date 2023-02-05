# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    #Constructer
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"
    
    def has_birthday(self):
        self.age += 1

#Extend  Class

class Customer(User):
    #Constructer
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"
    

# init User Object
brad_ok = User("Brad Traversy", "brad@gmail.com", 37)
# init Customer
janet_ok = Customer("Janet Johnson", "janet@yahoo.com", 25)

janet_ok.set_balance(500)
brad_ok.has_birthday()

print(brad_ok.greeting())
        










