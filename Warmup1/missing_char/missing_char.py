#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def missing_char(str, n):
    return str.replace(str[n], '')


# My little tests
def main():
    missing_char('kitten', 1)
    missing_char('kitten', 0)
    missing_char('kitten', 4)


if __name__ == '__main__':
    main()
