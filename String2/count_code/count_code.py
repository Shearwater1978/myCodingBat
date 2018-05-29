#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_code(str):
    split_on = count = 0
    while len(str) >= split_on + 4:
        if (str[split_on:split_on + 2] == 'co' and str[split_on + 3] == 'e'):
            count += 1
        split_on += 1
    return count

# My little tests
def main():
    count_code_new('codexxcode')
    count_code('aaacodebbb')
    count_code('codexxcode')
    count_code('cozexxcope')


if __name__ == '__main__':
    main()

