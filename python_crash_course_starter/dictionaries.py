# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create Dictionary
person_ok = {
    "First_Name" : "John",
    "Last_Name"  : "Doe",
    "Age"        : 30
    }

# Use Constructor
#person2_ok = dict(First_Name="Sara", Last_Name="Williams", )

# Get Value
print(person_ok["First_Name"])
print(person_ok.get("Last_Name"))

# Add Key/Value
person_ok["Phone_Number"] = "555-444-5555"

# Get Dict Keys
print(person_ok.keys())

# Get Dict Items
print(person_ok.items())

# Copy Dict
person3_ok = person_ok.copy()
person3_ok["City"] = "Istanbul"

# Remove Item
del(person_ok["Age"])
person_ok.pop("Phone_Number")

# Clear
person_ok.clear()

# Get Length
print(len(person3_ok))

# List of Dict

people_ok = [
    {"name" : "Martha", "age" : 30},
    {"name" : "Kevin", "age" : 25}
    ]

print(people_ok[1]["name"])



















