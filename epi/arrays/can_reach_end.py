def can_reach_end(A):
    """
    In a particular game, a player has to try to advance through a sequence of positions. Each position has a non-negative integer associated with it, representing the maximum you can advance from that position in one move. You begin a the first position and win by getting to the last position.

    For example, let A = [3, 3, 1, 0, 2, 0, 1] represent the board game, i.e, the ith entry in A is the maximum we can advance from i. Then the game can be won by the following sequence of advances through A:

    take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from A[4] to A[6], which is the last position. Note that A[0] = 3 >= 1, A[1] = 3 >= 3, A[4] = 2 >= 2, so all moves are valid.

    If A instead was [3, 2, 0, 0, 2, 0, 1], it would not be possible to advance past position 3, so the game cannot be won.

    Write a program which takes an array of n integers, where A[i] denotes the maximum you can advance from index i, and returns whether it is possible to advance to the last index starting from the beginning of the array.

    Algo: If for some i before the end of the array, i is the furthest index that we have demonstarated that we can advance to, we cannot reach the last index. Otherwise, we can reach the end.
    """
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0

    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)

        #note: A[i] + i is the actual index on the array you'll move to. Eg. if the first number in A is 3 i.e A[0] = 3, it means you can only advance as far as index 3 in A after making a move. This applies to all indexes and values in A.

        i += 1

    return furthest_reach_so_far >= last_index

if __name__ == '__main__':
    print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
    print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))
