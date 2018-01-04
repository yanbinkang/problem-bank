def print_spiral_order(array, m, n):
    k = 0
    l = 0
    i = 0

    while k < m and l < n:
        while i < n:
            print array[k][i] ,
            i += 1

        k += 1

        i = k
        while i < m:
            print array[i][n-1] ,
            i += 1
        n -= 1

        if k < m:
            i = n - 1
            while  i >= l:
                print array[m-1][i] ,
                i -= 1
            m -= 1

        if l < n:
            i = m - 1
            while i >= k:
                print array[i][l] ,
                i -= 1
            i += 1


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

s = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],
     [17, 18, 19, 20]]

print_spiral_order(s, 5, 4)
