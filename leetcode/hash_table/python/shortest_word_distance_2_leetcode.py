"""
https://leetcode.com/problems/shortest-word-distance-ii/?tab=Description

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

https://discuss.leetcode.com/topic/20643/java-solution-using-hashmap

O(n) time, O(m + n) space for shortest()
"""
import collections
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.d[word].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.d[word1], self.d[word2]
        min_distance = float('inf')
        i = j = 0

        # because the elements in l1, l2 will be sorted we can use idea of merge sort here and perform comparision in O(m + n)
        while i < len(l1) and j < len(l2):
            min_distance = min(min_distance, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1

        return min_distance

if __name__ == '__main__':
    # Your WordDistance object will be instantiated and called as such:
    obj = WordDistance(['practice', 'makes', 'perfect', 'coding', 'makes'])
    param_1 = obj.shortest('makes', 'coding')

    print param_1
