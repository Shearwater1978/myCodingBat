#!/usr/bin/env python
# -*- coding: utf-8 -*-

# My solution
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    return False


# Solution by codingbat.com
#def makes10(a, b):
#  return (a == 10 or b == 10 or a+b == 10)


# My little tests
def main():
    makes10(9, 10)
    makes10(9, 9)
    makes10(1, 9)


if __name__ == '__main__':
    main()
