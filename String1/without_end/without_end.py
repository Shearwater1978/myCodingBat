#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def without_end(str):
    res =''
    if len(str) >= 4:
        res = str[1:len(str)-1:1]
    return(res)

# My little tests
def main():
    without_end('Hello')
    without_end('java')
    without_end('coding')


if __name__ == '__main__':
    main()
