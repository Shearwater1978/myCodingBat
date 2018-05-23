#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def make_abba(a, b):
    return str(a + b + b + a)


# My little tests
def main():
    make_abba('Hi', 'Bye')
    make_abba('Yo', 'Alice')
    make_abba('What', 'Up')


if __name__ == '__main__':
    main()
