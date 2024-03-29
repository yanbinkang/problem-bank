"""
https://leetcode.com/problems/most-common-word/description/

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.


Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Note:

* 1 <= paragraph.length <= 1000.
* 1 <= banned.length <= 100.
* 1 <= banned[i].length <= 10.
* The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
* paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
Different words in paragraph are always separated by a space.
* There are no hyphens or hyphenated words.
* Words only consist of letters, never apostrophes or other punctuation symbols.

similar to:
    https://leetcode.com/problems/top-k-frequent-elements/
    https://leetcode.com/problems/top-k-frequent-words/description/
    https://leetcode.com/problems/sort-characters-by-frequency/
"""
def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    result, d = [], {}
    s = ''.join([char.lower() for char in paragraph if char not in "!?',;."]).split()

    for word in s:
        if word not in banned:
            d[word] = d.get(word, 0) + 1

    bucket = [None for i in range(len(s) + 1)]

    for key, val in d.items():
        if bucket[val] == None:
            bucket[val] = []
        bucket[val].append(key)

    for i in reversed(range(len(bucket))):
        if bucket[i] is not None:
            result += bucket[i]

    return result[0]

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print mostCommonWord(paragraph, banned)
