#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum67(nums):
    count = 0
    summ = 0
    for item in nums:
        if (count == 0 and item == 6) or (count == 1 and item != 7):
            count = 1
        elif count == 1 and item == 7:
            count = 0
        else:
            count = 0
            summ = summ + item
    return(summ)


# My little tests
def main():
    sum67([1, 2, 2])
    sum67([1, 2, 2, 6, 99, 99, 7])
    sum67([1, 1, 6, 7, 2])
    sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
    sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
    sum67([2, 7, 6, 2, 6, 7, 2, 7])
    sum67([2, 7, 6, 2, 6, 2, 7])


if __name__ == '__main__':
    main()
