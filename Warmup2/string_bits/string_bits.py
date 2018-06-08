#!/usr/bin/env python
# -*- coding: utf-8 -*-


def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


# My little tests
def main():
    string_bits('Hello')
    string_bits('Hi')
    string_bits('Heeololeo')


if __name__ == '__main__':
    main()

