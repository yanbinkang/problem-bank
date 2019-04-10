"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

https://discuss.leetcode.com/topic/5863/sharing-my-simple-and-clear-c-solution

hint: at the ith element, ask yourself, which price is the min_so_far (from 0th - ith index). When you subtract the current price (ith element) from the min_so_far, we'll get a profit. Return the max profit at the end of the iteration!
"""


def max_profit(prices):
    max_pro = 0
    min_price_so_far = float('inf')

    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        max_pro = max(max_pro, price - min_price_so_far)

    return max_pro


# https://discuss.leetcode.com/topic/19853/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input
def max_profit_1(prices):
    max_cur, max_so_far = 0, 0

    for i in range(1, len(prices)):
        max_cur += prices[i] - prices[i - 1]
        max_cur = max(0, max_cur)
        max_so_far = max(max_cur, max_so_far)

    return max_so_far


if __name__ == '__main__':
    print max_profit([7, 1, 5, 3, 6, 4])
    print('\n')
    print max_profit([7, 6, 4, 3, 1])
    print('\n')
    print max_profit([0, 6, -3, 7])
    print('\n')
    print max_profit([1, 7, 4, 11])
    print('\n')
    print max_profit([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print('\n')
    print max_profit_1([7, 1, 5, 3, 6, 4])
    print('\n')
    print max_profit_1([7, 6, 4, 3, 1])
    print('\n')
    print max_profit_1([0, 6, -3, 7])
    print('\n')
    print max_profit_1([1, 7, 4, 11])
    print('\n')
    print max_profit_1([0, 6, -3, 7])
    print('\n')
    print max_profit_1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
