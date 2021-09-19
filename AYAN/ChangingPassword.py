#Changing passsword script

a = "GouthamKrishna"
b = "abcxyz"

c = str(input("Enter Username "))
d = str(input("Enter Password "))

if a == c and b == d:
    b = str(input("Enter New Password "))
elif a != c and b == d:
    print("The username is wrong")
elif a == c and b != d:
    print("The password is wrong")
else:
    print("Both username and password are wrong")
