#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def combo_string(a, b):
    if len(a) != len(b):
        if len(a) > len(b):
           return(b+a+b)
        else:
           return(a+b+a)


# My little tests
def main():
    combo_string('Hello', 'hi')
    combo_string('hi', 'Hello')
    combo_string('aaa', 'b')


if __name__ == '__main__':
    main()
