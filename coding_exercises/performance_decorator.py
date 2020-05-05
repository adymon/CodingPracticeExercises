# performance decorator created here measures the time taken by function to execute
from time import time


# defining a decorator
def performance(func):
    def wrapper_performance(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} seconds to finish execution')
    return wrapper_performance


# using decorator
@performance
def performance_check():
    for i in range(100000):
        print(i)


performance_check()
