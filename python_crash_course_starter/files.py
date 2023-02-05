# Python has functions for creating, reading, updating, and deleting files.

# Open File
myFile_ok = open("myfile.txt", "w")

# Get some Info
print("Name : ", myFile_ok.name)
print("Is Closed : ", myFile_ok.closed)
print("Opening Mode : ", myFile_ok.mode)

# Write to File
myFile_ok.write("I love Python")
myFile_ok.write(" and Javascript")
myFile_ok.close()

# Append to File
myFile_ok = open("myfile.txt", "a")
myFile_ok.write(" and I also like PHP")

# Read from File
myFile_ok = open("myfile.txt", "r+")
text = myFile_ok.read(100)

print(text)