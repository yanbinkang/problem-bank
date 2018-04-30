"""
https://leetcode.com/problems/word-ladder/?tab=Description

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",

return its length 5.

Note:
Return 0 if there is no such transformation sequence.

All words have the same length.

All words contain only lowercase alphabetic characters.

You may assume no duplicates in the word list.

You may assume beginWord and endWord are non-empty and are not the same.
"""
import collections
from graph import *
def ladder_length(begin_word, end_word, word_list):
    d = collections.defaultdict(list)
    g = Graph()

    for word in word_list:
        # word = w[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]

            d[bucket].append(word)

    for bucket in d.keys():
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)

    return g

def dfs(g, start):
    start.set_distance(0)
    start.set_pred(None)

    vert_queue = []
    vert_queue.append(start)

    while vert_queue:
        current_vert = vert_queue.pop()

        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_pred(current_vert)
                vert_queue.insert(0, nbr)

        current_vert.set_color('black')


if __name__ == '__main__':
    g = ladder_length('hit', 'cog', ["hot","dot","dog","lot","log","cog"])

    print g.get_vertex('hot')
    print g.get_vertex('dot')
    print g.get_vertex('dog')
    print g.get_vertex('lot')
    print g.get_vertex('log')
    print g.get_vertex('cog')

    dfs(g, g.get_vertex('hot'))
