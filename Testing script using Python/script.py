import pandas as pd
import requests
from colorama import init
from termcolor import colored

format_row12 = "{:>12}"
format_row4 = "{:>4}"

dfs = pd.read_excel('data.xlsx')
data = list(dfs['data'])
name = list(dfs['name'])

print("\n\n==================================")
print("TEST SUITE INITIATED")
print("TOTAL TCs = ", len(data))
print("==================================")

i=1
tcsuccess, tcfail = 0,0
ite = 0

format_row10 = "{:>10}"

for x in data:
    url = "#"
    response = requests.post(url, data=x)
    if response.status_code == 200:
        init()
        print(format_row4.format(i), format_row12.format(colored('Pass', 'green')),format_row12.format(name[ite]))
        tcsuccess += 1
    else:
        init()
        print(format_row4.format(i), format_row12.format(colored('Fail', 'red')),format_row12.format(name[ite]),  format_row10.format(colored(response.text,'red')))
        tcfail += 1
    i=i+1
    ite = ite+1

print("\n\nTotal Test Cases : ", i-1)
print("Failed Test Cases : ", tcfail)
print("Success Test Cases : ", tcsuccess)