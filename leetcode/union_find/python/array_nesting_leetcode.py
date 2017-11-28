"""
https://leetcode.com/problems/array-nesting/#/description

A zero-indexed array A consisting of N different integers is given. The array contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the size of the largest set S[K] for this array.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:
    1) N is an integer within the range [1, 20,000].

    2) The elements of A are all distinct.

    3) Each element of array A is an integer within the range [0, N-1].

solution: https://discuss.leetcode.com/topic/90542/java-solution-union-find

for each number, union index and number. Return value is the maximum members for each set representative.
"""
from disjoint_set import *

def array_nesting(nums):
    d = {}

    ds = DisjointSet()
    for num in nums:
        ds.make_set(num)

    for i, num in enumerate(nums):
        ds.union(i, num)

    maxmax = 0

    for num in nums:
        p = ds.find_set(num)
        d[p] = d.get(p, 0) + 1
        maxmax = max(maxmax, d.get(p))

    return maxmax

if __name__ == '__main__':
    print array_nesting([5,4,0,3,1,6,2])
