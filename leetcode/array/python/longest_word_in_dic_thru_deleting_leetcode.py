"""
https://leetcode.com/contest/leetcode-weekly-contest-21/problems/longest-word-in-dictionary-through-deleting/

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:

1. All the strings in the input will only contain lower-case letters.
2. The size of the dictionary won't exceed 1,000.
3. The length of all the strings in the input won't exceed 1,000.

https://discuss.leetcode.com/topic/80816/python-simple-two-pointer
"""
def find_longest_word(s, d):
    d.sort(key = lambda x: (-len(x), x))

    for word in d:
        i = 0

        for char in s:
            if i < len(word) and word[i] == char:
                i += 1

            if i == len(word):
                return word

    return ''


if __name__ == '__main__':
    print find_longest_word('abpcplea', ['ale','apple','monkey','plea'])
    print('\n')
    print find_longest_word('abpcplea', ['a', 'b', 'c'])
    print('\n')
    print find_longest_word('bab', ['ba', 'ab', 'a', 'b'])
