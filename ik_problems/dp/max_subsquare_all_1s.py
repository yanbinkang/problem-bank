def max_size(matrix):
    result = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

    # first column is always equal to first column of input matrix
    for i in range(len(result)):
        result[i][0] = matrix[i][0]

    # first row is always equal to first row of input matrix
    for i in range(len(matrix[0])):
        result[0][i] = matrix[0][i]

    max_val = 1
    max_i = 0
    max_j = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            # if matrix value is zero do nothing
            if matrix[i][j] == 0:
                result[i][j] = 0
            else:
                # get min of top, diagonal or left and add 1 if matrix value is 1
                # result[i-1][j] = top
                # result[i-1][j-1] = diagonal
                # result[i][j-1] = left
                t = min(result[i-1][j], result[i-1][j-1], result[i][j-1])
                result[i][j] = t + 1
            # update max_val
            if result[i][j] > max_val:
                max_val = result[i][j]
                max_i = i
                max_j = j

    # return max_val (this is the max size of sub square all 1s)

    # print sub matrix
    i = max_i
    while i > max_i - max_val:
        j = max_j
        while j > max_j - max_val:
            print "%s" % matrix[i][j]
            j -= 1
        print "\n"
        i -= 1

arr = [[0, 1, 1, 0, 1],
       [1, 1, 1, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 0, 1]]

if __name__ == '__main__':
    print max_size(arr)
