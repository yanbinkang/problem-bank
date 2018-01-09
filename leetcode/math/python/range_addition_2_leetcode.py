"""
https://leetcode.com/problems/range-addition-ii/#/description

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:

Input:
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation:
Initially, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:
    1) The range of m and n is [1,40000].
    2) The range of a is [1,m], and the range of b is [1,n].
    3) The range of operations size won't exceed 10,000.

Algorithm: when you take a critical look at the matrix after the updates have been done, you'll realize that the ops with min values for row and col will have the maximum integer. And the count will be row * col.

Special case line 44: when ops == [] there will be no updates and the maxinmum integer will be 0 and the count will be m * n

https://discuss.leetcode.com/topic/90547/java-solution-find-min
"""
def max_count(m, n, ops):
    if not ops: return m * n

    row, col = float('inf'), float('inf')

    for op in ops:
        row = min(row, op[0])
        col = min(col, op[1])

    return row * col

if __name__ == '__main__':
    print max_count(3, 3, [[2,2],[3,3]])
    print('\n')
    print max_count(26, 17,
                    [[20,10],[26,11],[2,11],
                    [4,16],[2,3],[23,13],[7,15],
                    [11,11],[25,13],[11,13],[13,11],
                    [13,16],[26,17]]
        )
