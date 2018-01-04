def solve_n_queens(n):
    result = []
    solve(n, 0, [-1 for i in range(n)], result)

    return result

def solve(n, curr_queen_num, board, result):
    if curr_queen_num == n:
        one_answer = [['.' for j in range(n)] for i in range(n)]
        for i in range(n):
            # place Q on board
            one_answer[i][board[i]] = 'Q'
            # store row representaion in var one_answer[i]
            one_answer[i] = ''.join(one_answer[i])
        result.append(one_answer)
        return

    for i in range(n):
        valid = True
        for j in range(curr_queen_num):
            if board[j] == i:
                valid = False
                break
            if abs(board[j]- i) == curr_queen_num - j:
                valid = False
                break
        if valid:
            board[curr_queen_num] = i
            solve(n, curr_queen_num + 1, board, result)

print solve_n_queens(8)
print "\n"
print "There exist", str(len(solve_n_queens(8))), "arrangements"
