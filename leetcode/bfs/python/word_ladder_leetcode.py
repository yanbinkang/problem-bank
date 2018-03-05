"""
https://leetcode.com/problems/word-ladder/description/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    1. Only one letter can be changed at a time.
    2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

For example,

Given:

beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
- Return 0 if there is no such transformation sequence.

- All words have the same length.

- All words contain only lowercase alphabetic characters.

- You may assume no duplicates in the word list.

- You may assume beginWord and endWord are non-empty and are not the same.
"""

"""
Algorithm:

1. Using a dictionary, put the words that differ by one letter into a bucket. Eg.

 "_ot" -> ["hot",  "dot",  "lot"]

 meaning "hot", "dot" and "lot" are possible words that we can teansform by changing only one letter!

 2. Create a queue and add beginWord and 1 (being the length of the transformation) to queue.

 3. Create a visited set and add beginWord to the set - meaning we've seen beginWord

        queue, visited = [(beginWord, 1)], set()

 4. While the queue is not empty

    a. pop the back of the queue. this will yield a word and its transformation length

    b. Find all combinations of buckets from this word. If this bucket is already stored in the dictionary, get all the words stored under this bucket.

    Remember, all the words under this bucket differ by only one letter!

    c. For each word in the bucket, if the word is not in the visited set (we've not processed this word), add it to the set. Then insert the word and the length of the new transformation to the front of the queue.

    This means from one word, we've been able to find another word that required us to change only one letter.

    d. If at any point in this process we find a word that's the same as endWord we retrun length + 1. Why length + 1? Because the current length is assocaited with the previous word in the transformation. Since we've found a new word that we care about and its also the same as endWord, we add 1 to change the length of the transformation.

5. Go back to the queue, if its not empty repeat step 4.

6. When the queue gets empty and we've not reached endWord, return 0.

Visualize ladder using example in question:

"hit"

====

"hit" -> "hot"

=======

"hit" -> "hot" -> "dot"

"hit" -> "hot" -> "lot"


=============

"hit" -> "hot" -> "dot" -> "dog"

"hit" -> "hot" -> "lot" -> "log"

===================

"hit" -> "hot" -> "dot" -> "dog" - "cog"
"""
# import collections
# https://discuss.leetcode.com/topic/43246/simple-to-understand-python-solution-using-list-preprocessing-and-bfs-beats-95
def word_ladder_length(beginWord, endWord, wordList):
    dict_words = construct_dict(wordList)

    # print dict_words

    return bfs(beginWord, endWord, dict_words)


def bfs(beginWord, endWord, dict_words):
    queue, visited = [(beginWord, 1)], set()
    # queue, visited = collections.deque( [[beginWord, 1]] ), set()

    visited.add(beginWord)

    while queue:
        # word, length = queue.popleft()
        word, length = queue.pop()


        for i in range(len(word)):
            s = word[:i] + '_' + word[i+1:]
            nbr_words = dict_words.get(s, [])

            for nbr in nbr_words:
                if nbr not in visited:

                    if nbr == endWord:
                        return length + 1

                    visited.add(nbr)

                    # queue.append( [nbr, length + 1] )
                    queue.insert( 0, (nbr, length + 1) )

    return 0

def construct_dict(wordList):
    d = {}

    # create buckets of words that differ by one letter
    for word in wordList:
        for i in range(len(word)):
            s = word[:i] + '_' + word[i + 1:]
            d[s] = d.get(s, []) + [word]

    return d


if __name__ == '__main__':
    print word_ladder_length('hit', 'cog', ['hot','dot','dog','lot','log','cog'])
    # "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    print('\n')
    print word_ladder_length('fool', 'sage', ['pool', 'poll', 'pole', 'pale', 'sale', 'sage', 'cage'])
    # "fool" -> "pool" -> "poll" -> "pole" -> "pale" -> "sale" -> "sage"

