import threading
import time
def fun1():
    for i in range(10000000):
        j=i
    
def fun2():
    for i in range(10000000):
        j=i

t1 =  threading.Thread(target=fun1)
t2 =  threading.Thread(target=fun2)

start = time.time()
# fun1()
# fun2()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-start)