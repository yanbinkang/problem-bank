"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

https://discuss.leetcode.com/topic/20831/python-solutions-sort-and-dictionary
"""
def is_anagram1(s, t):
    return sorted(s) == sorted(t)

def is_anagram2(s, t):
    dic1, dic2 = {}, {}

    for item in s:
        dic1[item] = dic1.get(item, 0) + 1

    for item in t:
        dic2[item] = dic2.get(item, 0) + 1

    return dic1 == dic2

def is_anagram3(s, t):
    dic1, dic2 = [0]*26, [0]*26

    for item in s:
        dic1[ord(item) - ord('a')] += 1

    for item in t:
        dic2[ord(item) - ord('a')] += 1

    return dic1 == dic2
