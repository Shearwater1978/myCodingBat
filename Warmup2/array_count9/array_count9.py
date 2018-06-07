#!/usr/bin/env python
# -*- coding: utf-8 -*-


def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


# My little tests
def main():
    array_count9([1, 2, 9])
    array_count9([1, 9, 9])
    array_count9([1, 9, 9, 3, 9])


if __name__ == '__main__':
    main()

