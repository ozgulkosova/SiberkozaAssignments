# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ok = ["John", "Paul", "Sara", "Susan"]

# Simple for Loop
#for person_ok in people_ok:
    #print(f"Current Person: {person_ok}")
    
# Break
#for person_ok in people_ok:
    #if person_ok == "Sara":
        #break
    #print(f"Current Person: {person_ok}")
    
# Continue
#for person_ok in people_ok:
    #if person_ok == "Sara":
        #continue
    #print(f"Current Person: {person_ok}")
    
# range
#for i in range(len(people_ok)):
    #print(people_ok[i])
    
#for i in range(0, 11):
    #print(f"Number: {i}")


# While loops execute a set of statements as long as a condition is true.

count_ok = 0
while count_ok < 10:
    print(f"Count: {count_ok}")
    count_ok += 1