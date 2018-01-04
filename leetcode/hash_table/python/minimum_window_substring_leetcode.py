"""
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

ref: https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
"""
def min_window(s, t):
    if len(t) > len(s): return ''

    d = {}

    for c in t:
        d[c] = d.get(c, 0) + 1

    left, right, head, count = 0, 0, 0, len(t)

    min_length = float('inf')

    while right < len(s):
        if s[right] in d:
            if d[s[right]] > 0:
                count -= 1

            # if char or s[right] does not exist in t, d[right]) will be negative
            d[s[right]] -= 1

        right += 1

        while count == 0:
            if s[left] in d:
                d[s[left]] += 1

                if d[s[left]] > 0:
                    count += 1

            if right - left < min_length:
                min_length = right - left
                head = left

            left += 1

    if min_length == float('inf'): return ''
    return s[head:head + min_length]

def min_window_1(s, t):
    if len(t) > len(s): return ''

    d = {}

    for c in t:
        d[c] = d.get(c, 0) + 1

    left, right, head, count = 0, 0, 0, len(t)

    min_length = float('inf')

    while right < len(s):
        # If char in s exists in t, decrease counter
        if d.get(s[right]) > 0:
            count -= 1

        # Decrease d[s[right]]. If char does not exist in t, d[s[right]] will be negative
        d[s[right]] = d.get(s[right], 0) - 1

        right += 1 # move right forward

        # we've found all the chars in t in s
        # when we found a valid window, move left to find a smaller window
        while count == 0:
            if right - left < min_length:
                min_length = right - left
                head = left

            """
            if we care about s[left], we need to update its value and count

            Why? If we care about s[left], we would have decremented the count and value earlier. We need to add it back in case we see another char == s[left]

            remember earlier we said if the char does not exist in t d[s[right]] will be negative. So in the same vain if d[s[left]] is not greater than zero, we don't care about this char so we won't increment count for the next window!
            """
            if s[left] in d:
                d[s[left]] += 1

                if d[s[left]] > 0:
                    count += 1

            left += 1

    if min_length == float('inf'): return ''
    return s[head:head + min_length]


if __name__ == '__main__':
    print min_window('ADOBECODEBANC', 'ABC') #BANC
    print min_window('A', 'A') #A
    print min_window('cabwefgewcwaefgcf', 'cae')  #cwae
    print min_window('aa', 'aa') #aa
    print('\n')
    print min_window_1('ADOBECODEBANC', 'ABC') #BANC
    print min_window_1('A', 'A') #A
    print min_window_1('cabwefgewcwaefgcf', 'cae')  #cwae
    print min_window_1('aa', 'aa') #aa


