"""
https://leetcode.com/problems/minimum-size-subarray-sum/#/description

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2, 3, 1, 2, 4, 3] and s = 7,
the subarray [4, 3] has the minimal length under the problem constraint.

ref: https://discuss.leetcode.com/topic/18583/accepted-clean-java-o-n-solution-two-pointers

Algo:

Keep two pointers where right is ahead of left. Use right to calculate the cumulative total.

During each iteration while the cumulative total is greater than or equal to s, the length of that subarray will be equal to right - left. Now, we need to check if there exist a smaller array length which is also >= s. What to do?

Example: with subarray [2, 3, 1, 2] and total 8, left = 0 and right = 4. We need to check if sum of subarray [3, 1, 2] (a smaller subarray) will also be >= s. So, first subtract 2 from the previous total and move left pointer forward by 1. Keep doing this until you break out of while loop.

Go back to the outter while loop and repeat the process.
"""
def min_subarray_len(s, nums):
    if not nums or len(nums) == 0: return 0

    left, right, total, imin = 0, 0, 0, float('inf')

    while right < len(nums):
        total += nums[right]
        right += 1

        # reduce window
        while total >= s:
            imin = min(imin, right - left)
            total -= nums[left]
            left += 1

    return 0 if imin == float('inf') else imin

if __name__ == '__main__':
    print min_subarray_len(7, [2, 3, 1, 2, 4, 3])
