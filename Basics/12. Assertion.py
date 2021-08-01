
def assertion_without_trycatch():
    age = int(input("Please enter your age : "))
    # age = int(age)
    assert (age>0),"Age has to be greater than 0"
    print("Awesome")

assertion_without_trycatch()