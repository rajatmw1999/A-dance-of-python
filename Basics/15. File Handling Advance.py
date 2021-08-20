
removenames = ['Tywin Lannister','Catelyn Stark']

myfile = open('GameofThrones.txt','r')
myreaddata = myfile.readlines()

myfile.close()

myfile = open('GameofThrones.txt','w')
for x in myreaddata:
    y = x[:-1]
    if y not in removenames:
        myfile.write(x)



# mywritefile = open('writefile.txt','w')
# mywritefile.write("Hello")
# mywritefile.write("World")
