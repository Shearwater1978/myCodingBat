#!/usr/bin/env python
# -*- coding: utf-8 -*-


def array_front9(nums):
    try:
        if nums.index(9) in list(range(0,3,1)):
            res = True
        else:
            res = False
    except:
        res = False
    return res


# My little tests
def main():
    array_front9([1, 2, 9, 3, 4])
    array_front9([1, 2, 3, 4, 9])
    array_front9([1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()

