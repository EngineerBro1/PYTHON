# Function caching in Python refers to the technique of storing the results of expensive function calls and returning the cached result when the same inputs occur again. This can significantly improve the performance of the application by avoiding redundant computations.
# Python provides several ways to implement function caching, including using decorators from the functools module, using third-party libraries like functools.lru_cache, or implementing custom caching mechanisms.

# Using functools.lru_cache::

from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(20))

# Using a Custom Decorator::


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrapper

@memorize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(20))



# Using a Dictionary for Caching::

def fibonacci(n,cache={}):
    if n in cache:
        return cache[n]
    if n<=1:
        return n
    result = fibonacci(n-1, cache) + fibonacci(n-2,cache)
    cache[n]=result
    return result

print(fibonacci(20)) 
