import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4
import task3

@decorator_4
def func(a, b):
    """
    This function does something useful
    :param a: description
    :param b: description
    """
    result = 0
    n = randomrandint(10, 751)
    for i in range(n):
        result += (i ** 2)
    return 'output of func'

@decorator_4
def funk(n=2, m=5):
    """
    This function does something useful
    :param n: description
    :param m: description
    """
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    return 'output of funk'

if __name__ == "__main__":
    func()
    funk(2, 4)
    func()
    funk(10, 30)
    func()
    print('PROGRAM | RANK | TIME ELAPSED')
    dict(sorted(task3.rank.items(), key=lambda item: item[1]))
    for i, (k, v) in enumerate(task3.rank.items()):
        print(f'{k}\t\t{i+1} \t\t{round(v, 6)}')
