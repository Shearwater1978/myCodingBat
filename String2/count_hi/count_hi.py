#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_hi(str):
    return(str.count('hi'))



# My little tests
def main():
    count_hi('abc hi ho')
    count_hi('ABChi hi')
    count_hi('hihi')


if __name__ == '__main__':
    main()

