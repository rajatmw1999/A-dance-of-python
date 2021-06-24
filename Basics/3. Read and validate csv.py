# pandas is used as it makes parsing of csv very easier and customizable compared to csv module
from pandas import read_csv
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

def checkcolumns(columns):
    rule = ['Name','Email','Gender','Phone','Post']
    try:
        i=0
        while i<len(rule):
            if rule[i] != columns[i]:
                print("Column mis-match, expected '{}', got '{}'".format(rule[i], columns[i]))
                return False
            i+=1
        return True
    except Exception as e:
        print(e)

def checkdata(data):
    try:
        # email column validation
        email_data = data["Email"].tolist()
        for x in email_data:
            if re.search(regex,x):   
                pass   
            else:   
                print("Invalid Email : " + str(x))
                return False
        
        # gender column validation
        gender_data = data["Gender"].tolist()
        for x in gender_data:
            if x != 'M' and x != 'F':
                print("Invalid gender value, expected M or F, got '{}'".format(x))
                return False
        
        # phone number validation
        phone_data = data["Phone"].tolist()
        for x in phone_data:
            if len(str(x))!=10:
                print("Invalid length of phone number, expected 10, got '{}', length = '{}'".format(x, len(str(x))))
                return False
        
        # post value validation
        posts = ['Boss', 'Worker']
        post_data = data["Post"].tolist()
        for x in post_data:
            if x not in posts:
                print("Invalid value of Post, expected '{}', got '{}'".format(posts,x))
                return False
    except Exception as e:
        print(e)


def readandvalidate(filename):
    try:
        # reading CSV file
        data = read_csv(filename)

        # get all the columns of csv
        columns = []
        
        # iterating the columns
        for col in data.columns:
            columns.append(col)
        ans = checkcolumns(list(columns))
        if ans == True:
            if checkdata(data) == True:
                print("File succeded")
    except Exception as e:
        print(e)

readandvalidate('file1.csv')