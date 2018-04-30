def buy_and_sell_stock_once(prices):
    """
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] => Prices


    [310, 310, 275, 275, 260, 260, 260, 230, 230, 230] => Min Pc So Far

    [0, 5, 0, 20, 0, 10, 30, 0, 25, 20] => Max Profit

    O(n) time O(1) space
    """
    min_price_so_far, max_profit = float('inf') , 0.0

    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)

    return max_profit

if __name__ == '__main__':
    print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
