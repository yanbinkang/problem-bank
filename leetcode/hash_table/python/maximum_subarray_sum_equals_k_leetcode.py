"""
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

NOTE: The problem proposes to find a contiguous array. But subarray is by itself contiguous so no problem with wording of problem.

algo:
1. Calculate accumulated sum for nums array.

2. Go through the accumulated sum:
    a) If the sum == k, update max_length. This happens when there are negative numbers in the array. SO when the accumulated sum is equal to k, we have might have a max_length and we need to update it. eg. max_subarray_len([1, -1, 5, -2, 3], 3)

    b) if sum - k is in the hash table, update max_length. Example, given k = 6 and nums as [23, 2, 4, 6, 7], we have an accumulated sum:
                  [23, 25, 29, 35, 42].
    We can tell that 29 - 23 == 6, this means from index 0 (exclusive) to 2 (inclusive) we have seen a nums that equals 6. Also, 35 - 29 == 6 meaning from index 2 (exclusive) to 3 (inclusive) we have seen num(s) that equal 6.

    c. If total not in dictionary, add it as key with index as value.
"""
def max_subarray_len(nums, k):
    n, imax = len(nums), -float('inf')

    # accumulate the nums
    for i in range(1, n):
        nums[i] += nums[i - 1]

    d = {}

    for i in range(len(nums)): # for i, num in enumerate(nums):
        num = nums[i]

        if num == k:
            imax = max(imax, i + 1)

        if num - k in d:
            imax = max(imax, i - d[num - k])

        # keep only 1st duplicate as we want first index as left as possible
        if num not in d:
            d[num] = i

    return 0 if imax == -float('inf') else imax

"""
https://discuss.leetcode.com/topic/33259/o-n-super-clean-9-line-java-solution-with-hashmap

algorithm: The HashMap stores the sum of all elements before index i as key, and i as value. For each i, check not only the current sum but also (currentSum - previousSum) to see if there is any that equals k, and update max length.
"""
def max_subarray_length_0(nums, k):
    hash_map = {}
    hash_map[0] = -1

    total, max_size = 0, 0

    for i in range(len(nums)):
        total += nums[i]

        # check if there's a previous sum that equals k
        if (total - k) in hash_map:
            max_size = max(max_size, i - hash_map[total - k])

        if total not in hash_map:
            hash_map[total] = i

    return max_size

def max_subarray_length_1(nums, k):
    total, max_size = 0 , 0
    hash_map = {}

    for i in range(len(nums)):
        total = total + nums[i]

        # found a subarray. add 1 to current index to get length
        if total == k:
            max_size = i + 1
        elif total - k in hash_map:
            """
            we have found another subarray. check if this new subarray is longer than first one
            """
            max_size = max(max_size, i - hash_map[total - k])

        if total not in hash_map:
            hash_map[total] = i

    return max_size

def max_subarray_length_2(nums, k):
    if not nums or len(nums) == 0:
        return 0

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    d = {}

    d[0] = -1

    maxmax = 0

    for i in range(len(nums)):
        if nums[i] - k in d:
            maxmax = max(maxmax, i - d[nums[i] - k])

        if nums[i] not in d:
            d[nums[i]] = i

    return maxmax


if __name__ == '__main__':
    print max_subarray_length_0([23, 5, 4, 7, 2, 11], 20)
    print max_subarray_len([1, -1, 5, -2, 3], 3)
    print('\n')
    print max_subarray_length_0([1, -1, 5, -2, 3], 3)
    print max_subarray_length_0([1, -1, 5, -2, 3], 3) # tests why we need hash_map[0] = -1

    print('\n')
    print max_subarray_length_1([1, -1, 5, -2, 3], 3)
    print max_subarray_length_1([-2, -1, 2, 1], 1)
    print max_subarray_length_1([23, 2, 4, 6, 7], 6)
    print('\n')
    print max_subarray_length_2([1, -1, 5, -2, 3], 3)
    print max_subarray_length_2([-2, -1, 2, 1], 1)
    print max_subarray_length_2([23, 2, 4, 6, 7], 6)

