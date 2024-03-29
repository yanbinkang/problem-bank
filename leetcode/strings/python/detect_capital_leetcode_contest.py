"""
https://leetcode.com/problems/detect-capital/#/description

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".

2. All letters in this word are not capitals, like "leetcode".

3. Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
def detect_capital_use(word):
    num_upper = 0

    for i in range(len(word)):
        if word[i].isupper():
            num_upper += 1

    # all letters are not capital or all letters are capital
    if num_upper == 0 or num_upper == len(word): return True

    # only one letter is capital therefore check if the first letter is capital
    if num_upper == 1:
        return word[0].isupper()

    return False

def detect_capital_use_1(word):
    return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    print detect_capital_use('USA')
    print('\n')
    print detect_capital_use('leetcode')
    print('\n')
    print detect_capital_use('FlaG')

