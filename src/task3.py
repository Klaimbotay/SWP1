import time
from inspect import *
import io
import contextlib

rank = {}
class decorator_3:
    def __name__(self, func):
        return func.__name__

    def __init__(self, func):
        self.count = 0
        self.func = func
        self.name = func.__name__

    def __call__(self, *args, **kwargs):
        global rank
        self.count += 1
        start = time.time()
        self.func(args, kwargs)
        end = time.time() - start
        with open('output_file.txt', 'a') as out:
            out.write(f'{self.name} call {self.count} executed in {round(end, 4)} sec\n')
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
