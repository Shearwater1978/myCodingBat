#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cat_dog(str):
    return(str.count('cat') == str.count('dog'))


# My little tests
def main():
    cat_dog('catdog')
    cat_dog('catcat')
    cat_dog('1cat1cadodog')


if __name__ == '__main__':
    main()
