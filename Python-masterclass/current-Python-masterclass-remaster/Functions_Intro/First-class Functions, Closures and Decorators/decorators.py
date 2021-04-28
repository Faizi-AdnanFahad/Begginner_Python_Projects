# Decorators

# FUNCTIONS
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f'Wrapper executed this before {original_function.__name__}')
#         return original_function(*args, **kwargs)
#
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display function ran')
#
#
# # display = decorator_function(display)
# display()
#
# print('--------------------------------')
#
#
# @decorator_function
# def display_info(name, age):
#     print(f'display_info ran with arguments ({name}, {age})')
#
#
# display_info('John', 25)

print("-------------------------------------------------------------------------------------------------------------")


# # ClASSES
# class decorator_class(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print(f"call method before {self.original_function.__name__}")
#         self.original_function(*args, **kwargs)
#
#
# @decorator_class
# def display():
#     print('display function ran')
#
#
# display()
#
# print('--------------------------------')
#
#
# @decorator_class
# def display_info(name, age):
#     print(f'display_info ran with arguments ({name}, {age})')
#
#
# display_info('John', 25)
#
# print("-------------------------------------------------------------------------------------------------------------")

# Practical Examples


# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
#         return orig_func(*args, **kwargs)
#
#     return wrapper
#

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper

#
# @my_logger
# def display_info(name, age):
#     print(f'display_info ran with arguments ({name}, {age})')
#
#
# display_info('John', 12)


import time

from functools import wraps

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
#
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#
#     return wrapper
#
#
# def my_timer(orig_func):
#     import time
#
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result
#
#     return wrapper
#
# import time
#
#
# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with arguments ({}, {})'.format(name, age))
#
# display_info('Tom', 22)

print("------------------------------------------------------------------------------------------------------------")
