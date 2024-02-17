"""
Learn the use of decorator
"""

"""
Decorator adds some generic lines added in a decorator function after the decorator defined function job is finished
"""

import time

def deco(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() -t1
        print(f"{func.__name__} took {t2:.6f} to complete")
    return wrapper

@deco
def f1():
    time.sleep(3)

@deco
def f2():
    time.sleep(2.5)

f1()

f2()
print("Done")