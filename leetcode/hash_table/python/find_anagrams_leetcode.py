"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

https://discuss.leetcode.com/topic/64434/shortest-concise-java-o-n-sliding-window-solution/4

loot at this: http://bookshadow.com/weblog/2016/10/23/leetcode-find-all-anagrams-in-a-string/

https://discuss.leetcode.com/topic/68976/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
"""
def find_anagrams(s, p):
    result = []

    if len(p) > len(s): return result

    d = {}

    for char in p:
        d[char] = d.get(char, 0) + 1

    count = len(p)

    left, right = 0, 0

    while right < len(s):
        if s[right] in d:

            if d[s[right]] > 0:
                count -= 1

            d[s[right]] -= 1

        right += 1

        while count == 0:
            """
            # we do this because we're about to resize the window!

            think about it, it makes sense. We've made use of the count and must restore it.
            This is to make sure subsequent characters are also checked!
            """
            if s[left] in d:
                d[s[left]] += 1

                if d[s[left]] > 0:
                    count += 1

            if right - left == len(p):
                result.append(left)

            left += 1

    return result

if __name__ == '__main__':
    print find_anagrams('cbaebabacd', 'abc')
    print find_anagrams('abab', 'ab')
    print find_anagrams('aa', 'bb')
    print find_anagrams('baa', 'aa')
