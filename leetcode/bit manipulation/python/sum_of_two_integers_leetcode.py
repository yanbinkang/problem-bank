"""
https://leetcode.com/problems/sum-of-two-integers/#/description

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

https://discuss.leetcode.com/topic/49831/one-positive-and-one-negative-case-is-successful-for-python-a-b-1-1-is-ok-by-rules/3

https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
"""
import ctypes
def get_sum(a, b):
    total = 0
    carry = ctypes.c_int32(b)

    while carry.value != 0:
        total = a ^ carry.value
        carry = ctypes.c_int32(a & carry.value)
        carry.value = carry.value << 1
        a = total

    return total

def get_sum_TLE(a, b):
    if a == 0: return b

    if b == 0: return a

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

if __name__ == '__main__':
    print get_sum_TLE(1, 2)
    print get_sum_TLE(2, 3)
    print('\n')
    print get_sum(1, 2)
    print get_sum(2, 3)

