#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def make_tags(tag, word):
    return ("<{tag}>{word}</{tag}>".format(tag=tag, word=word))


# My little tests
def main():
    make_tags('i', 'Yay')
    make_tags('i', 'Hello')
    make_tags('cite', 'Yay')


if __name__ == '__main__':
    main()
