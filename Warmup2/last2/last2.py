#!/usr/bin/env python
# -*- coding: utf-8 -*-


def last2(str):
    if len(str) < 2:
        return 0
    else:
        last2symbol = str[len(str)-2:]
        count = 0
    for i in range(len(str)-2):
        if str[i:i+2] == last2symbol:
            count += 1
    return count


# My little tests
def main():
    last2('hixxhi')
    last2('xaxxaxaxx')
    last2('axxxaaxx')


if __name__ == '__main__':
    main()

