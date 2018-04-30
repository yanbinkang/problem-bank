"""
https://leetcode.com/problems/reverse-string-ii/#/description

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

solution: For every block of 2k characters starting with position i, we want to replace S[i:i+k] with it's reverse.

https://discuss.leetcode.com/topic/82596/python-straightforward-with-explanation
"""
def reverse_str(s, k):
    s = list(s)

    for i in range(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])

    return ''.join(s)

if __name__ == '__main__':
    print reverse_str('abcdefg', 2)
