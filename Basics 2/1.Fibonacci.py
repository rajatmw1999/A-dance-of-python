# print("Hello world!")
# print("I am python. I don't have semicolons or curly brackets")
# print("I name arrays as lists, and objects as dicts")

print("0,1,1,2,3,5,8,13,21 .. Fibonacci Series")

first = 0
second = 1
ans = -1
i=0

print(0)
print(1)

while i<20:
    ans = first + second
    print(ans)
    first = second
    second= ans
    i = i+1