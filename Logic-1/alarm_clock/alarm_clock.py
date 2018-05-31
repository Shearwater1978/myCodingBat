#!/usr/bin/env python
# -*- coding: utf-8 -*-


def alarm_clock(day, vacation):
    if day in list(range(1,6)):
        if vacation:
            return('10:00')
        else:
            return('7:00')
    elif day == 0 or day == 6:
        if vacation:
            return('off')
        else:
            return('10:00')


# My little tests
def main():
    alarm_clock(1, False)
    alarm_clock(5, False)
    alarm_clock(0, False)
    alarm_clock(6, False)
    alarm_clock(0, True)
    alarm_clock(6, True)


if __name__ == '__main__':
    main()

