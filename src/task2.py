import contextlib
from inspect import *
import time
import io

def decorator_2(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        fun(args, kwargs)
        end = time.time() - start
        print(f'{fun.__name__} call {wrapper.calls} executed in {round(end, 4)} sec\n')
        print('Name: ', '\t', fun.__name__)
        print('Type: ', '\t', type(fun))
        sig = signature(fun)
        print('Sign: ', '\t', str(sig))
        print('Arg: ', '\t', 'positional', args)
        print('Arg: ', '\t', 'kwarg', kwargs)
        print('Doc: ', '\t', fun.__doc__)
        print('Source: ', '\t', getsource(fun))
        print('Output: ')
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            fun(args, kwargs)
        s = f.getvalue()
        for i in s.splitlines():
            print(f'\t {i}')
        return

    wrapper.calls = 0
    return wrapper
