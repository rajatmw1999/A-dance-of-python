def assertion(age):
    assert (age>0),"Age should be greater than 0"
    print(age)

def exception():
    try:

        print("Hello")
    except Exception as e:
        print(e)

exception()