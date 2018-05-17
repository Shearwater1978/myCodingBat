#!/usr/bin/env python
# -*- coding: utf-8 -*-


def first_last6(nums):
    if (nums[0] == 6 or nums[-1] == 6) :
        return True
    else:
        return False


def main():
    print(first_last6([2, 3, 6, 12 ]))


if __name__ == '__main__':
    main()
