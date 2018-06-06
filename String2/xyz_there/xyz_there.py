#!/usr/bin/env python
# -*- coding: utf-8 -*-


def xyz_there(str):
    print(str)
    if str.find('xyz') and len(str) > 0:
        if str[str.find('xyz')-1] != '.':
            return True
        else:
            return False
    else:
        return False
    
#        print(str, True)
#    elif (str.find('xyz') > 0) and (str.find('.', 0, str.find('xyz')) != str.find('xyz')) != True:
#        return True
#        print(str, True)
#    else:
#        return False
#        print(str, False)


# My little tests
def main():
    print(xyz_there('abcxyz'))
    print(xyz_there('abc.xyz'))
    print(xyz_there('xyz.abc'))


if __name__ == '__main__':
    main()
