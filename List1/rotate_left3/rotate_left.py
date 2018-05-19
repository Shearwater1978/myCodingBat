#!/usr/bin/env python
# -*- coding: utf-8 -*-


def rotate_left3(nums):
    nums.append(nums[0])
    nums.pop(0)
    return nums


# My little tests
def main():
    rotate_left3([1, 2, 3])
    rotate_left3([5, 11, 9])
    rotate_left3([7, 0, 0])


if __name__ == '__main__':
    main()

