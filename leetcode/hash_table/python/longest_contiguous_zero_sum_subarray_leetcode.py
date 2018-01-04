"""
https://discuss.leetcode.com/topic/25465/longest-continous-zero-sum-subarray

Find the length of longest continuous subarray within an array (containing at least one number) whose sum equals zero.

For example, given the array [1,0,-1,2],

The longest continuous subarray of zero-sum is [1,0,-1] , which has length = 3.

Algo:

1. Calculate accumulated sum for nums array.

2. Just go through the accumulated sum array and find if there's 0 or two identical numbers, if we find these, update the max length.

Why do we care about finding two identical numbers? Take as an eg. [1,0,-1,2]. After doing accumulated sum we get [1, 1, 0, 2]. Notice at index 1 we have accumulated sum of 1.

The only way we can have this is if there's a 0 in that particular index in the original nums array. It's basically saying, when you add zero to all the numbers before me you'll get an identical number. And since 0 is itself a continuous subarray which equals 0, we REALLY care about this.
"""
def longest_continous_zero_sum_subarray(nums):
    n, imax = len(nums), 0

    # accumulate the nums
    for i in range(1, n):
        nums[i] += nums[i - 1]

    d = {}

    for i in range(len(nums)):
        num = nums[i]

        if num == 0:
            imax = max(imax, i + 1)
        elif num in d:
            imax = max(imax, i - d[num])
        else:
            d[num] = i

    return imax

if __name__ == '__main__':
    print longest_continous_zero_sum_subarray([1, 0, -1, 2]) # 3
    print longest_continous_zero_sum_subarray([1, 1, 0, -1, 1, 2]) # 3
