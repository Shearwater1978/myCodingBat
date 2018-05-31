#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sorta_sum(a, b):
    for item in list(range(10,20)):
        if a + b == item:
            return 20
    else:
        return a + b


# My little tests
def main():
    sorta_sum(3, 4)
    sorta_sum(9, 4)
    sorta_sum(10, 11)


if __name__ == '__main__':
    main()

