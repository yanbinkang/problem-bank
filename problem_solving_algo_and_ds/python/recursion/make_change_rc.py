# extremely inefficient. over 67,716,925 recursive calls.
def rec_mc(coin_value_list, change):
    min_coins = change

    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_mc(coin_value_list, change-i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(rec_mc([1, 5, 10, 25], 63))
