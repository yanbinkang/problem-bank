"""
https://leetcode.com/problems/longest-harmonious-subsequence/#/description

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.

solution:
    1) https://discuss.leetcode.com/topic/89990/simple-java-hashmap-solution
    2) https://discuss.leetcode.com/topic/89994/python-straightforward-with-explanation
"""
def find_LHS(nums):
    dic = {}

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    result = 0

    for key in dic:
        if key + 1 in dic:
            result = max(result, dic.get(key + 1) + dic.get(key))

    return result

def find_LHS_2(nums):
    result = 0
    dic = {}

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

        if num - 1 in dic:
            result = max(result, dic[num] + dic[num - 1])

        if num + 1 in dic:
            result = max(result, dic[num] + dic[num + 1])

    return result

if __name__ == '__main__':
    print find_LHS([1,3,2,2,5,2,3,7])
    print('\n')
    print find_LHS_2([1,3,2,2,5,2,3,7])
