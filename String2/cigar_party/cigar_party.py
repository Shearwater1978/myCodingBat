#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cigar_party(cigars, is_weekend):
    print(cigars, is_weekend)
    if (cigars >= 40 and cigars <= 60):
        print("1 if",  cigars, is_weekend, True)
        return True
    elif (cigars < 40 or cigars > 60) and is_weekend == True:
        print("2 if",  cigars, is_weekend, True)
        return True
    else:
        print("else", cigars, is_weekend, False)
        return False


# My little tests
def main():
#    cigar_party(30, False)
#    cigar_party(50, False)
    cigar_party(70, True)
    cigar_party(70, False)


if __name__ == '__main__':
    main()

