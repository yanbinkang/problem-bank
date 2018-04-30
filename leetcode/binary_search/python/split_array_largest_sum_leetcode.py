"""
https://leetcode.com/problems/split-array-largest-sum/#/description

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

    1. 1 <= n <= 1000
    2. 1 <= m <= min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
def split_array(nums, m):
    imax, isum = 0, 0

    for num in nums:
        imax = max(imax, num)
        isum += num

    if m == 1: return isum

    l, r  = imax, isum

    while l <= r:
        mid = (l + r) / 2

        if valid(mid, nums, m):
            r = mid - 1
        else:
            l = mid + 1

    return l

def valid(target, nums, m):
    count, total = 1, 0

    for num in nums:
        total += num

        if total > target:
            total = num
            count += 1

            if count > m:
                return False

    return True

if __name__ == '__main__':
    print split_array([7, 2, 5, 10, 8], 2)
