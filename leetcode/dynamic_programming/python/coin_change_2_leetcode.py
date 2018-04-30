"""
https://leetcode.com/problems/coin-change-2/description/

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that
    1. 0 <= amount <= 5000
    2. 1 <= coin <= 5000
    3. the number of coins is less than 500
    4. the answer is guaranteed to fit into signed 32-bit integer

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

ref: https://www.educative.io/collection/page/5642554087309312/5679846214598656/210001

video: https://youtu.be/_fgjrs570YE?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

Time complexity: O(m n) where m is number of denominations and n is amount.

Space complexity: Linear, O(n) where n is the amount.

Explanation:

1. initialize result to array of zeros with length equal to (amount + 1). One additional space is reserved because we also want to store result for 0 amount. There is only one way you can make change of 0 i.e. select no coin so we'll initialize result[0] = 1.

2. Iterate through the coins, coin

3. In an inner loop iterate through all the possible amounts x from coin <= x <= amount

4. At each step you ask yourself, given total x and coin(s), how much change can I make:

    examples: given amount 5 and coins [1, 2, 5]

    coin = 1
    result = [1, 0, 0, 0, 0, 0] => the indexes become the amounts, number of ways becaomes the value

    Initially, the question becomes given an amount 1 and coin 1, how many ways can I make change? The answer is 1

    Then given an amount of 2 and coin of 1, how many ways can I make change? Again the answer is 1

    Continue till total is 7 while coin is still 1. At the end of this iteration result becomes:

            result = [1, 1, 1, 1, 1, 1]

    Next, move to the next coin 2. The inner loop for amount's range becomes 2 <= x <= 5

    We start at 2 because we know that given an amount of 1 and coins 1 and 2, 2 won't make any difference and since we already know that result for changing with coin 1 and amount 1, we move on.

    Now, the question is given coins 1 and 2 and a total of 2, how many ways can I make change? We already know how many ways we can make change with coin 1 and total 2. This is stored in result[i - coin]. The outcome when we add this new coin of 2 is stored at result[i]. so the formular becomes:

            result[i] = result[i] + result[i - coin]

5. At the end result[amount] will have the solution. return result[len(result) - 1]
"""
def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    result = [0] * (amount + 1)
    result[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            result[i] = result[i] + result[i - coin]

    return result[len(result) - 1] # or result[-1]
    # return result[amount]


print change(5, [1, 2, 5])
