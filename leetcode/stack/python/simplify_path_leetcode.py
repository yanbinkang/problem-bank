"""
https://leetcode.com/problems/simplify-path/description/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

algorithm:
ref: https://discuss.leetcode.com/topic/28240/9-lines-of-python-code/6

1. Use a stack

2. split the given path by '/' and iterate through the tokens

3. If token is '..', meaning we have to go to the parent directory, check if the stack is not empty. If this is True pop the last item from the stack

4. If the token is not an empty string and token is not equal to '.' - meaning we're staying in the same directory - append the token to the stack.

5. Finally return '/' concatenated with '/' joined with the items in the stack.

        return '/' + '/'.join(stack)
"""


def simplify_path(path):
    stack = []

    for p in path.split('/'):
        if p == '..':
            if stack:
                stack.pop()
        elif p and p != '.':
            stack.append(p)

    return '/' + '/'.join(stack)


if __name__ == '__main__':
    print simplify_path('/a/./b/../../c/')
    print('\n')
    print simplify_path('/home/')
