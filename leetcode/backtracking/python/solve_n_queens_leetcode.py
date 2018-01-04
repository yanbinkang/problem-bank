"""
https://leetcode.com/problems/n-queens/

Given nxn board place n queen on this board so that they dont attack each other.

https://youtu.be/xouin83ebxE

Time complexity O(n*n)
Space complexity O(n) because our recursion in the worse case will be n-level's deep for a nxn board
"""
def solve_n_queens(n):
    result = []
    positions = [None for i in range(n)]
    solve(n, 0, positions, result)

    return result

def solve(n, row, positions, result):
    if n == row:
        string = ''
        one_result = []
        for pos in positions:
            for i in range(n):
                string += 'Q' if pos[1] == i else '.'
                # if pos[1] == i:
                #     string += 'Q'
                # else:
                #     string += '.'

            one_result.append(string)
            string = ''
        result.append(one_result)
        return

    for col in range(n):
        found_safe = True


        """
        check if this row and col is not under attack from any previous queen
        queen's on the same row, col and diagonals will be attacked
        diagonals: top left to buttom right = row - col
        diagonals: bottom left to top right = row + col
        """
        for queen in range(row):
            if positions[queen][1] == col or \
               positions[queen][0] - positions[queen][1] == row - col or \
               positions[queen][0] + positions[queen][1] == row + col:
                    found_safe = False
                    break # row, col under attack; do not check other queens!

        if found_safe:
            positions[row] = (row, col)
            solve(n, row + 1, positions, result)

if __name__ == '__main__':
    print solve_n_queens(4)
    print('\n')
    print solve_n_queens(8)
