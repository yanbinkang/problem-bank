"""
https://leetcode.com/problems/max-consecutive-ones-ii

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4

Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

    - The input array will only contain 0 and 1.

    - The length of input array is a positive integer and will not exceed 10,000

Follow up:

What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


solution: https://discuss.leetcode.com/topic/75426/concise-o-n-solution-slight-modification-of-two-pointers-and-1-liner-solution-for-fun/5

O(n) time O(1) space
"""
def find_max_consecutive_ones(nums):
    nums.append(0)

    # [1, 0, 1, 1, 0, 0]
    # low1 = 0; low2 = 2; result = 1
    # low1 = 2; low2 = 5; result = 4
    # low1 = 5; low2 = 6; result = 3

    left, right = 0, 0
    result = 0

    for index, num in enumerate(nums):
        if num == 0:
            result = max(result, index - left)
            left = right
            right = index + 1

    return result

# https://discuss.leetcode.com/topic/75457/sliding-window-2-pointers-o-n-time-1-pass-o-1-space
def find_max_consecutive_ones_1(nums):
    l, mx, zeros = 0, 0, 0

    for i, num in enumerate(nums):
        if num == 0:
            zeros += 1

        # we have more than 1 zero. need to resize the window
        while zeros > 1:
            if nums[l] == 0:
                zeros -= 1
            l += 1

        mx = max(mx, i - l + 1) # calculate mx

    return mx



if __name__ == '__main__':
    print find_max_consecutive_ones([1, 0, 1, 1, 0])
    print(find_max_consecutive_ones_1([1, 0, 1, 1, 0]))
