#!/usr/bin/env python
# -*- coding: utf-8 -*-


def near_ten(num): 
    return not(2 < (num % 10) < 8)


# My little tests
def main():
    near_ten(12)
    near_ten(17)
    near_ten(19)


if __name__ == '__main__':
    main()

