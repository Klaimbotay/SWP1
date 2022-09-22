from datetime import datetime


def RV_decorator_1(func):
    """
    Prints count of function's calls and execution time
    """
    count = 0
    f = func

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        time = datetime.now()
        out = func(*args, **kwargs)
        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds():.6f} sec')
        return out
    return wrapper