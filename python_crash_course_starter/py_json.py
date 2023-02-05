# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json 

# Sample JSON
userJSON_ok = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to Dictionary
user_ok = json.loads(userJSON_ok)

#print(user_ok)
#print(user_ok["first_name"])

car_ok = {"make": "Ford", "model": "Mustang", "year": 1970}
carJSON_ok = json.dumps(car_ok)

print(carJSON_ok)
