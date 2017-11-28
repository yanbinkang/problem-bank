def coin_change_dp(denominations, amount):
    solution = [1] + [0] * amount
    solution[0] = 1

    for den in denominations:
        for i in range(den, amount+1):
            solution[i] += solution[i - den]

    return solution[len(solution) - 1]

print coin_change_dp([1, 2, 3], 4)
print coin_change_dp([1, 2, 5], 7)
print coin_change_dp([5, 7], 11)
print coin_change_dp([5, 2, 3], 10)
print coin_change_dp([1], 2)

