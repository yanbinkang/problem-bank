"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

def partition(s):
    result = []

    if not s: return result

    helper(s, result, 0, [])

    return result

def helper(s, result, start, temp_list):
    if start == len(s):
        result.append([] + temp_list)
    else:
        for i in range(start, len(s)):
            if is_palindrome(s, start, i):
                temp_list.append(s[start:i + 1])
                helper(s, result, i + 1, temp_list)
                temp_list.pop()

def is_palindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1

    return True

if __name__ == '__main__':
    print partition('aab')
    print partition('aabb')
    print partition('abc')
