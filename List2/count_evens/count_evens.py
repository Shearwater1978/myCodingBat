#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_evens(nums):
    result = 0
    for item in nums:
        if (item % 2 == 0):
            result += 1
    return result


# My little tests
def main():
    count_evens([2, 1, 2, 3, 4])
    count_evens([2, 2, 0])
    count_evens([1, 3, 5])


if __name__ == '__main__':
    main()

