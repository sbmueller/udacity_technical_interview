#!/usr/bin/env python2

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    index = 0
    size = len(input_array)
    while True:
        size = len(input_array)
        # check middle value
        if input_array[size//2] == value:
            return index
        # if only one element that not equals value, return -1
        elif size == 1:
            return -1
        # continue search on right half
        elif input_array[size//2] < value:
            input_array = input_array[size//2+1:]
            index += size//2+1
        # continue search on left half
        elif input_array[size//2] > value:
            input_array = input_array[:size//2]

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
