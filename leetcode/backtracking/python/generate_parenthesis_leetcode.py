"""
https://leetcode.com/problems/generate-parentheses/#/description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

left represents how many left parenthesis remains. right represents how many right parenthesis remains.
"""
def generate_parenthesis(n):
    result = []
    helper(result, '', n, n)

    return result

def helper(result, string, left, right):
    if left == 0 and right == 0:
        result.append(string)
        return

    if left > 0:
        helper(result, string + '(', left - 1, right)
    if right > left:
        helper(result, string + ')', left, right - 1)


if __name__ == '__main__':
    print generate_parenthesis(3)
