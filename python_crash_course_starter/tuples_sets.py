# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create Tuple
fruits_ok = ("Apples", "Oranges", "Grapes")
#fruits2_ok = tuple(("Apples", "Oranges", "Grapes"))

# Single Value Needs Comma
fruits2_ok = ("Apples",)

# Get Value
print(fruits_ok[1])

# Can't Chance Value
#fruits_ok[0] = "Pears"

# Delete Tuple
#del fruits2_ok
#print(fruits2_ok)

# Get Length
print(len(fruits_ok))




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create Set
fruits_set_ok = {"Apples", "Oranges", "Mango"}

# Check if in a Set
print("Apples" in fruits_set_ok)

# Add to Set
fruits_set_ok.add("Grape")

# Remove from Set
fruits_set_ok.remove("Grape")

# Add Duplicate
fruits_set_ok.add("Apples")

# Clear Set
#fruits_set_ok.clear()

# Delete
#del fruits_set_ok

print(fruits_set_ok)






























