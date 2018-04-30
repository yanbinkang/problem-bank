"""
https://leetcode.com/problems/sliding-window-maximum/description/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
from collections import deque
def maxSlidingWindow(nums, k):
    result = []

    if k > len(nums): return result

    window = deque()

    # find out max for first window
    for i in range(0, k):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    result.append(nums[window[0]])

    for i in range(k, len(nums)):
        # remove all numbers that are smaller than current number from tail of list
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window anymore
        if window and window[0] < i - k + 1:
            """
            think about i - k + 1 as indices in of the array. for eg if i = 3,
            i - k + 1 will be 3 - 3 + 1 = 1. which means that if the index stored at window[0] is less than this number, it's out of the current window and should be removed!
            """
            window.popleft()

        window.append(i)

        result.append(nums[window[0]])

    # return nums[window[0]]
    return result

if __name__ == '__main__':
    print(maxSlidingWindow([-4, 2, -5, 3, 6], 3))
    print maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)


