from inspect import *  # try to avoid this
import time


def decorator_2(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.time()
        fun(args, kwargs)
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
        print(f'\nOutput: \t {str(fun(args, kwargs))}\n\n\n')  # second func call!
        return

    wrapper.calls = 0
    return wrapper
