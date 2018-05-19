#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum2(nums):
    if (len(nums) < 2 and len(nums) > 0):
        summ = int(str(nums[0]))
    elif len(nums) == 0:
        summ = int(0)
    else:
        summ = int(nums[0] + nums[1])
    # This string need for visual control for output and exclude from code-areas for auto tests
    print(f"Array: {nums} Summ: {summ}")
    return summ


# My little tests
def main():
    sum2([1, 2, 3])
    sum2([1, 1])
    sum2([1, 1, 1, 1])


if __name__ == '__main__':
    main()
