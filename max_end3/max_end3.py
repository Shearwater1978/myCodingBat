#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_end3(nums):
    if (nums[0] < nums[-1]):
        mav_val = nums[-1]
    elif (nums[0] > nums[-1]):
        mav_val = nums[0]
    else:
        mav_val = nums[0]
    for count, num in enumerate(nums):
        nums[count] = mav_val
    return nums

# My little test calls
def main():
    max_end3([1, 2, 3])
    max_end3([11, 5, 9])
    max_end3([2, 11, 3])
    max_end3([11, 3, 3])
    max_end3([3, 11, 11])
    max_end3([2, 2, 2])
    max_end3([2, 11, 2])
    max_end3([0, 0, 1])


if __name__ == '__main__':
    main()
