#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def left2(str):
    return(str[2::1]+str[:2:1])


# My little tests
def main():
    left2('Hello')
    left2('java')
    left2('Hi')


if __name__ == '__main__':
    main()
