"""
https://leetcode.com/problems/coin-change/description/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

ref: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

O(n * amount) time and O(amount) space

For each amount from 1 to amount, go through all the coins given.

If the coin is less than or equal to the amount we're looking at, ask yourself, how many more coins do we need to get to this amount? Or what is the sum for which this coin needs to be addded to make this amount?

Eg. Say we're looking at amount 4 and coin 3. We have to ask, "how many more coins do I need to get a total of 4?" or "what is the sum for which 3 has to be added to make 4?".

The answer is 4 - 3 == 1. So we look at the value store at result[1] -- the minimum number of coins we could make (out of all possible coins) given an amount of  1. Get this value and add 1 to it. If its less than the value stored at result[i], we take it.

        if coin <= i and result[i - coin] + 1 < result[i]:
                result[i] = result[i - coin] + 1
"""
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    result = [float('inf')] * (amount + 1)
    result[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and result[i - coin] + 1 < result[i]:
                result[i] = result[i - coin] + 1

    # if result[amount] still infinity -> not possible
    return -1 if result[amount] > amount else result[amount]


if __name__ == '__main__':
    print coinChange([1, 3, 5], 11)
