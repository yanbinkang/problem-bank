"""
https://leetcode.com/problems/implement-strstr/#/description

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Time complexity: O(m * n) where m is length of haystack and n is length of the needle. Checking haystack[i:i+len(needle)] == needle is O(m) done O(n) times.

Space: O(1)

https://discuss.leetcode.com/topic/29848/my-answer-by-python
"""
def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1): # O(m)
        if haystack[i:i+len(needle)] == needle: # O(n)
            return i

    return -1

if __name__ == '__main__':
    print strStr('albert', 'rt')
