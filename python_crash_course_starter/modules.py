# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Models
import datetime
from datetime import date
import time
from time import time

# Pip Module
from camelcase import CamelCase

# Import Custom Module
import validator
from validator import validate_email


#today_ok = datetime.date.today()
today2_ok = date.today()
timestamp_ok = time()

c_ok = CamelCase()
print(c_ok.hump("helllo there world"))

email_ok = "test@test.com"
if validate_email(email_ok):
    print("Email is valid")
else:
    print("Email is bad")



