"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

https://discuss.leetcode.com/topic/26573/very-fast-3ms-java-solution-using-hashmap

https://leetcode.com/problems/isomorphic-strings/
"""


def word_pattern(pattern, string):
    words = string.split()
    d = {}

    if len(words) != len(pattern):
        return False

    for i in range(len(words)):
        char = pattern[i]

        if char in d.keys():
            if d.get(char) != words[i]:
                return False
        else:
            # at this point, we know the pattern and word (key/value pair) can be stored dict. But if word is already stored as a value in dict, return false. This means its already been associated with another pattern. See the last example.
            if words[i] in d.values():
                return False

            d[char] = words[i]

    return True


if __name__ == '__main__':
    print(word_pattern('abba', 'dog cat cat dog'))
    print(word_pattern('abba', 'dog cat cat fish'))
    print(word_pattern('abba', 'dog dog dog dog'))
