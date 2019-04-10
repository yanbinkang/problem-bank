"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


def findDuplicates(nums):
    '''
    When find a number i, flip the number at position i - 1 to negative.
    If the number at position i - 1 is already negative, i is the number that occurs twice.
    '''
    result = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            result.append(abs(index + 1))
        nums[index] = -nums[index]

    return result


# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
def findDuplicates2(nums):
    result = []

    for i in range(len(nums)):
        if nums[abs(nums[i])] >= 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            result.append(abs(nums[i]))

    return result


if __name__ == "__main__":
    print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    print('\n')
    print(findDuplicates2([1, 6, 3, 1, 3, 6, 6]))
