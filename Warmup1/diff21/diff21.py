#!/usr/bin/env python
# -*- coding: utf-8 -*-

# My solution
def diff21(n):
    if n >= 21:
        return((n - 21) * 2)
    else:
        return(21 - n)

# Solution from codingbat.com
#def diff21(n):
#  if n <= 21:
#    return 21 - n
#  else:
#    return (n - 21) * 2

# My little tests
def main():
    diff21(19)
    diff21(10)
    diff21(21)
    diff21(221)


if __name__ == '__main__':
    main()
