"""
https://leetcode.com/problems/unique-binary-search-trees/
https://www.youtube.com/watch?v=YDf982Lb84o
https://discuss.leetcode.com/topic/19670/python-solutions-dp-catalan-number
"""

def num_trees(n):
    t = [0] * (n + 1)
    t[0] = 1

    i = 1
    while i <= n:
        j = 0
        while j < i:
            t[i] += t[j] * t[i - j -1]
            j += 1
        i += 1

    return t[n]

print num_trees(3)
