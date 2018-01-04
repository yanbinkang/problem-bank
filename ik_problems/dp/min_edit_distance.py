# http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

def min_edit_distance(str1, str2):
    table = [[None for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    for i in range(len(table[0])):
        table[0][i] = i

    for i in range(len(table)):
        table[i][0] = i

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i - 1][j], table[i - 1][j - 1], table[i][j - 1]) + 1

    return table[len(str2)][len(str1)]


print min_edit_distance("abcdef", "azced")
