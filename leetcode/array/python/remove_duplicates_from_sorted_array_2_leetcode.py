"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

ref: https://discuss.leetcode.com/topic/17180/3-6-easy-lines-c-java-python-ruby

Same simple solution written in several languages. Just go through the numbers and include those in the result that haven't been included twice already.
"""
def remove_duplicates(nums):
    i = 0

    for n in nums:
        if i < 2 or n > nums[i - 2]:
            nums[i] = n
            i += 1

    return i

def remove_duplicates_1(nums):
    if len(nums) < 2: return len(nums)

    i = 1 #i = k - 1

    # for i in range(k, len(nums)):
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 1]:
            i += 1
            nums[i] = nums[j]

    return i + 1


"""
The solution can be generalized to 'at most K duplicates'


def remove_duplicates(nums):
    i = 0

    for n in nums:
        if i < k or n > nums[i - k]:
            nums[i] = n
            i += 1

    return i
"""

print remove_duplicates([1, 1, 1, 2, 2, 3])
print('\n')
print remove_duplicates_1([1, 1, 1, 2, 2, 3])
