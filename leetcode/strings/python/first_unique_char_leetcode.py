"""
https://leetcode.com/problems/first-unique-character-in-a-string


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

https://discuss.leetcode.com/topic/55148/java-7-lines-solution-29ms/2
"""
import string


def first_unique_char(s):
    collection = [0] * 26

    for char in s:
        index = string.lowercase.index(char)
        collection[index] += 1

    for char in s:
        index = string.lowercase.index(char)
        if collection[index] == 1:
            return s.index(char)

    return -1


def first_unique_char_1(s):
    collection = [0] * 26

    for char in s:
        index = ord(char) - ord('a')
        collection[index] += 1

    for char in s:
        index = ord(char) - ord('a')
        if collection[index] == 1:
            return s.index(char)

    return -1


if __name__ == '__main__':
    print(first_unique_char('leetcode'))
    print(first_unique_char('loveleetcode'))
    print('\n')
    print(first_unique_char_1('leetcode'))
    print(first_unique_char_1('loveleetcode'))
