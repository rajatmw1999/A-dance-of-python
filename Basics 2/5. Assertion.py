
def assertion(age):
    assert (age>0),"Age should be greater than 0"
    print(age)

def exception():
    try:
        # requests.get("https://google.com")
        print("Hello")
    except Exception as e:
        print(e)

# assertion(-4)
exception()