#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sleep_in(weekday, vacation):
    if (weekday == False or vacation == True):
        res = True
    else:
        res = False
    return(res)


# My little tests
def main():
    sleep_in(False, False)
    sleep_in(True, False)
    sleep_in(False, True)


if __name__ == '__main__':
    main()
