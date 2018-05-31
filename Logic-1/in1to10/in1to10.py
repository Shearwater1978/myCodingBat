#!/usr/bin/env python
# -*- coding: utf-8 -*-


def in1to10(n, outside_mode):
    if not outside_mode:
        if n in list(range(1, 11)):
            return True
        else:
            return False
    elif outside_mode:
        if n <= 1 or n >=10:
            return True
        else:
            return False


# My little tests
def main():
    in1to10(5, False)
    in1to10(11, False)
    in1to10(11, True)


if __name__ == '__main__':
    main()

