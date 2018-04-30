"""
https://discuss.leetcode.com/topic/153/continuous-sequence-against-target-number

Given a sequence of positive integers A and an integer T, return whether there is a continuous sequence of A that sums up to exactly T

Example:
[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20

[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8

[1, 3, 5, 23, 2], 7. Return False because no sequence in this array adds up to 7
"""
def has_sequnce(nums, t):
    if not nums or t <= 0: return False
    left, right, total = 0, 0, 0

    while right < len(nums):
        total += nums[right]
        right += 1

        while total > t:
            total -= nums[left]
            left += 1

        if total == t:
            return True

    return False

def has_sequnce_1(nums, t):
    if not nums or t <= 0: return False

    n = len(nums)

    # accumulate the nums
    for i in range(1, n):
        nums[i] += nums[i - 1]

    d = {}

    for i in range(len(nums)):
        num = nums[i]

        if num - t in d:
            return True

        if num not in d:
            d[num] = i

    return False

if __name__ == '__main__':
    print has_sequnce([23, 5, 4, 7, 2, 11], 20)
    print has_sequnce([1, 3, 5, 23, 2], 8)
    print has_sequnce([1, 3, 5, 23, 2], 7)
    print('\n')
    print has_sequnce_1([23, 5, 4, 7, 2, 11], 20)
    print has_sequnce_1([1, 3, 5, 23, 2], 8)
    print has_sequnce_1([1, 3, 5, 23, 2], 7)





