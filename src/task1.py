import time


def decorator_1(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        fun(args, kwargs)
        end = time.time() - start
        print(f'{fun.__name__} call {wrapper.calls} executed in {round(end, 4)} sec')
        return

    wrapper.calls = 0
    return wrapper
