

def writefile():
    myfile = open('webseries.txt','w')
    myfile.write("\nLoki")

def appendfile():
    myfile = open('webseries.txt','a')
    myfile.write("\nMoney Heist")

def readfile():
    myfile = open('webseries.txt','r')
    data = myfile.read()
    print(data)

def myfavseries():
    myfav = input("Please enter your favorite web series : ")
    print("Searching if we have it this series or not ....")
    myfile = open('webseries.txt','r')
    mydata = myfile.readlines()
    i=0
    while i<len(mydata):
        mydata[i] = mydata[i][:-1]
        i=i+1
    flag = 1
    for x in mydata:
        # print(x)
        if x.lower() == myfav.lower():
            print("We have the series")
            flag = 0
    if flag == 1:
        print("We don't have that series")

myfavseries()

# open a text file in write mode
# open a text file in read mode
# open a text file in append mode