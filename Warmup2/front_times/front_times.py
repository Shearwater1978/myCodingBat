#!/usr/bin/env python
# -*- coding: utf-8 -*-


def front_times(str, n):
    if len(str) > 3:
       if len(str[0:n]) < 3:
           return(str[0:n+1] * n)
       else:
           return(str[0:n] * n)
    else:
       return(str[0:n] * n)


# My little tests
def main():
    print(front_times('Chocolate', 2))
    print(front_times('Chocolate', 3))
    print(front_times('Abc', 3))
    print(front_times('Ab', 4))
    print(front_times('A', 4))
    print(front_times('', 4))


if __name__ == '__main__':
    main()

