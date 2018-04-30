"""
https://leetcode.com/problems/valid-perfect-square/description/

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False

ref:https://discuss.leetcode.com/topic/49372/java-three-solutions-1-3-5-sequence-binary-search-newton
"""
def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 1: return False
    lo, hi = 1, num

    while lo <= hi:
        mid = (lo + hi) / 2

        res = mid * mid

        if res > num:
            hi = mid - 1
        elif res < num:
            lo = mid + 1
        else:
            return True

    return False

if __name__ == '__main__':
    print isPerfectSquare(9) # True
    print isPerfectSquare(5) # False
    print isPerfectSquare(1) # True
    print isPerfectSquare(16) # True
