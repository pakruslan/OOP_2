import time
from datetime import datetime
import functools
# 1. Напишите функцию say_whee, которая печатает «Whee!». Примените к этой функции
# декоратор, который будет запускать функцию say_whee только в течение дня (9:00 —
# 21:00), чтобы не беспокоить соседей.


# def data(fn):
#     def wrapper():
#         if 9 >= datetime.now().hour < 21:
#             fn()
#         else:
#             print("Тише соседи спят")
#     return wrapper


# @data
# def say_whee():
#     print("WHEE!!!")

# say_whee()



# 2. Напишите декоратор, который может узнать время выполнения функции, к которой он
# применен.


# def timer(f):
#     def tmp(*args, **kwargs):
#         t = time.time()
#         res = f(*args, **kwargs)
#         print ("Время выполнения функции: %f" % (time.time()-t))
#         return res

#     return tmp

# @timer
# def func(x, y):
#     return x + y

# func(1, 2)


# 3.







def repeat(nbrTimes=4):
    def real_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            nonlocal nbrTimes
            while nbrTimes != 0:
                nbrTimes -= 1
                func(*args, **kwargs)
        return wrapper_repeat
    return real_repeat

@repeat(4)
def display(x):
    print(x)

display("Python")

