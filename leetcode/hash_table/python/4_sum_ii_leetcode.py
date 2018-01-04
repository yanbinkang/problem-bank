"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

# https://discuss.leetcode.com/topic/67593/clean-java-solution-o-n-2
def four_sum_count(A, B, C, D):
    d = {}

    for i in range(len(C)):
        for j in range(len(D)):
            total = C[i] + D[j]
            d[total] = d.get(total, 0) + 1

    result = 0

    for i in range(len(A)):
        for j in range(len(B)):
            result += d.get(-1 * (A[i] +B[j]), 0)

    return result

# https://discuss.leetcode.com/topic/67659/easy-2-lines-o-n-2-python
import collections
def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)

if __name__ == '__main__':
    print four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])
