#!/usr/bin/env python2

"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        first = get_fib(position-2)
        second = get_fib(position-1)
        return first + second

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

