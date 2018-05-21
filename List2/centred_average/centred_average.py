#!/usr/bin/env python
# -*- coding: utf-8 -*-


def centered_average(nums):
    summ = 0
    result = 0
    if (len(nums) >= 3):
        nums_sort = sorted(nums)
        nums_sort.pop(0)
        nums_sort.pop(-1)
        for item in nums_sort:
            summ = summ + item
        result = int(summ / len(nums_sort))
    return result


# My little tests
def main():
    centered_average([1, 2, 3, 4, 100])
    centered_average([1, 1, 5, 5, 10, 8, 7])
    centered_average([-10, -4, -2, -4, -2, 0])
    centered_average([4, 0, 100])


if __name__ == '__main__':
    main()

