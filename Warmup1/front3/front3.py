#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def front3(str):
    if len(str) <= 3:
       str = str * 3
    else:
       str = str[0:3] * 3
    print(str)
    return str


# My little tests
def main():
    front3('Java')
    front3('Chocolate')
    front3('abc')


if __name__ == '__main__':
    main()
