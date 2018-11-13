"""
https://leetcode.com/problems/reverse-words-in-a-string-ii/#/description

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

algorithm: First reverse the whole string, then reverse each word.

O(n) time O(1) space

https://discuss.leetcode.com/topic/8366/my-java-solution-with-explanation

algo:
    1) reverse the whole sentence

    2) then reverse the individual words in the sentence

DO YOU UNDERSTAND WHY WE HAVE TO DO:
    for i in range(len(s) + 1):
        pass

Because we have to reverse the last word in the sentence, we need to go to the actual length of the sentence so we can reverse by using:
    reverse_char(s, index, i - 1) where i is the length of the input
"""
def reverse_words(s):
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    reverse_char(s, 0, len(s) - 1)

    index = 0

    for i in range(len(s) + 1):
        # need the conditions to be in this particular order to avoid IndexError. note we are iterating to (len(s) + 1) so if s[i] == ' ' appears first and we get to the last index we'll get IndexError.
        if  i == len(s) or s[i] == ' ':
            reverse_char(s, index, i - 1)
            index = i + 1

def reverse_char(s, first, last):
    while first <= last:
        temp = s[first]
        s[first] = s[last]
        s[last] = temp

        first += 1
        last -= 1

if __name__ == '__main__':
    s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
    print 'string before reverse is: %s' % ''.join(s)
    reverse_words(s)
    print 'string after reverse is: %s' % ''.join(s)
