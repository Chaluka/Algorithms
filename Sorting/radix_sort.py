"""
 Count Sort and Radix sort

 Given a list of integers are sorted by running counting sort on each digit.
"""

__author__ = "Chaluka Salgado"
__date__ = "18/10/2020"

import math

DOMAIN_SIZE = 10


def count_sort(input, index=0):
    """
    :return: sorted list based nth digit

    :complexity: best/worst case : O(N+U) where N is number of items and U is size of the domain
    """
    # create count array
    count_array = [0 for i in range(DOMAIN_SIZE)]
    for i in range(len(input)):
        count_array[get_digit(input[i], index)] += 1

    # create position array
    pos_array = [0 for i in range(DOMAIN_SIZE)]
    for i in range(1, DOMAIN_SIZE):
        pos_array[i] = pos_array[i - 1] + count_array[i - 1]

    # create sorted list using position array
    out_list = [None for i in range(len(input))]
    for i in range(len(input)):
        out_list[pos_array[get_digit(input[i], index)]] = input[i]
        pos_array[get_digit(input[i], index)] += 1

    return out_list


def radix_sort(input):
    """
        Return a sorted
    :return:
    :complexity:    best/worst case : O((N+U)k) where N is number of items,
                    k is the maximum number of digits in any item and U is size of the domain.
    """
    input_lst = input[::]
    max_digits = get_num_digits(max(input_lst))
    for i in range(max_digits):
        input_lst = count_sort(input_lst, i)

    return input_lst


def get_num_digits(num):
    """
    Given a list of integers, this function returns the maximum # of digits in any of the integers
    :param input_list:
    :return:
    """
    return math.floor(math.log10(num) + 1)


def get_digit(number, n):
    return number // int(math.pow(10, n)) % 10


if __name__ == "__main__":
    lst = [11, 1, 3, 1, 4, 10, 5, 7, 10]
    lst1 = radix_sort(lst)
    print(lst1)
