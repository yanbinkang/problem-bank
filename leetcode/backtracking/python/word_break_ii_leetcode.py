"""
https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
def word_break(string, dictionary):
    if not string or not dictionary:
        return []

    hash_map = {}
    max_length = len(max(dictionary, key=len))
    return word_break_helper(string, dictionary,
                            0, max_length,
                            hash_map)

def word_break_helper(string, dictionary, start, max_length, hash_map):
    if start == len(string):
        return ['']

    if start in hash_map:
        return hash_map[start]

    words = []
    for i in range(start, start + max_length):
        if i < len(string):
            new_word = string[start: i + 1]
            if new_word not in dictionary:
                continue
            sub_words = word_break_helper(string,
                                        dictionary, i + 1,
                                        max_length,
                                        hash_map)
            for word in sub_words:
                extra_space = '' if len(word) == 0 else ' '
                words.append(new_word + extra_space + word)

    hash_map[start] = words
    return words


if __name__ == '__main__':
    dictionary = {"cat", "cats", "and", "sand", "dog"}
    s = "catsanddog"
    print word_break(s, dictionary)
    print('\n')
    print word_break(s, {})
