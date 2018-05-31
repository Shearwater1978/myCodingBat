#!/usr/bin/env python
# -*- coding: utf-8 -*-


def caught_speeding(speed, is_birthday):
    if is_birthday == False:
        if speed <= 60:
            return 0
        elif speed in list(range(61,81)):
            return 1
        else:
            return 2
    else:
        if speed <= 65:
            return 0
        elif speed in list(range(66,86)):
            return 1
        else:
            return 2


# My little tests
def main():
    caught_speeding(60, False)
    caught_speeding(65, False)
    caught_speeding(65, True)


if __name__ == '__main__':
    main()

