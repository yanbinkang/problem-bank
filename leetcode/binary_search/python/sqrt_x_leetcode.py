"""
https://leetcode.com/problems/sqrtx/#/description

Implement int sqrt(int x).

Compute and return the square root of x.

Explanation: The square root of x is a number that when multplied by itself will result in x.

Example: square root of 9 is 3 because 3 * 3 == 9.

We can use binary search to compute this because we're looking for a number between 0.0 and x. Remember all the numbers between 0.0 and x are sorted!

low = 0.0
high = x

Do normal binary search and find mid. When doing the normal binary search we have to compute target. target = pow(mid, 2) or mid * mid.

If target is greater than x then mid cannot give us the answer so set high = mid and search lower half of range.

If target is less than x then mid cannot give is the answer so set low = mid, search higher half of range.

All the while we simply want a number that when multiplied by itself will give us x. Remember, target gives us mid * mid, so if we find that the difference between target and x is really really small (meaning target is very close to x), we have found our answer. How small? We use 0.000001. So we use diff to compute this difference and when diff <= 0.000001 we return mid.

(OlogN) time; O(1) space
"""
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0 or x == 1: return x

    low, high = 0.0, x

    while low <= high:
        mid = (low + high) / 2
        target = pow(mid, 2) # or mid * mid

        diff = abs(x - target)

        if diff <= 0.000001:
            return mid
        elif target > x:
            high = mid # search lower half
        else:
            low = mid # search upper half

if __name__ == '__main__':
    print mySqrt(5)
    print mySqrt(9)
    print mySqrt(25)
    print mySqrt(8)
