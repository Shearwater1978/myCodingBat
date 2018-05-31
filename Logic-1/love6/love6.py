#!/usr/bin/env python
# -*- coding: utf-8 -*-


def love6(a, b):
  if a == 6 or b == 6 or a+b == 6 or abs(a-b)==6:
      return True
  else:
      return False


# My little tests
def main():
    love6(6, 4)
    love6(4, 5)
    love6(1, 5)


if __name__ == '__main__':
    main()

