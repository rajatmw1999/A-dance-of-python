# pandas is used as it makes parsing of csv very easier and customizable compared to csv module
from pandas import read_csv

def checkcolumns(columns):
    rule = ['Name','Email','Gender','Phone','Post']
    try:
        i=0
        while i<len(rule):
            if rule[i] != columns[i]:
                print("OOPS! Wrong")
                return False
            i+=1
        return True
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
            print("File succeded")
    except Exception as e:
        print(e)

readandvalidate('file1.csv')