myfile = open('data.txt')
data = myfile.read()
if data[0] == '<':
    print("XML")
elif data[0] == '{':
    print("JSON")