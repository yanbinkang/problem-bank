"""
https://leetcode.com/problems/wildcard-matching/

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") => false
isMatch("aa","aa") => true
isMatch("aaa","aa") => false
isMatch("aa", "*") => true
isMatch("aa", "a*") => true
isMatch("ab", "?*") => true
isMatch("aab", "c*a*b") => false
"""

"""
ref: https://longwayjade.wordpress.com/2015/04/26/leetcode-recursion-dp-greedy-wildcard-matching/

O(p * s) where p and s are the lengths of the pattern and input strings.
"""
def is_match_2(s, p):
    i, j = 0, 0
    asterick, match = -1, -1

    """
    asterick: once we found a star, we want to record the place of the star

    match: once we found a star, we want to start to match the rest of the pattern with the string, starting from the match position. This is for remembering the place where we need to start
    """

    # we check and match every char in s
    while i < len(s):
        # we are not currently at '*'. s and p match or p == '?'
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        # we are currently at a '*'
        elif j < len(p) and p[j] == '*':
            match = i
            asterick = j
            j += 1
        # they do not match, we are not currently at '*' but the last match is '*'
        elif asterick >= 0:
            match += 1
            i = match
            j = asterick + 1
        # they do not match, we are not at '*' and last matched is not a '*', then the answer is false
        else:
            return False

    # when we finish matching all chars in s, is pattern also finished? we cound only allow '*' at the rest of pattern
    while j < len(p) and p[j] == '*':
        j += 1

    return j == len(p)



def is_match_1(s, p):
    return is_match_rec(s, p, 0, 0)

def is_match_rec(text, pattern, i, j):
    if i == len(text) and j == len(pattern):
        return True


    if j < len(pattern) and pattern[j] == '*':
        while j < len(pattern) - 1 and pattern[j + 1] == '*':
            j += 1

        for k in range(i, len(text) + 1):
            if is_match_rec(text, pattern, k, j + 1):
                return True

            # if k >= len(text):
            #     return False

            # if pattern[j] != '*' and k != j:
            #     return False
        return False


    elif i < len(text) and j < len(pattern) and\
        (pattern[j] == '?' or pattern[j] == text[i]):
            return is_match_rec(text, pattern, i + 1, j + 1)

    return False

def is_match(s, p):
    string = list(s)
    pattern = list(p)

    write_index = 0
    is_first = True

    # replace multiple * with one *
    # e.g a**b***c --> a*b*c
    for i in range(len(pattern)):
        if pattern[i] == '*':
            if is_first:
                pattern[write_index] = pattern[i]
                write_index += 1
                is_first = False
        else:
            pattern[write_index] = pattern[i]
            write_index += 1
            is_first = True

    table = [[False for i in range(write_index + 1)] for j in range(len(s) + 1)]

    if write_index > 0 and pattern[0] == '*':
        table[0][1] = True

    table[0][0] = True


    for i in range(1, len(table)): # string
        for j in range(1, len(table[0])): # pattern
            if pattern[j -1] == '?' or string[i - 1] == pattern[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                table[i][j] = table[i - 1][j] or table[i][j - 1]

    # print table
    return table[-1][-1]




# print is_match('xaylmz', 'x?y*z')
# print is_match('aab', 'c*a*b')
# print is_match('aaa','aa')
# print is_match('aa', '*')
# print is_match('aa','a')
# print is_match('aa','aa')
# print is_match('ab', '?*')
# print is_match('aa', 'a*')
# print is_match('', '')
# print is_match('zacabz', '*a?b*')
# print('\n')
# print is_match_1('xaylmz', 'x?y*z')
# print is_match_1('aab', 'c*a*b')
# print is_match_1('aaa','aa')
# print is_match_1('aa', '*')
# print is_match_1('aa','a')
# print is_match_1('aa','aa')
# print is_match_1('ab', '?*')
# print is_match_1('aa', 'a*')
# print is_match_1('', '')
# print is_match_1('zacabz', '*a?b*')
# print is_match_1('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab', '***bba**a*bbba**aab**b')
# print('\n')
print is_match_2('xaylmz', 'x?y*z')
print is_match_2('aab', 'c*a*b')
print is_match_2('aaa','aa')
print is_match_2('aa', '*')
print is_match_2('aa','a')
print is_match_2('aa','aa')
print is_match_2('ab', '?*')
print is_match_2('aa', 'a*')
print is_match_2('', '')
print is_match_2('zacabz', '*a?b*')
print is_match_2('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab', '***bba**a*bbba**aab**b')

