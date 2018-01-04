"""
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z

refer to word_search for algo.

Difference between this and original word_search:
    1. This one searches for multiple words so we'll have to iterate throuhg all the words and then run the word_search algo. THIS TAKES TOO MUCH TIME!

    2. Using a Trie helps make the search for words faster. So build insert words into Trie and then search.
"""
from trie import Trie

def find_words(board, words):
    result = []

    trie = Trie()

    for word in words:
        trie.insert(word)

    node = trie.root

    for i in range(len(board)):
        for j in range(len(board[0])):
            find(board, i, j, node, '', result)

    return result

def find(board, i, j, node, string, result):
    if node.end_of_word:
        result.append(string)

        # mark false as we've already seen end of word as per the if condition
        """
        eg. ['o', F] -> ['a', F] -> ['t', F] -> ['h' , F] -> ['', T]

        given above node, after 'oath' has been found we need to make the last node's end_of_word to False. ['', T] => ['', F].

        This is because:
            a. we'll continue to search the adjacent cells to see if we can match another word
            b. we'll continue to pass the last node into the recursion and if its end_of_word is still True 'oath' is gonna be added to result mutilple times.

        IF we don't do this and 'oath' is added multiple times to the result we'll have to do list(set(result)) to get the correct answer!
        """
        node.end_of_word = False

    if i < 0 or i >= len(board) or\
       j < 0 or j >= len(board[0]) or\
       node.children.get(board[i][j]) is None:
            return

    temp = board[i][j]
    board[i][j] = '#'

    node = node.children.get(temp)

    find(board, i + 1, j, node, string + temp, result)
    find(board, i - 1, j, node, string + temp, result)
    find(board, i, j + 1, node, string + temp, result)
    find(board, i, j - 1, node, string + temp, result)

    board[i][j] = temp



def find_words_alt(board, words):
    trie = {}

    for word in words:
        t = trie

        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'

    result = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            helper(board, i, j, trie, '', result)

    return list(set(result))

def helper(board, i, j, trie, string, result):
    if '#' in trie: # end of word
        result.append(string)

    if i < 0 or i >= len(board) or\
       j < 0 or j >= len(board[0]) or\
       board[i][j] not in trie:
            return

    temp = board[i][j]
    board[i][j] = '@'

    helper(board, i + 1, j, trie[temp], string + temp, result)
    helper(board, i - 1, j, trie[temp], string + temp, result)
    helper(board, i, j + 1, trie[temp], string + temp, result)
    helper(board, i, j - 1, trie[temp], string + temp, result)

    board[i][j] = temp


if __name__ == '__main__':
    board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]

    words = ['oath','pea','eat','rain']

    print find_words_alt(board, words)

    print find_words(board, words)
