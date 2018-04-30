"""
https://leetcode.com/problems/decode-ways/#/description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

ref: https://discuss.leetcode.com/topic/4727/concise-cpp-solution-with-o-1-space-and-o-n-time

DON'T UNDERSTAND THIS SHIT! NEED TO GET IT!!!!!!!!

O(n) time O(1) space
"""
def num_decodings(s):
    # empty string or leading zero means no way
    if not s or s[0] == '0': return 0

    # r1 and r2 store ways of the last and the last of the last
    r1, r2 = 1, 1

    for i in range(1, len(s)):
        # zero voids ways of the last because zero cannot be used separately
        if s[i] == '0':
            r1 = 0

        # possible two-digit letter, so new r1 is sum of both while new r2 is old r1
        if s[i - 1] == '1' or (int(s[i - 1]) == 2 and int(s[i]) <= 6):
            r1 = r2 + r1
            r2 = r1 - r2
        else: # one-digit letter, no new way added
            r2 = r1

    return r1

if __name__ == '__main__':
    print num_decodings('12')
    print num_decodings('26')
    print num_decodings('56')
    print num_decodings('100')
    print num_decodings('10')
