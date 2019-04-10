'''
https://leetcode.com/problems/find-common-characters/description/

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

    1. 1 <= A.length <= 100
    2. 1 <= A[i].length <= 100
    3. A[i][j] is a lowercase letter

ref: https://leetcode.com/problems/find-common-characters/discuss/247592/Java-Straight-Forward
'''


def common_chars1(A):
    global_store = {}

    result = []

    for word in A:
        temp = {}

        for char in word:
            temp[char] = temp.get(char, 0) + 1


def common_chars(A):
    result = []

    global_histogram = [float('inf')] * 26

    for word in A:
        temp = [0] * 26

        for char in word:
            # convert char to integer between 1 - 26
            temp[ord(char) - ord('a')] += 1

        for j in range(26):
            # We're using min because we only care about
            # minimum number of chars that chow up in all strings
            global_histogram[j] = min(global_histogram[j], temp[j])

    for i, val in enumerate(global_histogram):
        for j in range(val):
            # convert integer to string
            result.append(chr(i + ord('a')))

    # for i in range(len(vals)):
    #     for j in range(vals[i]):
    #         result.append(chr(i + ord('a')))

    return result


from collections import Counter


def commonChars(A):
    res = Counter(A[0])
    for a in A:
        res &= Counter(a)
    return list(res.elements())


if __name__ == "__main__":
    print(common_chars(["bella", "label", "roller"]))
