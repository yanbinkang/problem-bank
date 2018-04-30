"""
https://leetcode.com/problems/shortest-word-distance/

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = 'coding', word2 = 'practice', return 3.
Given word1 = 'makes', word2 = 'coding', return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

https://discuss.leetcode.com/topic/20668/ac-java-clean-solution
"""
import collections

def shorted_distance(words, word1, word2):
    p1, p2, min_distance = -1, -1, float('inf')

    for i, word in enumerate(words):
        if word == word1:
            p1 = i

        if word == word2:
            p2 = i

        if p1 != -1 and p2 != -1:
            min_distance = min(min_distance, abs(p1 - p2))

    return min_distance



# brute force
def shorted_distance_1(words, word1, word2):
    d = collections.defaultdict(list)

    result = []

    for i, word in enumerate(words):
        d[word].append(i)

    word1_indexes = d[word1]
    word2_indexes = d[word2]

    for i in word1_indexes:
        for j in word2_indexes:
            result.append(abs(i - j))

    return min(result)

if __name__ == '__main__':
    print shorted_distance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice')
    print shorted_distance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding')

    print('\n')

    print shorted_distance_1(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice')

    print shorted_distance_1(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding')


