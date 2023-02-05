# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers_ok = [1,2,3,4,5]
fruits_ok = ["Apples", "Oranges", "Grapes", "Pears"]

# Use a Constructor
numbers2_ok = list((1,2,3,4,5))

# Get a Value
print(fruits_ok[1])

# Get Length
print(len(fruits_ok))

# Append  to Lİst
fruits_ok.append("Mangos")

# Remove from List
fruits_ok.remove("Grapes")

# Insert into Position
fruits_ok.insert(2, "Strawberies")

# Change Value
fruits_ok[0] = "Blueberries"

# Remove with Pop
fruits_ok.pop(2)

# Reverse List
fruits_ok.reverse()

# Sort List
fruits_ok.sort()

# Reverse Sort
fruits_ok.sort(reverse=True)


print(fruits_ok)




