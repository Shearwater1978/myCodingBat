#!/usr/bin/env python
# -*- coding: utf-8 -*-


def end_other(a, b):
    if len(a) > len(b):
        res = a[len(a)-len(b):len(a)].lower() == b.lower()
    elif len(a) < len(b):
        res = a.lower() == b[len(b)-len(a):len(b)].lower()
    else:
        return a.lower() == b.lower()


# My little tests
def main():
    end_other('Hiabc', 'abc')
    end_other('Hiabc', 'bc')
    end_other('Hiabcx', 'bc')
    end_other('Z', '12xz')


if __name__ == '__main__':
    main()
