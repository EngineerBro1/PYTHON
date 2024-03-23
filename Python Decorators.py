# Python Decorators::
# In Python, decorators are a powerful feature that allows you to modify or extend the behavior of functions or classes without directly changing their code. Decorators are implemented using functions and the @decorator_name syntax.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening before the function is called.")
#     return wrapper
# def Say_hello():
#     print("Hello")
# Say_hello = my_decorator(Say_hello)
# Say_hello()


# @my_decorator
# def Say_World():
#     print("World")
# Say_World()
# 




# import logging
# def log_fun_call(func):
#     def decorator(*args, **kwargs):
#         logging.info(f"calling{func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorator
# @log_fun_call
# def my_fun(a,b):
#     return a+b





