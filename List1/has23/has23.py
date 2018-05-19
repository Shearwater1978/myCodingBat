#!/usr/bin/env python
# -*- coding: utf-8 -*-


def has23(nums):
    result = False
    if (len(nums) != 2):
        result = False
    if len(nums) == 2:
        for item in nums:
            if (item == 2 or item == 3):
                result = True
    print(f"Array: {nums} Result: {result}")
#    return result


# My little tests
def main():
    has23([2, 5])
    has23([4, 3])
    has23([4, 5])
    has23([4, 5, 6])
    has23([3])
    has23([])


if __name__ == '__main__':
    main()

