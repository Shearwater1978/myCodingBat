#!/usr/bin/env python
# -*- coding: utf-8 -*-


def same_first_last(nums):
    if (len(nums) >= 1 and nums[0] == nums[-1]):
        return True
    else:
        return False


def main():
    print(same_first_last([1, 2, 3]))


if __name__ == '__main__':
    main()
    
