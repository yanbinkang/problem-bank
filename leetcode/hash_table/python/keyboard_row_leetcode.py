"""
https://leetcode.com/problems/keyboard-row/

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
    1. You may use one character in the keyboard more than once.
    2. You may assume the input string will only contain letters of alphabet.
"""
def find_words(words):
    keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']

    result = []

    for letters in keyboard:
        for word in words:
            length = len(word)
            for i, char in enumerate(word):
                if char.lower() not in letters:
                    break
                if char.lower() in letters and i == length - 1:
                    result.append(word)

    return result

if __name__ == '__main__':
    print find_words(["Hello", "Alaska", "Dad", "Peace"]) # ["Alaska", "Dad"]
