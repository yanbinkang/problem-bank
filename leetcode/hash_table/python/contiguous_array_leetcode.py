"""
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

algorithm: The idea is to change 0 in the original array to -1. Thus, if we find SUM[i, j] == 0 then we know there are even number of -1 and 1 between index i and j. Also put the sum to index mapping to a HashMap to make search faster.
"""
def find_max_length(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    sum_to_index_map = {}
    sum_to_index_map[0] = -1

    total, max_size = 0, 0

    for i in range(len(nums)):
        total += nums[i]

        if total in sum_to_index_map:
            max_size = max(max_size, i - sum_to_index_map[total])
        else:
            sum_to_index_map[total] = i

    return max_size

# https://discuss.leetcode.com/topic/80020/one-pass-use-a-hashmap-to-record-0-1-count-difference
def find_max_length_1(nums):
    d = {}
    d[0] = -1

    zero, one, max_size = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        else:
            one += 1

        if zero - one  in d:
            max_size = max(max_size, i - d[zero - one])
        else:
            d[zero - one] = i

    return max_size

if __name__ == '__main__':
    print find_max_length([0, 1])
    print find_max_length([0, 1, 0])
    print find_max_length([0, 1, 0, 0, 1, 1])
    print('\n')
    print find_max_length_1([0, 1])
    print find_max_length_1([0, 1, 0])
    print find_max_length_1([0, 1, 0, 0, 1, 1])
