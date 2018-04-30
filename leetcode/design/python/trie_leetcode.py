"""
https://leetcode.com/problems/implement-trie-prefix-tree/

https://youtu.be/AXjmTQ8LEoI

O(l x n) time. where l is the average length of the word, n is total number of words
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.end_of_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root

        for i in range(len(word)):
            char = word[i]
            node = current.children.get(char)

            if node is None:
                node = TrieNode()
                current.children[char] = node
            current = node

        current.end_of_word = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in range(len(word)):
            char = word[i]
            node = current.children.get(char)

            if node is None:
                return False

            current = node

        return current.end_of_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            node = current.children.get(char)

            if node is None:
                return False

            current = node

        return True



# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert('abc')
# trie.search("key")
