def number_of_paths(a_list, x, y):
    height = len(a_list[0])
    width = len(a_list)

    # base case
    if x == width - 1 and y == height - 1:
        return a_list[x][y]
    elif x == width - 1:
        return a_list[x][y+1]
    elif y == height - 1:
        return a_list[x+1][y]
    elif a_list[x][y] == 1:
        return number_of_paths(a_list, x + 1, y) + number_of_paths(a_list, x, y+ 1)
    else:
        return 0


matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 1, 1]]

print number_of_paths(matrix, 0, 0)
