#!/usr/bin/env python
# -*- coding: utf-8 -*-


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return (0)
    elif (you in list(range(8, 11)) or date in list(range(8, 11))):
        return (2)
    else:
        return (1)


# My little tests
def main():
    date_fashion(5, 10)
    date_fashion(9, 2)
    date_fashion(5, 5)


if __name__ == '__main__':
    main()

