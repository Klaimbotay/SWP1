import time
from inspect import *  # try to avoid this

# RV imports
from io import StringIO
import sys

rank = {}
class decorator_3:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        # changing stdout stream while func executes
        IO_out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = IO_out

        global rank
        self.count += 1
        start = time.time()
        func_out = self.func(*args, **kwargs)  # use * and **
        end = time.time() - start

        # extracting the output for later use and returning to old stdout
        IO_out = IO_out.getvalue()
        sys.stdout = old_stdout

        with open('output_file.txt', 'a') as out:
            out.write(f'{self.func.__name__} call {self.count} executed in {round(end, 4)} sec\n')
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
            out.write(f'\nOutput: \t {str(self.func(*args, **kwargs))}\n\n\n')  # second execution of function

            # print of the console out
            out.write(f'Console out: \t{IO_out}')

        rank[self.func.__name__] = round(end, 5)
        return func_out  # out of function should be returned!

    # display via class function
    @staticmethod
    def print_ranks():
        global rank
        print_ranks(rank)


# display via separate function
def print_ranks(rank_):
    print('PROGRAM | RANK | TIME ELAPSED')
    rank_table = dict(sorted(rank_.items(), key=lambda item: item[1]))
    for i, (k, v) in enumerate(rank_table.items()):
        print(f'{k}\t\t{i + 1} \t\t{v}')