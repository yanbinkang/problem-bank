"""
Problem Statement
=================

0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
weight.

Runtime Analysis
----------------
Time complexity - O(W*total items)

Video
-----
* Topdown DP - https://youtu.be/149WSzQ4E1g
* Bottomup DP - https://youtu.be/8LusJS5-AGo

References
----------
* http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
* https://en.wikipedia.org/wiki/Knapsack_problem
"""


def knapsack_01(profits, weights, capacity):
    total_items = len(weights)

    rows = total_items + 1
    cols = capacity + 1

    table = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):  # row
        for j in range(1, cols):  # column
            if j < weights[i - 1]:
                table[i][j] = table[i - 1][j]
            else:
                # watch youtube video at position 5:20 for perfect explanation of this branch
                table[i][j] = max(
                    table[i - i][j],
                    profits[i - 1] + table[i - 1][j - weights[i - 1]])

    return table[rows - 1][cols - 1]


def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    # base case
    if capacity <= 0 or current_index < 0 or current_index >= len(profits):
        return 0

    # recursive call after choosing the element at current_index
    # if the weight of the element at current_index exceeds the capacity,
    # we shouldn't process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_recursive(
            profits, weights, capacity - weights[current_index],
            current_index + 1)

    # recursive call after exceeding the element at the current_index
    profit2 = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit1, profit2)


if __name__ == "__main__":
    profits = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    max_profit = solve_knapsack(profits, weights, 7)
    print(max_profit)
