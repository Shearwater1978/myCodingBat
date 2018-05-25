#!/usr/bin/env python
# -*- coding: utf-8 -*-


def double_char(str):
    str_o = ''
    for item in list(str):
        str_o = str_o + (item * 2 )
    return str_o


# My little tests
def main():
    double_char('The')
    double_char('AAbb')
    double_char('Hi-There')


if __name__ == '__main__':
    main()

