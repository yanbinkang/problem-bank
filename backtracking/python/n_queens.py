"""
https://youtu.be/xouin83ebxE

You can use a tuple to store Q ro and col instead of Position object
"""
class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return str(self.row) + ', ' + str(self.col)

def solve_n_queens(n):
    positions = [None for i in range(n)]
    has_solution = solved_nqueen_one_solution_util(n, 0, positions)

    if has_solution:
        return positions
    else:
        return 0

def solved_nqueen_one_solution_util(n, row, positions):
    if n == row:
        return True

    for col in range(n):
        found_safe = True

        for queen in range(row):
            if (positions[queen].col == col) or \
               (positions[queen].row - positions[queen].col == row - col) or \
               (positions[queen].row + positions[queen].col == row + col):
                    found_safe = False
                    break

        if found_safe:
            positions[row] = Position(row, col)
            if solved_nqueen_one_solution_util(n, row + 1, positions):
                return True

    return False


def solve_n_queens_1(n):
    positions = [None for i in range(n)]
    has_solution = solved_nqueen_one_solution_util(n, 0, positions)

    if has_solution:
        return positions
    else:
        return 0

def solved_nqueen_one_solution_util(n, row, positions):
    if n == row:
        return True

    for col in range(n):
        found_safe = True

        for queen in range(row):
            if (positions[queen][1] == col) or \
               (positions[queen][0] - positions[queen][1] == row - col) or \
               (positions[queen][0] + positions[queen][1] == row + col):
                    found_safe = False
                    break

        if found_safe:
            positions[row] = (row, col)
            if solved_nqueen_one_solution_util(n, row + 1, positions):
                return True

    return False



if __name__ == '__main__':
    res = solve_n_queens(4)
    print [str(i) for i in res]
    print '\n'
    res = solve_n_queens_1(4)
    print res
