"""
https://leetcode.com/problems/word-pattern-ii/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:
You may assume both pattern and str contains only lowercase letters.
"""
def word_pattern_match(pattern, string):
    if len(pattern) == 0 and len(string) == 0:
        return True

    if len(pattern) == 0:
        return False

    hash_map = {}
    hash_set = set()

    return helper(pattern, string, 0, 0, hash_map, hash_set)

def helper(pattern, string, i, j, hash_map, hash_set):
    if i == len(pattern) and j == len(string):
        return True

    if i >= len(pattern) or j >= len(string):
        return False

    char = pattern[i]

    for k in range(j + 1, len(string) + 1):
        substring = string[j:k]

        if char not in hash_map and substring not in hash_set:
            hash_map[char] = substring
            hash_set.add(substring)

            if helper(pattern, string, i + 1, k, hash_map, hash_set):
                return True

            del hash_map[char]
            hash_set.remove(substring)
        elif char in hash_map and hash_map.get(char) == substring:
            if helper(pattern, string, i + 1, k, hash_map, hash_set):
                return True

    return False


if __name__ == '__main__':
    print word_pattern_match('abab', 'redblueredblue')
    print word_pattern_match('aaaa', 'asdasdasdasd')
    print word_pattern_match('aabb', 'xyzabcxzyabc')


