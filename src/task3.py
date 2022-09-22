import time
import inspect
import contextlib, io

rank = {}
class decorator_3:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        global rank
        self.count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            output = self.func(args, kwargs)
        end = time.time() - start
        with open('output_file.txt', 'a') as out:
            out.write(f'{self.func.__name__} call {self.count} executed in {round(end, 4)} sec\n')
            out.write(f'Name: \t {self.func.__name__}\n')
            out.write(f'Type: \t {type(self.func)}\n')
            out.write(f'Sign: \t {str(inspect.signature(self.func))}\n')
            out.write(f'Args: \t positional {args}\n')
            out.write(f'      \t kwarg {kwargs}\n\n')
            out.write(f'Doc: \t {self.func.__doc__}\n')
            lines = inspect.getsourcelines(self.func)
            out.write('Source: \t')
            for l in lines[0]:
                out.write('\t' + str(l))
            out.write(f'\nOutput: \t {str(output)}\n\n\n')
        rank[self.func.__name__] = round(end, 5)
        return output
