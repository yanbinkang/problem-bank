"""
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 => 2
[1,3,5,6], 2 => 1
[1,3,5,6], 7 => 4
[1,3,5,6], 0 => 0

note:

we're using hi = len(nums) because of the case of 1 element. Eg. searchInsert([1], 2). This makes sure initially lo=0 and hi=1.

When we're in the while loop mid becames 0 and we can safely jump into the first if statement which makes the invariant false.

But when we use hi = len(nums) - 1, lo=0 and hi=0 and the invariant is already false which makes returning lo the wrong answer.
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) / 2

        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


"""
can we use this now because of the case of a single element test case? FIND OUT!

Edit 06/03/2018: I have tested this and we can indeed use it for single element test case. The trick is to use:
            while low <= high
    as the invariant. and also use:
            high = mid - 1
    for the else case.

    This way, when we have a single element low = high = 0
    and the variant won't be false. Hence with Eg. searchInsert([1], 2) we can safely jump into the first if statement which will make the invariant false.
"""
def searchInsert_1(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) / 2

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

if __name__ == '__main__':
    print searchInsert([1,3,5,6], 5)
    print searchInsert([1,3,5,6], 2)
    print searchInsert([1,3,5,6], 7)
    print searchInsert([1,3,5,6], 0)
    print searchInsert([1], 2)
    print('\n')
    print searchInsert_1([1], 2)

