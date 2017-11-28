"""
manacher algorithm O(n)
http://en.wikipedia.org/wiki/Longest_palindromic_substring
https://leetcode.com/discuss/28791/manacher-algorithm-in-python-o-n
http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
"""
def longest_palindrome(s):
    t = '#'.join('^{}$'.format(s))
    n = len(s)
    p = [0] * n
    c = r = 0

    for i in range(1, n - 1):
        p[i] = (r > i) and min(r - i, p[2*c - i])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r:
            c, r = i, i + p[i]

    max_len, center_index = max((n, i) for i, n in enumerate(p))
    return s[(center_index - max_len)//2 : (center_index + max_len)//2]

print longest_palindrome("babcbabcbaccba")
