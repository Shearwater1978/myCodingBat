#!/usr/bin/env python
# -*- coding: utf-8 -*-


# My solution
def pos_neg(a, b, negative, exept):
    if (a < 0 or b < 0) and ( a > 0 or b > 0) and negative == False:
        ret = True
    elif (a < 0 and b < 0) and negative == True:
        ret = True
    else:
        ret = False
    if ret != exept:
        print(f"Элемент а: {a}, Элемент б: {b}, Условие: {negative}, Итог: {ret} Ожидание: {exept}")
    return(ret)

# Solution from codingbat.com
#def pos_neg(a, b, negative):
#  if negative:
#    return (a < 0 and b < 0)
#  else:
#    return ((a < 0 and b > 0) or (a > 0 and b < 0))


# My little tests
def main():
    pos_neg(1, -1, False, True)
    pos_neg(-1, 1, False, True)
    pos_neg(-4, -5, True, True)
    pos_neg(-4, -5, False, False)
    pos_neg(-4, 5, False, True)
    pos_neg(-4, 5, True, False)
    pos_neg(1, 1, False, False)
    pos_neg(-1, -1, False, False)
    pos_neg(1, -1, True, False)
    pos_neg(-1, 1, True, False)
    pos_neg(1, 1, True, False)
    pos_neg(-1, -1, True, True)
    pos_neg(5, -5, False, True)
    pos_neg(-6, 6, False, True)
    pos_neg(-5, -6, False, False)
    pos_neg(-2, -1, False, False)
    pos_neg(1, 2, False, False)
    pos_neg(-5, 6, True, False)
    pos_neg(-5, -5, True, True)


if __name__ == '__main__':
    main()
