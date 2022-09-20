import time
from inspect import *
import io
import contextlib

rank = {}
class decorator_4:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        global rank
        self.count += 1
        start = time.time()
        try:
            self.func(args, kwargs)
        except Exception as Argument:
            with open('log_file.txt', 'a') as out:
                out.write(str(Argument) + '\n')

        end = time.time() - start
        with open('output_file.txt', 'a') as out:
            out.write(f'{self.func.__name__} call {self.count} executed in {round(end, 4)} sec\n')
            out.write(f'Name: \t {self.func.__name__}\n')
            out.write(f'Type: \t {type(self.func)}\n')
            sig = signature(self.func)
            out.write(f'Sign: \t {str(sig)}\n')
            out.write(f'Arg: \t positional {args}\n')
            out.write(f'Arg: \t kwarg {kwargs}\n')
            out.write(f'Doc: \t {self.func.__doc__}\n')
            out.write(f'Source: \t {getsource(self.func)}\n')
            out.write(f'Output: \t \n')
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                self.func(args, kwargs)
            s = f.getvalue()
            for i in s.splitlines():
                out.write(f'\t {i}')
        rank[self.func.__name__] = end
        return


def decorator_5(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        try:
            fun(args, kwargs)
        except Exception as Argument:
            with open('log_file.txt', 'a') as out:
                out.write(str(Argument))
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