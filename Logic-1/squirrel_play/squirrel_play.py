#!/usr/bin/env python
# -*- coding: utf-8 -*-


def squirrel_play(temp, is_summer):
    if is_summer:
        if temp in list(range(60,101)):
            return True
        else:
            return False
    if is_summer != True:
        if temp in list(range(60,91)):
            return True
        else:
            return False

# My little tests
def main():
    squirrel_play(70, False)
    squirrel_play(95, False)
    squirrel_play(95, True)


if __name__ == '__main__':
    main()

