"""
https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:

    1. All the given strings' lengths will not exceed 10.
    2. The length of the given list will be in the range of [2, 50].
"""
# ref: https://leetcode.com/problems/longest-uncommon-subsequence-ii/solution/#approach-3-sorting-and-checking-subsequence-accepted
"""
By some analysis, we can note that if longest uncommon subsequence is there, then it will always be one of the string from the given list of strings.

Using this idea, we can check each string that whether it is a subsequence of any other string. If a string is not a subsequence of any other string i.e. it is uncommon , we will return maximum length string out of them. If no string found, we will return -1.
"""
def find_LUS_length_1(strs):
    result = -1

    for i in range(len(strs)):
        for j in range(len(strs)):
            if i == j:
                continue

            if is_subsequence_1(strs[i], strs[j]):
                break

        if j == len(strs):
            result = max(result, len(strs[i]))

    return result

"""
In the last approach, we needed to compare all the given strings and compare them for the subsequence criteria. We can save some computations if we sort the given set of strings based on their lengths initially.

In this approach, firstly we sort the given strings in decreasing order of their lengths. Then, we start off by comparing the longest string with all the other strings. If none of the other strings happens to be the subsequence of the longest string, we return the length of the longest string as the result without any need of further comparisons. If some string happens to be a subsequence of the longest string, we continue the same process by choosing the second largest string as the first string and repeat the process, and so on.
"""
def find_LUS_length_1(strs):
    strs.sort(key = len, reverse =  True)

    for i in range(len(strs)):
        flag = True
        for j in range(len(strs)):
            if i == j:
                continue

            if is_subsequence(strs[i], strs[j]):
                flag = False
                break
        if flag:
            return len(strs[i])

    return -1

def is_subsequence_1(x, y):
    if len(x) > len(y):
        return False

    i = 0

    for j in range(len(y)):
        if i < len(x) and x[i] == y[j]:
            i += 1

    return i == len(x)

# ref: https://discuss.leetcode.com/topic/85044/python-simple-explanation/2
def is_subsequence_2(x, y):
    # True of x is a subsequence of y
    i = 0

    for c in y:
        if i < len(x) and x[i] == c:
            i += 1

    return i == len(x)

def is_subsequence(s, t):
    if len(s) > len(t): return False

    t = iter(t)
    return all(c in t for c in s)


def find_LUS_length(strs):
    for s in sorted(strs, key=len, reverse=True):
        if sum(is_subsequence(s, t) for t in strs) == 1:
            return len(s)

    return -1


def find_LUS_length_2(strs):
    strs.sort(key = len, reverse = True)

    for i, word1 in enumerate(strs):
        if all(not is_subsequence_2(word1, word2)
                for j, word2 in enumerate(strs) if i != j):
                    return len(word1)

    return -1


if __name__ == '__main__':
    print find_LUS_length(['aba','cdc','eae'])
    print find_LUS_length(['aaa', 'aaa', 'aa'])
    print('\n')
    print find_LUS_length_1(['aba','cdc','eae'])
    print find_LUS_length_1(['aaa', 'aaa', 'aa'])
