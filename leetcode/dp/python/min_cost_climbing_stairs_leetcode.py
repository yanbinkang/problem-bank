"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
* cost will have a length in the range [2, 1000].
* Every cost[i] will be an integer in the range [0, 999].

O(n) time O(1) space
ref: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/110111/Easy-to-understand-C++-using-DP-with-detailed-explanation
"""
def minCostClimbingStairs(cost):
    n = len(cost)
    for i in range(2, n):
        cost[i] = cost[i] + min(cost[i - 2], cost[i - 1])

    return min(cost[n - 2], cost[n - 1])

if __name__ == '__main__':
    print minCostClimbingStairs([10, 15, 20])
    print minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
