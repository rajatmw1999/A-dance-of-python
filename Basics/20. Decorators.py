# Put simply: decorators wrap a function, modifying its behavior.

# By definition, a decorator is a function that takes another function,
#  and extends the behavior of the latter function without explicitly modifying it.
import time

def mydec(func):
    def wrapper():
        print("Starting the decorator code")
        func()
        print("Ending the decorator code")
    return wrapper

def functimedeco(func):
    def wrapper():
        start = time.time()
        print(start)
        func()
        end = time.time()
        print(end)
    return wrapper

@mydec
def helloworld():
    print("Hello World")

@functimedeco
def looping():
    i=0
    while i<10000000:
        i=i+1

looping()
# helloworld()

# https://realpython.com/primer-on-python-decorators/