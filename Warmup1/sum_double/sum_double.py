#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum_double(a, b):
    if a != b:
        return(a+b)
    else:
       return((a+b) * 2)

#Solutuion from codingbat.com
#def sum_double(a, b):
#  sum = a + b
#  if a == b:
#    sum = sum * 2
#  return sum

# My little tests
def main():
    sum_double(1, 2)
    sum_double(3, 2)
    sum_double(2, 2)


if __name__ == '__main__':
    main()
