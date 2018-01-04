"""
solution: http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
"""

def coin_play(pots):
    n = len(pots)
    first = [[0 for j in range(n)] for i in range(n)]


    for gap in range(n):
        i = 0
        j = gap
        while j < n:
            x = first[i+2][j] if (i+2 <= j) else 0
            y = first[i+1][j-1] if (i+1 <= j-1) else 0
            z = first[i][j-2] if (i < j-2) else 0

            first[i][j] = max(pots[i] + min(x, y), pots[j] + min(y, z))
            i += 1
            j += 1
    return first[0][n-1]

if __name__ == '__main__':
    print coin_play([8, 15, 3, 7])
    print coin_play([5, 3, 7, 10])




# def coin_play(pot):
#     first = [[0 for j in range(len(pot))] for i in range(len(pot))]
#     second = [[0 for j in range(len(pot))] for i in range(len(pot))]

#     for l in range(1, len(pot) + 1):
#         for i in range(0, len(pot) - l + 1):
#             j = i + l - 1
#             if l == 1:
#                 #base case: when there is only one coin
#                 first[i][i] = pot[i]
#                 second[i][i] = 0
#             else:
#                 if pot[i] + second[i + 1][j] >= pot[j] + second[i][j - 1]:
#                     first[i][j] = pot[i] + second[i + 1][j]
#                     second[i][j] = first[i + 1][j]
#                 else:
#                     first[i][j] = pot[j] + second[i][j - 1]
#                     second[i][j] = first[i][j - 1]
#     return first[0][len(pot)-1]


# if __name__ == '__main__':
#     print coin_play([5, 3, 7, 10])
#     print coin_play([8, 15, 3, 7])
