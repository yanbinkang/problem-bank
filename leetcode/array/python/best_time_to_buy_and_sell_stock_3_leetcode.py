"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_total_profit, min_price_so_far = 0, float('inf')
        first_buy_sell_profits = [0] * len(prices)

        for i, price in enumerate(prices):
            min_price_so_far = min(min_price_so_far, price)
            max_total_profit = max(max_total_profit, price - min_price_so_far)
            first_buy_sell_profits[i] = max_total_profit

        max_price_so_far = float('-inf')

        for i, price in reversed(list(enumerate(prices[1:], 1))):
            max_price_so_far = max(max_price_so_far, price)
            max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])

        return max_total_profit

