#!/usr/bin/env python2

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) < 2:
        return array  # empty or single-element array, don't do anything
    # set pivot to last element
    pivot_index = len(array)-1
    pivot = array[pivot_index]
    iut = 0  # index under test
    # work through elements left of pivot
    while iut < pivot_index:
        if array[iut] > pivot:
            temp = array[iut]
            array[iut] = array[pivot_index-1]
            pivot_index -= 1
            array[pivot_index] = pivot
            array[pivot_index+1] = temp
        else:
            # element finished, go to next one
            iut += 1
    # recursive sort for remaining halves
    array = quicksort(array[:pivot_index]) + [pivot] + quicksort(array[pivot_index+1:])
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
