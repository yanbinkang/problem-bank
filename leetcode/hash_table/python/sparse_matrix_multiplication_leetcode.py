"""
https://leetcode.com/problems/sparse-matrix-multiplication/#/description

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

algo: The idea is, for each row in A, take the ith element in that row and multiply it with the each element in the ith row of B.

The result will be equal to the width of B * length A

so we have:

0th element in 0th row of A times elements in 0th row of B
1 * 7; 1 * 0; 1 * 0 => res[0] = [7, 0, 0]

1st element in 0th row of A times elements in 1st row of B
0 * 0; 0 * 0; 0 * 0 => res[0] = [7, 0, 0]

2nd element in 0th row of A times elements in 2nd row of B
0 * 0; 0 * 0; 0 * 1 => res[0] = [7, 0, 0]

STORE ACCUMUTAED TOTAL IN 0TH ROW OF RESULT LIST



0th element in 1th row of A times elements in 0th row of B
-1 * 7; -1 * 0, -1 * 0 => res[1] = [-7, 0, 0]

1st element in 1th row of A times elements in 1th row of B
0 * 0; 0 * 0; 0 * 0 => res[1] = [-7, 0, 0]

2nd element in 1th row of A times elements in 2nd row of B
3 * 0; 3 * 0, 3 * 1 => res[1] = [-7, 0, 3]

STORE ACCUMUTAED TOTAL IN 1TH ROW OF RESULT LIST


res = [[7, 0, 0],
       [-7, 0, 3]]

The trick to use to speed up the process is to only multily when the element in the ith row of A is not Zero. And when the ith row in B is not Zero!

Time complexity: O(m * n * k) where k is average number of non-zero elements in A and B. m and n are legnth and width of A
"""
def multiply(A, B):
    if A is None or B is None: return None

    rows_a = len(A)
    cols_a = len(A[0])
    cols_b = len(B[0])

    c = [[0 for i in range(cols_b)] for j in range(rows_a)]

    for i in range(rows_a): # O(rows_a)
        for j in range(cols_a): # O(cols_a)
            if A[i][j] != 0:
                for k in range(cols_b):
                    if B[j][k] != 0:
                        c[i][k] += A[i][j] * B[j][k]

    return c


"""
Use a table to store row, col and value of all non-zero elements in matrix B

Go through rest of algo as usual this using using table

https://discuss.leetcode.com/topic/30626/java-and-python-solutions-with-and-without-tables
"""
def multiply_1(A, B):
    rows_a, cols_a, cols_b = len(A), len(A[0]), len(B[0])

    if len(B) != cols_a:
        raise Exception("A's column number must be equal to B's row number")

    c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    tableB = {}

    for k, row in enumerate(B):
        tableB[k] = {}
        for j, eleB in enumerate(row):
            if eleB:
                tableB[k][j] = eleB

    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in tableB[k].items():
                    c[i][j] += eleA * eleB

    return c


def multiply_2(A, B):
    if A is None or B is None: return None

    rows_a, cols_a = len(A), len(A[0])

    if len(B) != cols_a:
        raise Exception("A's column number must be equal to B's row number.")

    cols_b = len(B[0])
    table_A, table_B = {}, {}

    for i, row in enumerate(A):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_A:
                    table_A[i] = {}
                table_A[i][j] = ele

    for i, row in enumerate(B):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_B:
                    table_B[i] = {}
                table_B[i][j] = ele

    c = [[0 for j in range(cols_b)] for i in range(rows_a)]

    for i in table_A:
        for j in table_A[i]:
            if j not in table_B: continue
            for k in table_B[j]:
                c[i][k] += table_A[i][j] * table_B[j][k]

    return c

if __name__ == '__main__':
    A = [
          [ 1, 0, 0],
          [-1, 0, 3]
        ]

    B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]
        ]

    print multiply(A, B)
    print multiply_1(A, B)
    print multiply_2(A, B)
