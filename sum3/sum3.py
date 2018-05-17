#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum3(nums):
    summ = 0
    for item in nums:
        summ = summ + item
    return (summ)


def main():
    print(sum3([5, 11, 2]))


if __name__ == '__main__':
    main()
