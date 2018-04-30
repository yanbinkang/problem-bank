"""
https://leetcode.com/problems/is-subsequence/description/

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""
from collections import defaultdict
from bisect import bisect_left

# greedy
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) > len(t): return False

    i = 0

    for j in range(len(t)):
        if i < len(s) and s[i] == t[j]:
            i += 1

    return i == len(s)


# ref: https://discuss.leetcode.com/topic/57718/easy-to-understand-binary-search-solution
# binary search. I don't understand this shit!
def create_map(s):
    # create a map. key is char and value is index of appearance in ascending order
    pos_map = defaultdict(list)

    for i, char in enumerate(s):
        pos_map[char].append(i)

    return pos_map

def is_subsequnce(s, t):
    pos_map = create_map(t)
    low_bound = 0

    for char in s:
        if char not in pos_map: return False

        char_index_list = pos_map[char]

        i = bisect_left(char_index_list, low_bound)

        if i == len(char_index_list): return False

        low_bound = char_index_list[i] + 1

    return True


