import time
from inspect import *  # try to avoid this

#RV imports
from task3 import print_ranks

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
            with open('output_file.txt', 'a') as out:
                out.write(f'{self.func.__name__} call {self.count} executed in {round(time.time() - start, 4)} sec\n')
                out.write(f'Name: \t {self.func.__name__}\n')
                out.write(f'Type: \t {type(self.func)}\n')
                out.write(f'Sign: \t {str(signature(self.func))}\n')
                out.write(f'Args: \t positional {args}\n')
                out.write(f'      \t kwarg {kwargs}\n\n')
                out.write(f'Doc: \t {self.func.__doc__}\n')
                lines = getsourcelines(self.func)
                out.write('Source: \t')
                for l in lines[0]:
                    out.write('\t' + str(l))
                out.write(f'\nOutput: \t {str(self.func(args, kwargs))}\n\n\n')

        except Exception as Argument:
            with open('log_file.txt', 'a') as out:
                out.write(f'Error with function {self.func.__name__}')
                out.write(str(Argument) + '\n')

        end = time.time() - start
        rank[self.func.__name__] = round(end, 5)
        return

    # display via class function
    @staticmethod
    def print_ranks():
        global rank
        print_ranks(rank)


def decorator_5(fun):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        try:
            start = time.time()
            fun(*args, **kwargs)  # use * and **
            end = time.time() - start
            print(f'{fun.__name__} call {wrapper.calls} executed in {round(end, 4)} sec\n')
            print('Name: ', '\t', fun.__name__)
            print('Type: ', '\t', type(fun))
            print('Sign: ', '\t', str(signature(fun)))
            print('Args: ', '\t', 'positional', args)
            print('      ', '\t', 'kwarg', kwargs)
            print('Doc: ', '\t', fun.__doc__)
            lines = getsourcelines(fun)
            print('Source: \t', end='')
            for l in lines[0]:
                print('\t' + str(l), end='')
            print(f'\nOutput: \t {str(fun(*args, **kwargs))}\n\n')
            print('\n')

        except Exception as Argument:
            with open('log_file.txt', 'a') as out:
                out.write(f'Error with function {fun.__name__}')
                out.write(str(Argument) + '\n')
        return

    wrapper.calls = 0
    return wrapper
