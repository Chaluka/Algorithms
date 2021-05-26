"""
Testing file for Question 2 of Interview Prac 2
"""
__author__ = "Chaluka Salgado"
__date__ = "24/03/2021"

import unittest
import random
from quick_sort import partition, quick_sort


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        """ The 'setUp' method is a frequently used method in unittest, and is called BEFORE every test case is run.
        This is useful when you want to create certain conditions before running a series of tests, without having to
        repeat code within those tests. Used in conjuction with tearDown to help ensure the test is isolated from
        the performance of other tests.

        Here it's just creating storage for any potential raised errors in the tests."""
        self.verificationErrors = []

    def tearDown(self):
        """ The 'tearDown' is another frequently used method in unittest, and is called AFTER every test case is run.
        This is useful when you want to delete created instances or do other required tasks,
        without having to repeat code within those tests. Used in conjuction with setUp to help
        ensure the test is isolated from the performance of other tests.

        Here it's just printing off the errors that may have been stored in our list of errors, as well as the total number
        of errors.
        """
        for item in self.verificationErrors:
            print(item)

        print("Number of Errors = " + str(len(self.verificationErrors)))

    random.seed(10)

    def test_partition(self):

        def check_index(lst, ind):
            for cur in range(len(lst)):
                if cur < ind and lst[cur] > lst[ind]:
                    return False
                if cur > ind and lst[cur] <= lst[ind]:
                    return False
            return True

        for i in range(10):
            randomlist = random.sample(range(100, 1000), 50)
            index = partition(randomlist, 0, len(randomlist) - 1)

            # Test if partition function correctly works
            try:
                self.assertTrue(check_index(randomlist, index), msg="partition function doesn't work properly")
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_quick_sort(self):

        def is_sorted(lst):
            for ind in range(1, len(lst)):
                if lst[ind - 1] > lst[ind]:
                    return False
            return True

        for itr in range(10):
            randomlist = [random.randrange(100) for i in range(100)]
            quick_sort(randomlist)

            # Test if quick sort function correctly works
            try:
                self.assertTrue(is_sorted(randomlist), msg="quick sort function doesn't work properly")
            except AssertionError as e:
                self.verificationErrors.append(str(e))


if __name__ == '__main__':
    unittest.main()
