"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

"""
ref: https://discuss.leetcode.com/topic/17081/three-lines-in-c-with-explanation

1. Buy and then sell on the same day means doing nothing on that day. Before the day starts, you have nothing, when the day ends you have nothing.

2. Same goes for "sell and then buy on the same day". Before the day starts, you have an amount of money, when the day ends, you still have the same amount of money.

3. So the only way to make a profit is to add the diff up

example: for [5, 8, 9, 10] it is (8 - 5) + (9 - 8) + (10 - 9) == 10 - 5 == 5

Second, suppose the first sequence is "a <= b <= c <= d", the profit is "d - a = (b - a) + (c - b) + (d - c)" without a doubt.

And suppose another one is "a <= b >= b' <= c <= d", the profit is not difficult to be figured out as "(b - a) + (d - b')". So you just target at monotone sequences.

Note: If a sequence is increasing or is a decreasing we call it monotonic

O(n) time, O(1) space
"""
def max_profit_1(price):
    total = 0

    for i in range(1, len(prices)):
        total = total + max(prices[i] - price[i - 1], 0)
        # max(prices[i] - price[i - 1], 0) if the price differnece doesn't make us a profit, do nothing. i.e add zero

    return total

def max_profit(prices):
    total = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            total += prices[i + 1] - prices[i]

    return total
