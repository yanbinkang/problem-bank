def lcs(x, y):
    n = len(x)
    m = len(y)
    table = {}

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i, j] = 0
            elif x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i-1, j], table[i, j-1])

    # now table[n, m] is the lcs of x and y

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif x[i-1] == y[j - 1]:
            return recon(i-1, j-1) + [x[i-1]]
        elif table[i-1, j] > table[i, j-1]:
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return ''.join(recon(n, m))

print lcs("AGGTAB", "GXTXAYB")
print lcs("ABCDGHLQR", "AEDPHR")

"""
def lcs(x, y):
    m = len(x)
    n = len(y)
    temp = [[0 for i in range(m+1)] for j in range(n+1)]

    max_val = 0

    for i in range(1, len(temp)):
        for j in range(1, len(temp[i])):
            temp[i][j] = max(temp[i][j-1], temp[i-1][j])

            if y[i-1] == x[j-1]:
                temp[i][j] = temp[i-1][j-1] + 1
                if temp[i][j] > max_val:
                    max_val = temp[i][j]

    print temp
    return max_val

if __name__ == '__main__':
    print lcs("ABCDGH", "AEDFHR")
    print lcs("AGGTAB", "GXTXAYB")
    print lcs("ABCDGHLQR", "AEDPHR")
    print lcs("abcdaf", "acbcf")
"""
