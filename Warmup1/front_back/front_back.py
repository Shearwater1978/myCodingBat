#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def front_back(str):
    if len(str) >= 2:
        last = str[len(str)-1]
        str = str.replace(str[len(str)-1], str[0])
        str = str.replace(str[0], last, 1)
    return str


# My little tests
def main():
    front_back('code')
    front_back('a')
    front_back('ab')


if __name__ == '__main__':
    main()
