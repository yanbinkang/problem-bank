def max_profit(prices)
  max_pro = 0
  min_price_so_far = Float::INFINITY

  for price in prices
    min_price_so_far = [min_price_so_far, price].min
    max_pro = [max_pro, price - min_price_so_far].max
  end

  max_pro
end

def max_profit_1(prices)
  max_cur, max_so_far = 0, 0

  (1..prices.length - 1).each do |i| # or (1...prices.length).each
    max_cur += prices[i] - prices[i - 1]
    max_cur = [0, max_cur].max
    max_so_far = [max_cur, max_so_far].max
  end

  max_so_far
end

p max_profit([7, 1, 5, 3, 6, 4])
p max_profit([7, 6, 4, 3, 1])
p max_profit([0, 6, -3, 7])
p max_profit([1, 7, 4, 11])
p max_profit([-2, 1, -3, 4, -1, 2, 1, -5, 4])
puts
p max_profit_1([7, 1, 5, 3, 6, 4])
p max_profit_1([7, 6, 4, 3, 1])
p max_profit_1([0, 6, -3, 7])
p max_profit_1([1, 7, 4, 11])
p max_profit_1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
