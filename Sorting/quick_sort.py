"""
        Quick Sort and Quick Select Implementations

        Quick  Sort : sort a list by recursively divide the list into perfect fractions using the partition
        function where a pivot is selected to identify the partition point.
"""

__author__ = "Chaluka Salgado"
__date__ = "24/03/2021"


def partition(input_lst, start_index, end_index):
    """
    Given a list of elements (of any primitive data type), this function partition the list into two halves based on the
    selected pivot. Here, first element is always selected as the pivot.
    :return: index of the chosen pivot
    :complexity: O(n) where n is the length of the list
    """
    # select first element in the list as the pivot
    pivot = input_lst[start_index]
    right_bad, left_bad = end_index, start_index + 1

    while left_bad <= right_bad:
        if input_lst[left_bad] > pivot >= input_lst[right_bad]:
            input_lst[left_bad], input_lst[right_bad] = input_lst[right_bad], input_lst[left_bad]

        if input_lst[left_bad] <= pivot:
            left_bad += 1
        if input_lst[right_bad] > pivot:
            right_bad -= 1

    input_lst[right_bad], input_lst[start_index] = input_lst[start_index], input_lst[right_bad]

    return right_bad


def quick_sort(input_lst):
    """
    Given a list is sorted in ascending order
    Complexity: Best case: O(nlogn) and Worst case: O(n^2) where n is the number of elements
    """

    start_index = 0
    end_index = len(input_lst) - 1

    quick_sort_aux(input_lst, start_index, end_index)


def quick_sort_aux(input_lst, start_index, end_index):
    """
        Base on the chosen pivot's index, this function will recursively call quick sort
        on two partitions (i.e., input_lst[start_index : index-1] and input_lst[index+1 : end_index] )
    """
    # k = len(input_lst[start_index:end_index+1]) // 2 - 1

    if start_index < end_index:
        index = partition(input_lst, start_index, end_index)
        quick_sort_aux(input_lst, start_index, index - 1)
        quick_sort_aux(input_lst, index + 1, end_index)


def quick_select(input_lst, start_index, end_index, index):
    """
    Using quick select we chose the pivot in the given index.
    (i.e., if we want the median of the input_list[start_idex:end_index] we pass index = n//2)
    This
    :return:
    """
    if index > 0 and start_index < end_index:

        cur_index = partition(input_lst, start_index, end_index)
        # print(index, cur_index, input_lst[start_index:end_index+1])
        if index == cur_index:
            return index
        elif index < cur_index:
            return quick_select(input_lst, start_index, cur_index - 1, index)
        else:
            return quick_select(input_lst, cur_index + 1, end_index, index)


if __name__ == "__main__":
    l = [75, 27, 78, 15, 96, 7, 62, 12]
    quick_sort(l)
    print(l)
