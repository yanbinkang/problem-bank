"""
https://leetcode.com/problems/valid-palindrome/?tab=Description

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
# O(n) time and space
import string
def is_palindrome(s):
    deque = []

    for char in s:
        if char == ' ':
            continue

        # string.punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        if char not in string.punctuation:
            deque.append(char.lower())

    first, last = 0, len(deque) - 1

    while first <= last:
        if deque[first] != deque[last]:
            return False

        first += 1
        last -= 1

    return True

"""
str.isalnum()

Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
"""
# O(n * 2k) ==> O(n) time O(1) space
def is_palindrome_1(s):
    l, r = 0, len(s) - 1

    while l < r: # O(n)
        while l < r and not s[l].isalnum(): # O(k) k is number of non alnum
            l += 1

        while l < r and not s[r].isalnum(): # O(k) k is number of non alnum
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

# O(n) time O(1) space
def is_palindrome_2(s):
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1

    return True


if __name__ == '__main__':
    print is_palindrome("A man, a plan, a canal: Panama")
    print is_palindrome("race a car")
    print('\n')
    print is_palindrome_1("A man, a plan, a canal: Panama")
    print is_palindrome_1("race a car")
    print('\n')
    print is_palindrome_2("A man, a plan, a canal: Panama")
    print is_palindrome_2("race a car")
