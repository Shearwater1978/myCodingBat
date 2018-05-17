#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def make_pi():
    a = str(math.pi)[0:4]
    b = []
    for count, item in enumerate(a):
        if count != 1:
            b.append(int(item))
    return b


# My little tests
def main():
    make_pi()


if __name__ == '__main__':
    main()

