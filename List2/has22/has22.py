#!/usr/bin/env python
# -*- coding: utf-8 -*-


def has22(nums):
    res = False
    for i, item in enumerate(nums):
        if item != 2:
            continue
        elif item == 2 and i < len(nums)-1:
            if nums[i+1] == 2:
                res = True
    return(res)


# My little tests
def main():
    has22([1, 2, 2])
    has22([1, 2, 1, 2])
    has22([2, 1, 2])
    has22([2, 2, 1, 2])
    has22([1, 3, 2])
    has22([1, 3, 2, 2])
    has22([2, 3, 2, 2])
    has22([4, 2, 4, 2, 2, 5])
    has22([1, 2])
    has22([2, 2])
    has22([2])
    has22([])
    has22([3, 3, 2, 2])
    has22([5, 2, 5, 2])


if __name__ == '__main__':
    main()
