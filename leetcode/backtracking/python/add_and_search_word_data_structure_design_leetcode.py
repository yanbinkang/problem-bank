"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z

https://jeantimex.gitbooks.io/solve-leetcode-problems/content/problems/Add%20and%20Search%20Word%20-%20Data%20structure%20design.html
"""
import string

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Trie()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.root.insert(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.root.search(word)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            node = current.children.get(char)

            if node is None:
                node = TrieNode()
                current.children[char] = node

            current = node
        current.end_of_word = True

    def search(self, word):
        return self.search_helper(self.root, word, 0)

    def search_helper(self, node, word, index):
        if node is None or index == len(word) and not node.end_of_word:
            return False

        if index == len(word) and node.end_of_word:
            return True

        char = word[index]

        if char == '.':
            for i in string.lowercase:
                if self.search_helper(node.children.get(i), word, index + 1):
                    return True
            return False
        else:
            return self.search_helper(node.children.get(char), word, index + 1)

if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    wordDictionary = WordDictionary()
    wordDictionary.addWord('ab')
    print wordDictionary.search('a.')
