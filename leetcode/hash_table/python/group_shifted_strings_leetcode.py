"""
https://leetcode.com/problems/group-shifted-strings/

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

O(n^2) time O(n) space

algorithm:
  for each string calculate the distance between the consecutive strings. store the distance as key and the string as value. In the end all string that have the same relative distance will be grouped together. Fianlly return the dictionary values.

https://discuss.leetcode.com/topic/71031/python-group-them-by-relative-distance
"""
import collections
def group_strings(strings):
    d = collections.defaultdict(list)

    for s in strings:
        temp = ''
        for i in range(1, len(s)):
            temp += ( str( (ord(s[i]) - (ord(s[i - 1])) ) % 26 ) )

        d[temp].append(s)

    return d.values()

if __name__ == '__main__':
    print group_strings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])

