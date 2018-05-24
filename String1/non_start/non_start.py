#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def non_start(a, b):
    if len(a) >= 1 and len(b) >= 1:
        return(a[1::1]+b[1::1])


# My little tests
def main():
    non_start('Hello', 'There')
    non_start('java', 'code')
    non_start('shotl', 'java')
    non_start('ab', 'x')
    non_start('x', 'ac')
    non_start('a', 'x')


if __name__ == '__main__':
    main()
