#!/usr/bin/env python
# -*- coding: utf-8 -*-

# My solution
def parrot_trouble(talking, hour):
    safe_hour = list(range(7,21,1))
    if safe_hour.count(hour):
        return False
    else:
        if talking:
            return True
        else:
            return False

        
# Solution from codingbat.com
#def parrot_trouble(talking, hour):
#  return (talking and (hour < 7 or hour > 20))

# My little tests
def main():
    parrot_trouble(True, 6)
    parrot_trouble(True, 7)
    parrot_trouble(False, 6)
    parrot_trouble(True, 20)


if __name__ == '__main__':
    main()
