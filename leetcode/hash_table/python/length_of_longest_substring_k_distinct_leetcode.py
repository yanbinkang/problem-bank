"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/?tab=Description

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.
"""
def length_of_longest_substring_k_distinct(s, k):
    dic = {}
    left, right, count, max_length = 0, 0, 0, 0

    while right < len(s):
        dic[s[right]] = dic.get(s[right], 0) + 1

        if s[right] in dic:
            if dic[s[right]] == 1: # new char
                count += 1
        right += 1

        while count > k:
            if s[left] in dic:
                dic[s[left]] -= 1

                if dic[s[left]] == 0:
                    count -= 1

            left += 1

        max_length = max(max_length, right - left)

    return max_length

if __name__ == '__main__':
    print length_of_longest_substring_k_distinct('eceba', 2)
