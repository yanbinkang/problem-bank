"""
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/2
"""
def combination_sum_3(k, n):
    result = []
    if not k or not n:
        return result

    helper(k, n, result, 1, [])

    return result

def helper(k, n, result, start, temp_list):
    if len(temp_list) > k or n < 0:
        return
    if n == 0 and len(temp_list) == k:
        result.append([] + temp_list)
    else:
        for i in range(start, 10):
            temp_list.append(i)
            helper(k, n - i, result, i + 1, temp_list)
            temp_list.pop()


if __name__ == '__main__':
    print combination_sum_3(3, 7)
    print('\n')
    print combination_sum_3(3, 9)
    print('\n')
    print combination_sum_3(6, 35)
