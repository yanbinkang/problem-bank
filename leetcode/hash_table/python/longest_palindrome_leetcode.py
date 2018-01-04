"""
https://leetcode.com/problems/longest-palindrome/

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

algorithm:

just count the number of same pairs, then this can be used to put in the different direction to consist of palindrome. Then if there exist more chars, we can put one in the middle.

https://discuss.leetcode.com/topic/61300/simple-hashset-solution-java
"""
def longest_palindrome(s):
    distinct = set()

    count = 0

    for char in s:
        if char in distinct:
            distinct.remove(char)
            count += 1
        else:
            distinct.add(char)


    if len(distinct) == 0:
        return count * 2
    else:
        return count * 2 + 1


if __name__ == '__main__':
    print longest_palindrome('abccccdd')
