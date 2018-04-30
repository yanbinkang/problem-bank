"""
https://leetcode.com/problems/one-edit-distance/#/description

Given two strings S and T, determine if they are both one edit distance apart.
"""

"""
ref: https://discuss.leetcode.com/topic/18392/accepted-clean-java-solution-with-explanation-two-pointers

By default this solution assumes that the 2nd string is longer than the first

The basic idea is we keep comparing s and t from the beginning, once there's a difference, we try to replace s(i) with t(j) or insert t(j) to s(i) and see if the rest are the same.

Example: i and j are the two pointers of S and T, we found that 'b' != 'c' and we try to replace it:

     i                           i
S: a c d      replace       S: a b d
T: a b c d   --------->     T: a b c d    --->  "d" != "cd", no good
     j                           j

now we try to insert T(j) to S(i) and we get:

     i                           i
S: a c d      insert        S: a b c d
T: a b c d   --------->     T: a b c d    --->  "cd" == "cd", viola!
     j                           j

To keep the code simple, we make s is always shorter than t, so we don't need to try deletion.
"""
def is_one_edit_distance(s, t):
    # if not s or not t:
    #     return False

    m, n = len(s), len(t)

    if m > n:
        return is_one_edit_distance(t, s)

    if n - m > 1: return False

    i, j = 0, 0

    while i < m and j < n:
        if s[i] != t[j]:
            return s[i + 1:] == t[j + 1:] or s[i:] == t[j + 1:]

        i += 1
        j += 1

    return n - m == 1

# https://discuss.leetcode.com/topic/22670/python-concise-solution-with-comments/4
def is_one_edit_distance_1(s, t):
    if len(s) > len(t):
        return is_one_edit_distance_1(t, s)

    if abs(len(s) - len(t)) > 1 or s == t:
        return False

    for i in range(len(s)): # s is shorter string
        if s[i] != t[i]:
            return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]

    return True


if __name__ == '__main__':
    print is_one_edit_distance('acd', 'abcd')
