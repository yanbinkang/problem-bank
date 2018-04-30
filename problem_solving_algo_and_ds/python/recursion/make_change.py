def dp_make_change(coin_value_list, change, min_coins, coins_used):
   for cents in range(change+1):
      coin_count = cents
      for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
               coin_count = min_coins[cents-j]+1
               new_coin = j
      min_coins[cents] = coin_count
      coins_used[cents] = new_coin
   return min_coins[change]
