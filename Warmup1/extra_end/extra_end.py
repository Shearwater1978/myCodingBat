#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def extra_end(str):
    if len(str) >= 2:
       return(str[-2:] * 3)


# My little tests
def main():
    extra_end('Hello')
    extra_end('ab')
    extra_end('Hi')


if __name__ == '__main__':
    main()
