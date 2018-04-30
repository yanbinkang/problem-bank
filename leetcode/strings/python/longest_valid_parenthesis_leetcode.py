"""
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

algo:

In this approach, we make use of two counters left and right. First, we start traversing the string from the left towards the right and for every '(' encountered, we increment the left counter for every ')' encountered, we increment the right counter. Whenever left becomes equal to right, we calculate the length of the current valid string and keep track of maximum length substring found so far. If right becomes greater than left we reset left and right to 0.

Next, we start traversing the string from right to left and similar procedure is applied.

ref: https://leetcode.com/problems/longest-valid-parentheses/solution/#approach-4-without-extra-space-accepted

O(n) time, O(1) space
"""
def longestValidParentheses(s):
    left, right, max_length = 0, 0, 0

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            max_length = max(max_length, right * 2)
        elif right > left:
            left = right = 0

    right = left = 0

    """
    why do we need to scan from right to left? Consider the input "(()" , left to right scan will output 0, but the answer is 2.
    """
    for i in reversed(range(len(s))):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            max_length = max(max_length, right * 2)
        elif left > right:
            left = right = 0

    return max_length

def longestValidParenthesesDP(s):
    max_so_far = 0
    dp = [0] * len(s)

    for i in range(1, len(s)):
        if s[i] == ')':
            dp[i] = dp[i - 2] + 2
        elif i - dp[i - 1] - 1 >= 0 and dp[i - dp[i - 1] - 1] == '(':
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            else:
                dp[i] = 0


        max_so_far = max(max_so_far, dp[i])

    return max_so_far
