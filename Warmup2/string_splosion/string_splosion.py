#!/usr/bin/env python
# -*- coding: utf-8 -*-


def string_splosion(str):
    iter_count = int(len(str))
    count = 0
    while count < iter_count:
        count += 1
        str = str[0:iter_count - count] + str
    return(str)

# My little tests
def main():
    string_splosion('Code')
    string_splosion('abc')
    string_splosion('ab')


if __name__ == '__main__':
    main()

