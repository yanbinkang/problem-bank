"""
https://leetcode.com/problems/reverse-words-in-a-string/#/description

Given an input string, reverse the string word by word.

For example,

Given s = "the sky is blue",

return "blue is sky the".

Clarification:
    - What constitutes a word?
      A sequence of non-space characters constitutes a word.

    - Could the input string contain leading or trailing spaces?
      Yes. However, your reversed string should not contain leading or trailing spaces.

    - How about multiple spaces between two words?
      Reduce them to a single space in the reversed string.

O(n) time O(n) space

Note: In python str.split() handles whitespcae trimming and runs of consecutive whitespace in the string.
"""
def reverse_words(s):
    s = s.split()

    reverse_chars(s, 0, len(s) - 1)

    return ' '.join(s)

def reverse_chars(s, first, last):
    while first <= last:
        temp = s[first]
        s[first] = s[last]
        s[last] = temp

        first += 1
        last -= 1

# https://discuss.leetcode.com/topic/5909/my-accept-answer-of-python-with-one-line
def reverse_words_1(s):
    return " ".join(s.split()[::-1])

def reverse_words_2(s):
    if not s: return

    a = list(s)
    n = len(s)

    # step 1. reverse the whole string
    reverse_chars(a, 0, n - 1)

    # step 2. reverse each word
    rev_words(a, n)

    # step 3. clean up spaces
    return clean_spaces(a, n)

def rev_words(a, n):
    i = 0
    j = 0

    while i <= n:
        # this line is very important. reverse the order and you'll get an IndexError
        if i == n or a[i] == ' ':
            reverse_chars(a, j, i - 1)
            j = i + 1

        i += 1

def clean_spaces(a, n):
    i, j = 0, 0

    while j < n:
        while j < n and a[j] == ' ':
            j += 1

        while j < n and a[j] != ' ':
            a[i] = a[j]
            i += 1
            j += 1

        while j < n and a[j] == ' ':
            j += 1

        if j < n:
            a[i] = ' '
            i += 1

    return ''.join(a)

if __name__ == '__main__':
    print reverse_words(' the sky is blue')
    print('\n')
    print reverse_words('   a   b ')
    print('\n')
    print reverse_words('hi!')
    print('\n')
    print reverse_words('a b')
    print('\n')
    print reverse_words_2(' the sky is blue')
    print('\n')
    print reverse_words_2('   a   b ')
