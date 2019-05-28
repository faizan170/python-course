# Import the python libraries
from pymongo import MongoClient

# Choose the appropriate client
client = MongoClient()

# Connect to the test db 
db=client.uni

# Use the employee collection
employee = db.employee



employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

# Use the insert method
result = employee.insert_one(employee_details)

# Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)
