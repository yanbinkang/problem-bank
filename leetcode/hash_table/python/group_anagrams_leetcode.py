"""
https://leetcode.com/problems/group-anagrams/#/description

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.

O(n*mlog(m)) in time and O(n) in space, where m represents the average length of the strings in strs and n is the number of the strings in strs
"""
def group_anagrams(strs):
    strs_hash = {}

    for string in strs: # O(n)
        sorted_string = ''.join(sorted(string)) # mlogm

        strs_hash[sorted_string] = strs_hash.get(sorted_string, []) + [string]

        # this is also correct
        # if sorted_string in strs_hash:
        #     strs_hash[sorted_string].append(string)
        # else:
        #     strs_hash[sorted_string] = [string]
    return strs_hash.values()


if __name__ == '__main__':
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print group_anagrams(strs)
