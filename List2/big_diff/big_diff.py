#!/usr/bin/env python
# -*- coding: utf-8 -*-


def big_diff(nums):
    result = sorted(nums)[-1] - sorted(nums)[0]
    return result


# My little tests
def main():
    big_diff([10, 3, 5, 6])
    big_diff([7, 2, 10, 9])
    big_diff([2, 10, 7, 2])

if __name__ == '__main__':
    main()

