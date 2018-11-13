"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9

Output: index1=1, index2=2
"""
def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    first = 0
    last = len(numbers) - 1

    while first < last:
        if numbers[first] + numbers[last] == target:
            return [first + 1, last + 1]
        elif numbers[first] + numbers[last] > target:
            last -= 1
        else:
            first += 1

if __name__ == '__main__':
    print two_sum([2, 7, 11, 15], 9)
