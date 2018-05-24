#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def first_two(str):
    return(str[0:2:1])

# My little tests
def main():
    first_two('Hello')
    first_two('abcdefg')
    first_two('ab')

if __name__ == '__main__':
    main()
