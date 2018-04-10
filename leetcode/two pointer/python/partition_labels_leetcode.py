"""
https://leetcode.com/problems/partition-labels/description/

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.

A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
    * S will have length in range [1, 500].
    * S will consist of lowercase letters ('a' to 'z') only.
"""
# https://leetcode.com/problems/partition-labels/discuss/113264/Easy-O(n)-Java-solution-using-sliding-window-(two-pointers)-comments-and-explanation-given
from collections import Counter
def partitionLabels(S):
    """
    O(n) time and space
    """
    result = []

    # for char in S:
    #     table[char] = table.get(char, 0) + 1
    table = Counter(S)

    i, j, l = 0, 0, len(S)
    counter, a_set = 0, set()

    while j < l:
        char = S[j]

        if char not in a_set:
            a_set.add(char)
            counter += 1

        table[char] -= 1

        if table[char] == 0:
            counter -= 1
            a_set.remove(char)

        if counter == 0:
            result.append(j - i + 1)
            i = j + 1

        j += 1

    return result


# https://leetcode.com/problems/partition-labels/solution/
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

# s = Solution().partitionLabels('ababcbacadefegdehijhklij')
s = partitionLabels('ababcbacadefegdehijhklij')
print s
