"""
https://leetcode.com/problems/repeated-substring-pattern/#/description

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
def repeated_substring_pattern(s):
    return s in (2 * s)[1:-1]



if __name__ == '__main__':
    print repeated_substring_pattern('aba')
    print repeated_substring_pattern('abab')
    print repeated_substring_pattern('abcabcabcabc')
    print repeated_substring_pattern('abaababaab')
    print repeated_substring_pattern('ababab')
