#!/usr/bin/env python
# -*- coding: utf-8 -*-


def make_ends(nums):
    a = []
    if (len(nums) >= 1):
        a = [nums[0], nums[-1]]
    return a


# My little tests
def main():
    make_ends([1, 2, 3])
    make_ends([1, 2, 3, 4])
    make_ends([7, 4, 6, 2])


if __name__ == '__main__':
    main()
