
def dectrycatch(func):
    def wrapper():
        try:
            print("this is the decorator")
            func()
        except Exception as e:
            print("exception wrapper")
            print(e)
    return wrapper

def funcdiv2():
    print("heeople div2")
    print(5/0)

def funcdiv1():
    print("Hello people")
    funcdiv2()

@dectrycatch
def mainfunc():
    print("Halo from mainfunc")
    funcdiv1()
    print("done")


mainfunc()