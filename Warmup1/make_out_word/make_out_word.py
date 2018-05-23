#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def make_out_word(out, word):
    return(out[:2]+word+out[2:])


# Solution by codingbat.com
#def makes10(a, b):
#  return (a == 10 or b == 10 or a+b == 10)


# My little tests
def main():
    make_out_word('<<>>', 'Yay')
    make_out_word('<<>>', 'WooHoo')
    make_out_word('[[]]', 'word')


if __name__ == '__main__':
    main()
