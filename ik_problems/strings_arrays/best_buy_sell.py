def best_buy_sell(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices:
        min_price = min(min_price, current_price)
        max_profit = max(max_profit, current_price - min_price)
    return max_profit
