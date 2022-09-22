import random
import time
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4
import task3
import task4

# RV imports
import numpy as np
from RV_stuff import RV_decorator_1
from task3 import print_ranks


@decorator_4
def func(a, b):
    """
    This function does something useful
    :param a: description
    :param b: description
    """
    print(f"example print from func")
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
    print(f"example print from funk")
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
    # print(max(n, m))   returns error !
    max_val = float('-inf')
    res = [pow(i, 2) for i in range(100000)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val


@RV_decorator_1
def RV_funh(n=2, m=5):
    """
    Function returns n highest nums from m random values. in case n > m, returns all random numbers
    :param n: num of the highest values to return
    :param m: count of randomly generated values from 1 - 1000
    :return: n highest values
    """
    res = np.random.randint(1, 1000, m)
    print(f'Generated arr: {res}')
    if n >= m:
        return res

    return sorted(res, reverse=True)[:n]


def RV_funh_copy(n=2, m=5):
    """
    Function returns n highest nums from m random values. in case n > m, returns all random numbers
    :param n: num of the highest values to return
    :param m: count of randomly generated values from 1 - 1000
    :return: n highest values
    """
    res = np.random.randint(1, 1000, m)
    print(f'Generated arr: {res}')
    if n >= m:
        return res

    return sorted(res, reverse=True)[:n]

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


# func for decorator 4 test
def div(a=2, b=2):
    return a/b


if __name__ == "__main__":
    func(4, 5)
    print(funk(3, 1))
    funk(3, 3)
    print(funh(8, m=6))  # returns None with decorator_1!
    funk(3, 3)
    fund(n=1, m=8)

    # # decorator_3
    # print('PROGRAM | RANK | TIME ELAPSED')
    # rank_table = dict(sorted(task3.rank.items(), key=lambda item: item[1]))
    # for i, (k, v) in enumerate(rank_table.items()):
    #     print(f'{k}\t\t{i + 1} \t\t{v}')
    #decorator_4
    #print('PROGRAM | RANK | TIME ELAPSED')
    #rank_table = dict(sorted(task4.rank.items(), key=lambda item: item[1]))
    #for i, (k, v) in enumerate(rank_table.items()):
        #print(f'{k}\t\t{i + 1} \t\t{v}')

    # RV examples
    print(f'RV_func out: {RV_funh(3, 20)}')  # example of correct decorator and function

    # example of alternative decorator assignment
    RV_funh_copy_1 = RV_decorator_1(RV_funh_copy)
    RV_funh_copy_1(3, 20)

    # example of rank displays
    RV_funh_copy_3 = decorator_3(RV_funh_copy)
    RV_funh_copy_3(3, 20)
    print(f'\nprint via class func')
    decorator_3.print_ranks()
    print(f'\nprint via separate func')
    print_ranks(task3.rank)

    # test of decorator 4
    decorator_4(div)(2, 0)
