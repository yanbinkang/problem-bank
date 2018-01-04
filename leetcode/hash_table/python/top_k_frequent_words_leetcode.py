"""
https://leetcode.com/problems/top-k-frequent-words/description/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
    1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    2. Input words contain only lowercase letters.

Follow up:

    1. Try to solve it in O(n log k) time and O(n) extra space.
    2. Can you solve it in O(n) time with only O(k) extra space?

similar to: https://leetcode.com/problems/top-k-frequent-elements/
"""
def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    bucket = [None for i in range(len(words) + 1)]
    d = {}

    for word in words:
        d[word] = d.get(word, 0) + 1

    for key, frequency in d.items():
        if bucket[frequency] is None:
            bucket[frequency] = []

        bucket[frequency].append(key)

    result = []

    for i in reversed(range(len(bucket))):
        if bucket[i] and len(result) < k:
                temp = sorted(bucket[i])
                result.extend( temp )

    return result[:k]
