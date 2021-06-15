import boto3
# pandas is used as it makes parsing of csv very easier and customizable compared to csv module
from pandas import read_csv
import re
import os

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def download():
    s3 = boto3.client('s3',aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
        aws_secret_access_key= os.environ.get('SECRET_ACCESS_KEY'))
    s3.download_file('testbucketcsvdownload', 'emails.csv', 'ayan.csv')
    checkemail()

def checkemail():
    try:
        # reading CSV file
        data = read_csv("ayan.csv")

        # converting column data to list individually
        selectedcol = data["Email"].tolist()
        print("All emails : " + str(selectedcol))
        for x in selectedcol:
            if re.search(regex,x):   
                pass   
            else:   
                print("Invalid Email : " + str(x)) 
    except Exception as e:
        print(e)

download()