import random
import time
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4
import task3
import task4


@decorator_4
def func(a, b):
    """
    This function does something useful
    :param a: description
    :param b: description
    """
    result = 0
    for i in range(1000000):
        result += (i ** 2)
    return result


@decorator_4
def funk(n=2, m=5):
    """
    This function does something useful
    :param n: description
    :param m: description
    """
    max_val = float('-inf')
    res = [pow(i, 2) for i in range(1000000)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val

@decorator_4
def funh(n=2, m=5):
    """
    This function does something useful
    :param n: description
    :param m: description
    """
    max_val = float('-inf')
    res = [pow(i, 2) for i in range(100000)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val

@decorator_4
def fund(n=2, m=5):
    """
    This function does something useful
    :param n: description
    :param m: description
    """
    max_val = float('-inf')
    res = [pow(i, 2) for i in range(1000000)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val


if __name__ == "__main__":
    func(4, 5)
    funk(3, 1)
    funh(8, m=6)
    fund(n=1, m=8)
    # # decorator_3
    # print('PROGRAM | RANK | TIME ELAPSED')
    # rank_table = dict(sorted(task3.rank.items(), key=lambda item: item[1]))
    # for i, (k, v) in enumerate(rank_table.items()):
    #     print(f'{k}\t\t{i + 1} \t\t{v}')
    #decorator_4
    print('PROGRAM | RANK | TIME ELAPSED')
    rank_table = dict(sorted(task4.rank.items(), key=lambda item: item[1]))
    for i, (k, v) in enumerate(rank_table.items()):
        print(f'{k}\t\t{i + 1} \t\t{v}')
