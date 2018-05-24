#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def first_half(str):
    if len(str) % 2 == 0:
        return(str[0:int(len(str) / 2):1])

# My little tests
def main():
    first_half('WooHoo')
    first_half('HelloThere')
    first_half('abcdef')
    first_half('abcdefa')


if __name__ == '__main__':
    main()
