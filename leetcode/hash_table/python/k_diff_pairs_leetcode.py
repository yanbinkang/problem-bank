"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/?tab=Description

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

O(n) time O(n) space

https://discuss.leetcode.com/topic/81714/java-o-n-solution-one-hashmap-easy-to-understand
"""

def find_pairs(nums, k):
    count = 0

    if not nums or len(nums) == 0 or k < 0: return count

    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1

    for key in d.keys():
        if k == 0:
            if d[key] >= 2:
                count += 1
        else:
            if key + k in d:
                count += 1
    return count

if __name__ == '__main__':
    print find_pairs([3, 1, 4, 1, 5], 2) #2
    print find_pairs([1, 2, 3, 4, 5], 1) #4
    print find_pairs([1, 3, 1, 5, 4], 0) #1
    print find_pairs([1, 2, 3, 4, 5], -1) #0

