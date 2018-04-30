"""
https://leetcode.com/problems/word-ladder-ii/description/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:
 - Return an empty list if there is no such transformation sequence.

 - All words have the same length.

 - All words contain only lowercase alphabetic characters.

 - You may assume no duplicates in the word list.

 - You may assume beginWord and endWord are non-empty and are not the same.

 solution: https://discuss.leetcode.com/topic/67637/python-iterative-solution-based-on-lc127-use-dict-to-store-neighbours

 algo:
 1) create buckets of words that differ by one letter call this dict_words. Sample: { '_ot': ['hot', 'dot', 'lot'] }

 2) set current to [[beginWord]] and initialize result to empty list

 3) while result list is empty do this:
    a) Iterate over all the lists in current

    b) set word to the last element in the above step

    c) generate the buckets (called key key) in the above word. sample = '_ot'. If the bucket is in  dict_words, iterate over all the elements in this bucket (called target) append (words + [target]) to new_words if target is not equal to word in above step.

    NOTE: words + [target] generates a new list. words is already a list!

    d) if the target == endWord append (words + [target]) to result

    e) append buckets (key) in the above step which are still in dict_words to key's list

    f) after the first step is complete, delete the keys added in the above step from dict_words since we've already seen them.

    g) set current to new_words and go through the process again

    h) Finally return result
"""
def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList: return []

    # wordList.append(endWord)

    dict_words = construct_dict(wordList)

    current = [[beginWord]]
    result = []

    while not result:
        if not current: break

        new_words = []
        keys = [] # delete keys after searching

        for words in current:
            word = words[-1]

            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                if key in dict_words:
                    for target in dict_words[key]:
                        if word != target:
                            new_words.append(words + [target])

                            if target == endWord:
                                result.append(words + [target])

                    # append key for later deletion if key in dict_words
                    keys.append(key)

        for key in keys:
            dict_words.pop(key, None)
        current = new_words

    return result

def construct_dict(wordList):
    d = {}

    for word in wordList:
        for i in range(len(word)):
            key = word[:i] + '_' + word[i + 1:]
            d[key] = d.get(key, []) + [word]

    return d


if __name__ == '__main__':
    print findLadders('hit', 'cog', ['hot','dot','dog','lot','log','cog'])
