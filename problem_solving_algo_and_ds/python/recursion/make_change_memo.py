def rec_dc(coin_value_list, change, know_results):
    min_coins = change

    if change in coin_value_list:
        know_results[change] = 1
        return 1
    elif know_results[change] > 0:
        return know_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins =  1 + rec_dc(coin_value_list, change-i, know_results)
            if num_coins < min_coins:
                min_coins = num_coins
                know_results[change] = min_coins
    return min_coins

print(rec_dc([1, 5, 10, 25], 63, [0]*64))
