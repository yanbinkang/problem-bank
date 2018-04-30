"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

algo: first sort the array and then simply compare the first and last elements in the sorted array. After the array is sorted, if there is a common prefix the first and last array will have it. i.e after sorting the first string and last string have the shortest common prefix, if there is one!

Time complexity: Comparison between two strings is O(k) where k is the average length of the two strings.

Sorting iis O(NlogN)

so complexity is O(NlogN) * k
"""
def longest_common_prefix_1(strs):
    result = ''

    if strs and len(strs) > 0:
        strs.sort()

        a = strs[0]

        b = strs[-1]

        for i in range(len(a)):
            if a[i] == b[i]:
                result += a[i]
            else:
                return result

    return result


def longest_common_prefix(strs):
    if len(strs) == 0: return ''

    prefix = strs[0]

    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0: len(prefix) - 1]
            if not prefix:
                return ''

    return prefix

if __name__ == '__main__':
    print longest_common_prefix(["abab","aba",""])
    print longest_common_prefix(["c","acc","ccc"])
    print longest_common_prefix(['aa', 'aa'])
    print longest_common_prefix(['a', 'a', 'b'])
    print('\n')
    print longest_common_prefix_1(['aa', 'aa'])

