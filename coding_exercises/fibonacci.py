"""
Fibonacci Series : 0,1,1,2,3,5,8,13,21,34......
"""
import time


# Using Generators
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


t0 = time.time()
x = fib(10000)

for i in x:
    print(i)

t1 = time.time()

print(f"{t1 - t0} seconds")

time.sleep(5)


# Using List

def fibb(num):
    a = 0
    b = 1

    fibo = []

    for i in range(num):
        fibo.append(a)
        temp = a
        a = b
        b = temp + b
    return fibo


t0 = time.time()
print(fibb(10000))
t1 = time.time()

print(f"{t1 - t0} seconds")
