"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

- All the strings in the input will only contain lowercase letters.
- The length of words will be in the range [1, 1000].
- The length of words[i] will be in the range [1, 30].

ref: https://discuss.leetcode.com/topic/109626/simple-short-7-lines-python-solution-using-sorting-and-set

algo: sort the words and iterate through it.
If length of word is 1 just add it to result. Or if prefix of word already in set add the word. Eg. if current word is 'wo' and 'w' already in set, we just add 'wo' to set.

Finally return, sort the set and return the word with max word length.
"""
def longest_word(words):
    valids = set()

    for word in sorted(words):
        if len(word) == 1 or word[:-1] in valids:
            valids.add(word)

    return max(sorted(valids), key=len) if valids else ''

if __name__ == '__main__':
    print longest_word(["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"])
    print('\n')
    print longest_word(["w","wo","wor","worl", "world"])

