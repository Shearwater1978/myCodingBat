#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def not_string(str):
    if str[:3] == 'not':
        pass
    else:
       str = 'not ' + str
    return(str)


# My little tests
def main():
    not_string('candy')
    not_string('x')
    not_string('not bad')


if __name__ == '__main__':
    main()
