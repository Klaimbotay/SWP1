import time
import contextlib, io


def decorator_1(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            output = fun(args, kwargs)
        end = time.time() - start
        print(f'{fun.__name__} call {wrapper.calls} executed in {round(end, 4)} sec')
        return output

    wrapper.calls = 0
    return wrapper
