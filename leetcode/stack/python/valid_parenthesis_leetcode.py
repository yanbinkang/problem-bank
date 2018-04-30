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
    d = {']':'[', '}':'{', ')':'('}

    for char in s:
        if char in d.values(): # just append any open parens
            stack.append(char)
        elif char in d.keys():
            # at this point we should have already seen an opens '({['. So if stack is empty return False. Also if opens doesn't match closers ']})' return False
            if stack == [] or d[char] != stack.pop():
                return False
        else: # char not in the characters we want
            return False

    # if stack if empty at this point, return True else False
    return stack == []

# my solution
def is_valid_1(s):
    stack = []

    for char in s:
        if stack:
            if char == ')' and stack[-1] == '(':
                stack.pop()
                continue
            if char == '}' and stack[-1] == '{':
                stack.pop()
                continue
            if char == ']' and stack[-1] == '[':
                stack.pop()
                continue

        stack.append(char)

    return stack == []

def is_valid_2(s):
    stack = []

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if not matches(top, char):
                    return False

    return stack == []


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    print is_valid('()[]{}')
    print('\n')
    print is_valid('([)]')
    print('\n')
    print is_valid('{{([][])}()}')
    print('\n')
    print is_valid_2('{{([][])}()}')
    print('\n')
    print is_valid_1('()[]{}')
    print('\n')
    print is_valid_1('{{([][])}()}')
