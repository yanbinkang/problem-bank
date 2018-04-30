"""
https://leetcode.com/problems/first-bad-version/#/description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.


Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Time complexity: LogN
Space complexity: O(1)

ref: https://leetcode.com/articles/first-bad-version/

It is not difficult to see that this could be solved using a classic algorithm - Binary search. Let us see how the search space could be halved each time below.

Scenario #1: isBadVersion(mid) => false

 1 2 3 4 5 6 7 8 9
 G G G G G G B B B       G = Good, B = Bad
 |       |       |
left    mid    right

Let us look at the first scenario above where isBadVersion(mid) => false. We know that all versions preceding and including mid are all good. So we set left = mid + 1 to indicate that the new search space is the interval [mid + 1, right](inclusive).

Scenario #2: isBadVersion(mid) => true

 1 2 3 4 5 6 7 8 9
 G G G B B B B B B       G = Good, B = Bad
 |       |       |
left    mid    right

The only scenario left is where isBadVersion(mid) => true. This tells us that mid may or may not be the first bad version, but we can tell for sure that all versions after mid can be discarded. Therefore we set right = mid as the new search space of interval [left,mid] (inclusive).

In our case, we indicate left and right as the boundary of our search space (both inclusive). This is why we initialize left = 1 and right = n. How about the terminating condition? We could guess that left and right eventually both meet and it must be the first bad version, but how could you tell for sure?

Here is a helpful tip to quickly prove the correctness of your binary search algorithm during an interview. We just need to test an input of size 2. Check if it reduces the search space to a single element (which must be the answer) for both of the scenarios above. If not, your algorithm will never terminate.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            # G G G B B B B B B
            if isBadVersion(mid):
                right = mid # mid could be the first bad version
            else: # G G G G G B B B
                left = mid + 1 # all versions before and including mid are good. move forward

        return left

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n

        while first < last:
            mid = (first + last) // 2

            # G G G G G B B B
            if not isBadVersion(mid):
                first = mid + 1
            else: # G G G B B B B B B
                last = mid

        return first

