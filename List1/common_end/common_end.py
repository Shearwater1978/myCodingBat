#!/usr/bin/env python
# -*- coding: utf-8 -*-


def common_end(a, b):
    return (a[0] == b[0] or a[-1] == b[-1])


def main():
    # Test call function
    print(common_end([1, 2, 3], [7, 3]))


if __name__ == '__main__':
    main()
