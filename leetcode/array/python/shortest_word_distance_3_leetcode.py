"""
https://leetcode.com/problems/shortest-word-distance-iii/

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = 'makes', word2 = 'coding', return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
def shortest_word_distance(words, word1, word2):
    idx1, idx2, min_distance = -1, -1, float('inf')

    for i, word in enumerate(words):
        if word == word1:
            idx1 = i

        # if the words are the same, it means idx1 has already been updated in first if statement. Update idx1 with current idx2 before updating idx2 to new index

        if word == word2:
            if word1 == word2:
                idx1 = idx2
            idx2 = i

        # OLD CODE
        # if word == word2 and word1 == word2:
        #     idx1 = idx2
        #     idx2 = i

        # if word == word2:
        #     idx2 = i

        if idx1 != -1 and idx2 != -1:
            min_distance = min(min_distance, abs(idx1 - idx2))

    return min_distance

if __name__ == '__main__':
    print shortest_word_distance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding')
    print('\n')
    print shortest_word_distance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes')
    print('\n')
    print shortest_word_distance(['a', 'b'], 'a', 'b')
