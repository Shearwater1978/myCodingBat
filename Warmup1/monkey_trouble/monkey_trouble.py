#!/usr/bin/env python
# -*- coding: utf-8 -*-


def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile and (a_smile == True or a_smile == False):
        return(True)
    else:
        return(False)


# My little tests
def main():
    monkey_trouble(True, True)
    monkey_trouble(False, False)
    monkey_trouble(True, False)
    monkey_trouble(False, True)


if __name__ == '__main__':
    main()
