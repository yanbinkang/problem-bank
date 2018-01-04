"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

https://discuss.leetcode.com/topic/12968/ac-hashmap-clear-code-java

https://discuss.leetcode.com/topic/19993/python-different-solutions-dictionary-etc

NB: Similar to https://leetcode.com/problems/word-pattern/
"""
def is_isomorphic(s, t):
    char_map = {}

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if s_char in char_map:
            if char_map.get(s_char) != t_char:
                return False
        else:
            if t_char in char_map.values():
                return False

            char_map[s_char] = t_char

    return True


def is_isomorphic_alt(s, t):
    d1, d2 = {}, {}

    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]

    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]

    return sorted(d1.values()) == sorted(d2.values())

if __name__ == '__main__':
    print is_isomorphic('egg', 'add')
    print('\n')
    print is_isomorphic('foo', 'bar')
    print('\n')
    print is_isomorphic('paper', 'title')
    print('\n')
    print is_isomorphic('', '')
    print('\n')
    print is_isomorphic('a', 'a')
    print('\n')
    print is_isomorphic('ab', 'ac')
    print('\n')
    print is_isomorphic('egg', 'aaa')
