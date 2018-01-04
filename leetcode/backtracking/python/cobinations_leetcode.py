"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

https://leetcode.com/problems/combinations/

https://discuss.leetcode.com/topic/46168/combinations-v-s-combination-sum-iii-java
"""

def combine(n, k):
    result = []

    if not n or not k:
        return result

    helper(n - k + 1, k, result, 1, [])

    return result

def helper(n, k, result, start, temp_list):
    if len(temp_list) == k:
        result.append([] + temp_list)
    else:
        for i in range(start, n + 1):
            temp_list.append(i)
            helper(n + 1, k, result, i + 1, temp_list)
            temp_list.pop()


if __name__ == '__main__':
    print combine(4, 2)
    print('\n')
    print combine(10, 7)
    print('\n')
    print combine(20, 16)
