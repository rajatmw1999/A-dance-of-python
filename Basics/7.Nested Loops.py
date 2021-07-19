
def for_in_while():
    i=0 
    while i<10:
        for x in [1,2,3]:
            print(str(x) + "\t" + str(x+1))
        i+=1

for_in_while()