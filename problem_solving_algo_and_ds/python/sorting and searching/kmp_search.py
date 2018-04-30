"""
Knuth Morris Pratt Search
Excellent explanation here:
http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
"""

def search(string, word):
    word_length = len(word)
    string_length = len(string)
    offsets = []

    if word_length > string_length:
        return offsets

    prefix = compute_prefix(word)

    i = 0
    j = 0

    while j < string_length:
        while i > 0 and word[i] != string[j]:
            i = prefix[i - 1]

        if word[i] == string[j]:
            i += 1

        if i == word_length:
            offsets.append(j - word_length + 1)
            i = prefix[i - 1]

        j += 1

    return offsets


def compute_prefix(word):
    word_length = len(word)
    prefix = [0] * word_length

    i = 0
    j = 1

    while j < word_length:
        while i > 0 and word[i] != word[j]:
            i = prefix[i - 1]

        if word[i + 1] == word[j]:
            i += 1

        prefix[j] = i

        j += 1

    return prefix


print search("ABC ABCDAB ABCDABCDABDE", "ABCDAB")
print search("aaaab", "aab")
