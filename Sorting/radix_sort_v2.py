"""
    This implementation use linked list count array to do the counting sort

    Given a list of integers, count sort convert each integer into a given base and do the sorting.

"""

__author__ = "Chaluka Salgado"
__date__ = "18/10/2020"

import math
import random
import time
from typing import List, TypeVar


def count_sort(num_list: List[int], base: int, index: int):
    """
    this will sort the input list in ascending order. O(N+b) complexity
    :param num_list: a list of items
    :param base: base of the numbers
    :param index: index of the column that sorting focuses
    :return: sorted list of items
    """
    sorted_list = []
    count_list = [[] for _ in range(base)]

    # adding items to the counting array
    for number in num_list:
        count_list[get_nth_digit(number, base, index)].append(number)

    for list in count_list:
        for num in list:
            sorted_list.append(num)

    return sorted_list


def get_nth_digit(num: int, b: int, n: int):
    """
    this returns the nth digit of the given number in base b
    if we divide number by base n-1 times (i.e. we skip n-1 digits) and then getting the remainder of nth division
    gives you nth digit of the given number in base b
    :return:
    """
    return (num // b ** (n - 1)) % b


def get_number_of_digits(number: int, base: int):
    # count = 0
    # while number != 0:
    #     number = number // base
    #     count += 1

    return int((math.log2(number) // math.log2(base)) + 1)


def radix_sort(num_list: List, base: int):
    """
     Complexity (N+b)M to sort a given list
    """
    max_count = 0
    for num in num_list:
        count = get_number_of_digits(num, base)
        if count > max_count:
            max_count = count

    for index in range(1, max_count + 1):
        num_list = count_sort(num_list, base, index)

    return num_list


def time_radix_sort():
    test_data = [random.randint(1, (2 ** 64) - 1) for _ in range(100000)]
    base_list = [2, 4, 16, 32, 64, 128]
    time_list = []
    for base in base_list:
        start = time.time()
        radix_sort(test_data, base)
        end = time.time()
        time_list.append([base, (end - start)])
        print(base, "\t", end - start)

    return time_list
