import msgpack
import json
import csv
import time

# Opening JSON file and loading the data
# into the variable data
print(time.time())
with open('data.json') as json_file:
	data = json.load(json_file)
    

employee_data = data['emp_details']
bin = msgpack.packb(employee_data)
# print(bin)