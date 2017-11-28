def is_interleaved(str1, str2, str3):
    m = len(str1)
    n = len(str2)

    table = [[False for i in range(m+1)] for j in range(n+1)]

    if m + n != len(str3):
        return False

    for i in range(len(table)):
        for j in range(len(table[i])):
            l = i + j - 1
            if i == 0 and j == 0:
                table[i][j] = True
            elif i == 0:
                if str3[l] == str2[j-1]:
                    table[i][j] = table[i][j-1]
            elif j == 0:
                if str1[i-1] == str3[l]:
                    table[i][j] = table[i-1][j]
            else:
                table[i][j] = (table[i-1][j] if str1[i-1] == str3[l] else False) or (table[i][j-1] if str2[j-1] == str3[l] else False)

    return table[m][n]


print is_interleaved("aab", "axy", "aaxaby")
print is_interleaved("aab", "axy", "abaaxy")
print is_interleaved("XXY", "XXZ", "XXZXXXY")
print is_interleaved("XY" ,"WZ" ,"WZXY")
# print is_interleaved("XY", "X", "XXY")
# print is_interleaved("YX", "X", "XXY")
print is_interleaved("XXY", "XXZ", "XXXXZY")
