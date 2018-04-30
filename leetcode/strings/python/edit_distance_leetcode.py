"""
https://leetcode.com/problems/edit-distance/#/description

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
def min_distance(word1, word2):
    # degenerate cases
    if word1 == word2:
        return 0

    if len(word1) == 0:
        return len(word2)

    if len(word2) == 0:
        return len(word1)

    # create two arrays of integer distances
    d1, d2 = [0] * (len(word2) + 1), [0] * (len(word2) + 1)

    for i in range(len(word2) + 1):
        d1[i] = i

    for i in range(len(word1)):
        d2[0] =  i + 1

        for j in range(len(word2)):
            if word1[i] == word2[j]:
                count = 0
            else:
                cost = 1

            d2[j + 1] = min(d2[j] + 1, d1[j + 1] + 1, d1[j] + cost)

        for j in range(len(word2) + 1):
            d1[j] = d2[j]

    return d2[len(word2)]


if __name__ == '__main__':
    print min_distance('kitten', 'sitting')
