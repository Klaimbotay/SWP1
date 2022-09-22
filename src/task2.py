from inspect import *
import time
import contextlib, io


def decorator_2(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            output = fun(args, kwargs)
        end = time.time() - start
        print(f'{fun.__name__} call {wrapper.calls} executed in {round(end, 4)} sec\n')
        print('Name: ', '\t', fun.__name__)
        print('Type: ', '\t', type(fun))
        print('Sign: ', '\t', str(signature(fun)))
        print('Args: ', '\t', 'positional', args)
        print('      ', '\t', 'kwarg', kwargs, '\n')
        print('Doc: ', '\t', fun.__doc__)
        lines = getsourcelines(fun)
        print('Source: \t', end='')
        for l in lines[0]:
            print('\t' + str(l), end='')
        print(f'\nOutput: \t {str(output)}\n\n\n')
        return output

    wrapper.calls = 0
    return wrapper
