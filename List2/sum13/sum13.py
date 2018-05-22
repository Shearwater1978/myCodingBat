#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum13(nums):
    summ = 0
    count = 0
    if len(nums) == 0:
        summ = 0
    else:
        for i in range(len(nums)):
            if (nums[i] == 13 and count == 0):
                count = 1
            elif (count == 1):
                count = 0
            else:
                summ = summ + nums[i]
    return summ


# My little tests
def main():
    sum13([1, 2, 2, 1])
    sum13([1, 1])
    sum13([1, 2, 2, 1, 13])


if __name__ == '__main__':
    main()
