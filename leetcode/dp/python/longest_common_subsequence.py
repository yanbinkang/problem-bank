"""
Problem Statement
=================

Given two sequences A = [A1, A2, A3,..., An] and B = [B1, B2, B3,..., Bm], find the length of the longest common
subsequence.

Video
-----

* https://youtu.be/NnD96abizww

Complexity
----------

* Recursive Solution: O(2^n) (or O(2^m) whichever of n and m is larger).
* Dynamic Programming Solution: O(n * m) time and space

Reference
---------

* https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
* http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
"""

"""
example:

S = 'abcdaf'
T = 'acbcf'

LCS = 'abcf'

Initial Table looks like this:

      a  b  c  d  a  f
[ [0, 0, 0, 0, 0, 0, 0],
a [0, 0, 0, 0, 0, 0, 0],
c [0, 0, 0, 0, 0, 0, 0],
b [0, 0, 0, 0, 0, 0, 0],
c [0, 0, 0, 0, 0, 0, 0],
f [0, 0, 0, 0, 0, 0, 0]]

We start off with the first a from the col and row. Since they are equal we increase LCS by one by finding max of the LCS we've found so far and add 1 to it i.e 1 + value at diagonal:

    T[i][j] = 1 + T[i - 1][j - 1]

Then the row value of 'a' stays the same and we move to the next col value of 'b'; so now we're comparing 'a' with 'ab'.

Now, we compare the last char in the col which is 'b' to the char in the row 'a'. Since they are different, we set T[i][j] to the max LCS we've found s far, i.e max of value at the top or value at the left:

    T[i][j] = max(T[i - 1][j], T[i][j - 1])

Then move to comparing 'ac' and 'a'. 'ac' comes form the rows and 'a' from the col. Next compare 'ac' and 'ab' and so on...

Finally return T[row][col]

eg. given table

      a  b  c  d  a  f
[ [0, 0, 0, 0, 0, 0, 0],
a [0, 1, 1, 1, 1, 1, 1],
c [0, 1, X, Y, 0, 0, 0],
b [0, 0, 0, 0, 0, 0, 0],
c [0, 0, 0, 0, 0, 0, 0],
f [0, 0, 0, 0, 0, 0, 0]]

At X we're comparing 'ac' with 'a'. And since 'c' != 'a' the result is the max LCS we've found so far, i.e max of value at the top or value at the left. Value at the top because we know comparing 'ab' and 'a' already yielding a result of 1. Value at the left because we already know comparing 'ac' and 'a' yielded 1.

At Y, we're comparing 'ac' with 'abc'. Since 'c' == 'c', we know we've added a new common subsequence. So we add 1 to the already computed value for comparing 'a' with 'ab' i.e the chars without the 'c'.
"""
def longest_common_subsequence(s, t):
    cols = len(s) + 1 # Add 1 to represent 0 valued column for DP
    rows = len(t) + 1 # Add 1 to represent 0 valued row for DP

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    max_length = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if t[i - 1] == s[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

            max_length = max(max_length, T[i][j])

    return max_length

if __name__ == '__main__':
    s = 'ABCDGHLQR'
    t = 'AEDPHR'

    assert 4 == longest_common_subsequence(s, t)
