import datetime

def func():
    today = datetime.datetime.now()
    val = input("Enter any number : ")
    val = int(val)
    if val>=0 and val<=100:
        print("Valid value")
    else:
        print("Invalid value")
    marks = 70
    print(val)
    print(today)
    names = ["Anay","Ayan","Ajay","Anil","Aman","Abhi"]
    ite = 0
    while ite<len(names):
        print(names[ite])
        ite+=2
    for x in names:
        print(x)

func()

# 1 Display date of today in this format ==> 14th June 2021
# 2 Take 5 numbers as input and calculate percentage, also check if the number are in range 0-100
# 3 Create a list of number. Display the numbers which are odd