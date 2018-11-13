"""
https://leetcode.com/problems/majority-element/?tab=Description

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

read: https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

https://discuss.leetcode.com/topic/28601/java-solutions-sorting-hashmap-moore-voting-bit-manipulation

O(n) time O(1) space
"""
def majority_element(nums):
    major = 0
    count = 0

    for i in range(len(nums)):
        if count == 0:
            major = nums[i]

        if major == nums[i]:
            count += 1
        else:
            count -= 1

    # get count of majority element
    major_count = nums.count(major)

    # return majority if count > n / 2
    if major_count > len(nums) // 2:
        return major

# O(n) time and space
def majority_element_1(nums):
    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1

    return [i for i, j in d.items() if j > len(nums) // 2][0]


"""
NOTICE that the majority element always exist in the array,so that the middle always is the answer
"""
def majority_element_2(nums):
    return sorted(num)[len(num)/2]



if __name__ == '__main__':
    print(majority_element([1, 2, 3, 3, 3, 3, 3, 3, 10]))
