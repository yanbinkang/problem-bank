"""
https://leetcode.com/problems/n-queens-ii/

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

https://youtu.be/xouin83ebxE
"""

def total_n_queens(n):
    positions = [None for i in range(n)]
    count = [0]

    total(n, 0, positions, count)

    return count[0]

def total(n, row, positions, count):
    if row == n:
        count[0] += 1
        return

    for col in range(n):
        found_safe = True

        for queen in range(row):
            if positions[queen][1] == col or\
               positions[queen][0] - positions[queen][1] == row - col or\
               positions[queen][0] + positions[queen][1] ==  row + col:
                    found_safe = False
                    break

        if found_safe:
            positions[row] = (row, col)
            total(n, row + 1, positions, count)


if __name__ == '__main__':
    print total_n_queens(4)
