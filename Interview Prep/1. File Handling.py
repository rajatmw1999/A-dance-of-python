
def readfile():
    myfile = open('presidents.txt','r')
    mydata = myfile.read()
    print(mydata)
    myfile.close()

def writefile():
    myfile = open('presidents.txt','w')
    myfile.write("Kovind Obama Putin")
    myfile.close()

def appendfile():
    myfile = open('presidents.txt','a')
    myfile.write(" Netanyahu")
    myfile.close()

def operators():
    myfile = open('presidents.txt','r')
    print(myfile.closed)
    print(myfile.mode)
    print(myfile.name)
    myfile.close()
    print(myfile.closed)

def readwritefile():
    
    myfile = open('presidents.txt','r+')
    myfile.write("Biden")
    mydata = myfile.read()
    print(mydata)
    
    myfile.close()
    
def readlinesfile():
    myfile = open('friends.txt','r')
    mydata = myfile.readlines()

    i=0
    while(i<len(mydata)):
        element = mydata[i]
        mydata[i] = element[:-1]
        i=i+1
    
    print(mydata)

# writefile()
# appendfile()
# readfile()
# operators()
# readwritefile()
readlinesfile()

# More names here
# Rachel
# Phoebe
# Joe