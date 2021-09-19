# How to read an excel file in python  
import pandas as pd

data = pd.read_excel('data.xlsx')
result_column = list(data['result'])
name_column = list(data['name'])

i=0
while i<len(result_column):
    print(name_column[i] , "is", result_column[i])
    i=i+1

# print(result_column)