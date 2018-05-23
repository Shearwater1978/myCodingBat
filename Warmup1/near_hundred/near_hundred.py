#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def near_hundred(n):
  return (abs(n-100) <= 10 or abs(n-200) <= 10)


# Solution from codingbat.com
#def near_hundred(n):
#  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# My little tests
def main():
    near_hundred(93)
    near_hundred(90)
    near_hundred(89)

if __name__ == '__main__':
    main()
