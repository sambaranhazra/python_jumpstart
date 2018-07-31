from functools import wraps
from time import time


def timed_execution(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print('Execution time:', (end_time - start_time))
        return result

    return wrapper


@timed_execution
def sum_list():
    return sum([i for i in range(1, 1000000)])


@timed_execution
def sum_gen():
    return sum(i for i in range(1, 1000000))


print(sum_list())
print(sum_gen())


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)

        return wrapper

    return inner


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(add_to_ten(2, 3))
print(add_to_ten(10, 2))
