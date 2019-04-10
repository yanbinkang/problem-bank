"""
https://leetcode.com/problems/valid-parentheses/#/description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

https://discuss.leetcode.com/topic/6534/simple-python-solution-with-stack

O(n) time and space
ref: https://wiki.python.org/moin/TimeComplexity
"""


def is_valid(s):
    stack = []
    d = {']': '[', '}': '{', ')': '('}

    for char in s:
        if char in d.values():  # just append any open parens
            stack.append(char)
        elif char in d.keys():
            # at this point we should have already seen an opens '({['. So if stack is empty return False. Also if opens doesn't match closers ']})' return False
            if stack == [] or d[char] != stack.pop():
                return False
        else:  # char not in the characters we want
            return False

    # if stack is empty at this point, return True else False
    return stack == []


if __name__ == '__main__':
    print(is_valid('()'))
    print('\n')
    print(is_valid('()[]{}'))
    print('\n')
    print(is_valid('([)]'))
    print('\n')
    print(is_valid('{{([][])}()}'))
    print('\n')
