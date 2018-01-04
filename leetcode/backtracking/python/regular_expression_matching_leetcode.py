"""
https://leetcode.com/problems/regular-expression-matching/#/description

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch('aa','a') => false
isMatch('aa','aa') => true
isMatch('aaa','aa') => false
isMatch('aa', 'a*') => true
isMatch('aa', '.*') => true
isMatch('ab', '.*') => true
isMatch('aab', 'c*a*b') => true

Exponential time and space

ref: https://www.educative.io/collection/page/5642554087309312/5679846214598656/240003
"""

"""
special case for '*'

When a pattern is followed by a star '*' eg. b*, it means the pattern matches 0 or more of the preceeding char, in this case 'b'.

The strategy here is to continue matching the remaining text with the remaining pattern (but after the "*").

WHY?

Because '*' can match zero or more of the preceeding char. So we ask, what if its zero? Then follow that path.

If we're matching zero characters of the char preceeding the '*' then it means the character after the '*' should match the first character in the rest of the string.

If it does we return True.

If it doesn't we return False. This tells us that there is a char or more which might or mightn't match the char preceeding '*'.

Now we ask, what if '*' matches one or more of the preceeding char?

We then proceed to check if the first char in the rest of text matches the character before '*'.

So we do this by running:

        if pattern[j] != '.' and text[k] != pattern[j]:
                return False


If it doesn't return False, because according to the rule in the pattern, we're supposed to match at least 0 or more of the preceeding char.


If it does, keep checking the next char in the rest of the text against the character after '*'
"""

def is_match(s, p):
    return is_match_rec(s, p, 0, 0)

def is_match_rec(text, pattern, i, j):
    # base case. we're at end of both text and pattern
    if len(text) == i and len(pattern) == j:
        return True

    """
    special case for '*'

    Note on loop condition: because we're checking for pattern[j + 1] we need to make sure j < len(pattern) - 1

    we can also do:

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
    """
    if j < len(pattern) - 1 and pattern[j + 1] == '*':
        for k in range(i, len(text) + 1):
            # recursively match the char after * in the pattern with the rest of the text
            if is_match_rec(text, pattern, k, j + 2):
                return True

            """
            text is shorter than pattern, return False. Eg: ('a', 'ab*a'). In the first recursion 'a' matches 'a'. hence i = 1 and j = 1. In the next iteration, after the for loop k will be greater than or equal to len(text). There is nothing to match. return False
            """
            if k >= len(text):
                return False

            if pattern[j] != '.' and text[k] != pattern[j]:
                return False

    # case of '.' or when char in patter and text match. see if remaining pattern and text also match
    elif i < len(text) and\
             j < len(pattern) and \
                (pattern[j] == '.' or pattern[j] == text[i]):
            return is_match_rec(text, pattern, i + 1, j + 1)

    return False

if __name__ == '__main__':
    print is_match('a', 'a*')
    print('\n')
    print is_match('a', 'ab*a')
    print('\n')
    print is_match('xaabyc', 'xa*b.c')
    print('\n')
    print is_match('', 'a*')
    print('\n')
    print is_match('ab', '.*')
    print('\n')
    print is_match('aa', '.*')
    print('\n')
    print is_match('aa', 'a*')
    print('\n')
    print is_match('aa', 'a')
    print('\n')
    print is_match('facbbc', '.ab*c')
