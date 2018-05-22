#!/usr/bin/env python
# -*- coding: utf-8 -*-


def diff21(n):
    if n >= 21:
        return((n - 21) * 2)
    else:
        return(21 - n)


# My little tests
def main():
    diff21(19)
    diff21(10)
    diff21(21)
    diff21(221)


if __name__ == '__main__':
    main()
