# Python program to convert
# JSON file to CSV


import json
import csv
import time

# Opening JSON file and loading the data
# into the variable data
print(time.time())
with open('data.json') as json_file:
	data = json.load(json_file)
    

employee_data = data['emp_details']

# employee_data = employee_data[0]

# i=0 
# while i<20000:
#     moredata = employee_data[0]
#     employee_data.append(moredata)
#     i=i+1
# print(employee_data)
# dictionary = {}

# dictionary['emp_details'] = employee_data

# output =  open('data.json','w')
# output.write(json.dumps(employee_data))


# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
	if count == 0:

		# Writing headers of CSV file
		header = emp.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(emp.values())

data_file.close()
print(time.time())


# 20,000 rows => 0.3 seconds
# 30,000 rows => 0.6 seconds
# 40,000 rows => 0.6 seconds
# 60,000 rows => 1.2 seconds