# -*- coding: utf-8 -*-


def array123(nums):
    res = False
    for count, num in enumerate(nums):
        if num == 1 and count + 2 < len(nums):
            if nums[count+1] == 2 and nums[count+2] == 3:
                res = True
    return res

# My little tests
def main():
    array123([1, 1, 2, 3, 1])
    array123([1, 1, 2, 4, 1])
    array123([1, 1, 2, 1, 2, 3])


if __name__ == '__main__':
    main()

