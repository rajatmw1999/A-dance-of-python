
# INTEGER AND FLOAT TYPES
myint = 23
myfloat = 45.91
myfloat2 = 4e+4

print(myint, type(myint))
print(myfloat, type(myfloat))
print(myfloat2, type(myfloat2))

print(5/2)
print(5//2)


# ---------
# STRING TYPES
mystring = "Mohil"
# mystring[0] = "R"
print(mystring)

# -----------------------------
# LIST TYPES 
mylist = [1,2,3,"Rajat","Mohil",4,5,6]
print(mylist)
print(len(mylist))
print(mylist*2)
print(mylist[2:4])
print(12 in mylist)


# ------------------------
# TUPLE TYPE
mytuple = (2,3,4)
mytuple2 = (34,78)
print(mytuple)
print(mytuple[0])
mytuple = mytuple2
print(mytuple)


# -----------------------------
# RANGE TYPE
for i in range(0,5):
    print(i)

for i in range(0,10,2):
    print(i)


# --------------------------------
# SET TYPE
myset = {1,2,3,4,5,6}
myset2 = {8,9,7,4,5,6}
print(myset)
print(myset2)
myset3 = myset.union(myset2)
print(myset3)
print(myset & myset2)
myset.add(123)
print(myset)

# https://techvidvan.com/tutorials/python-sequences/
# https://realpython.com/python-sets/