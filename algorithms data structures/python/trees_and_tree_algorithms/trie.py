"""
https://leetcode.com/problems/implement-trie-prefix-tree/

https://youtu.be/AXjmTQ8LEoI

Insert: O(l x n) time. where l is the average length of the word, n is total number of words

search: O(l) where l is length of the word

delete: O(l x n) time. where l is the average length of the word, n is total number of words

Note: Delete is not part of leetcode interface
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

        for char in word:
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
        for char in word:
            node = current.children.get(char)

            if node is None:
                return False

            current = node

        return current.end_of_word

    def search_recursive(self, word):
        return self.search_recursive_util(self.root, word, 0)

    def search_recursive_util(self, current, word, index):
        if index == len(word):
            return current.end_of_word

        char = word[index]

        node = current.children.get(char)

        if node is None:
            return False

        return self.search_recursive_util(node, word, index + 1)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            node = current.children.get(char)

            if node is None:
                return False

            current = node

        return True

    # not part of leetcode interface
    def delete(self, word):
        self.delete_util(self.root, word, 0)

    def delete_util(self, current, word, index):
        if index == len(word):
            # when end of word is reached only delete if currrent.end_of_word is true
            if not current.end_of_word:
                return False

            current.end_of_word = False

            # if current has no other mapping then return true
            return len(current.children) == 0

        char = word[index]
        node = current.children.get(char)
        if node is None:
            return False

        should_delete_util_current_node = self.delete_util(node, word, index + 1)

        # if true is returned then delete the mapping of character and trienode reference from map.
        if should_delete_util_current_node:
            del current.children[char]

            # return true if no mappings are left in the map.
            return len(current.children) == 0

        return False




if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert('abc')
    trie.insert('lmn')
    print trie.search('abc')
    print trie.startsWith('lm')
    print trie.startsWith('z')

    print('\n')

    t = Trie()
    states = """
            Alabama
            Alaska
            Arizona
            Arkansas
            California
            Colorado
            Connecticut
            Delaware
            Florida
            Georgia
            Hawaii
            Idaho
            Illinois
            Indiana
            Iowa
            Kansas
            Kentucky
            Louisiana
            Maine
            Maryland
            Massachusetts
            Michigan
            Minnesota
            Mississippi
            Missouri
            Montana
            Nebraska
            Nevada
            New Hampshire
            New Jersey
            New Mexico
            New York
            North Carolina
            North Dakota
            Ohio
            Oklahoma
            Oregon
            Pennsylvania
            Rhode Island
            South Carolina
            South Dakota
            Tennessee
            Texas
            Utah
            Vermont
            Virginia
            Washington
            West Virginia
            Wisconsin
            Wyoming"""
    states_list = [w.strip().lower() for w in states.splitlines() if w]
    for state in states_list:
        t.insert(state)
    print t.startsWith("new")
    print t.search("tah")
