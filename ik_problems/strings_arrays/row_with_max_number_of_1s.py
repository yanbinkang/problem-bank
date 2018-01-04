"""
solution: http://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
"""
# O(m+n)
def row_with_max_1s(matrix):
    m = len(matrix[0])
    n = len(matrix)
    res = {}
    i = 0

    while i < m:
        count = 0
        j = 0
        while j < n:
            if matrix[i][j] == 1:
                count += 1
            j += 1
        res[i] = count
        i += 1

    max_val = max(res.values())
    for k, v in res.items():
        if v == max_val:
            return k


# 0(mLogn)
def row_with_max_1s(matrix):
    max_row_index = 0
    _max = -1

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        index = first(matrix[i])

        if index != -1 and col - index > _max:
            _max = col - index
            max_row_index = i

    return max_row_index

def first(arr):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if (mid == 0 or arr[mid - 1] == 0) and (arr[mid] == 1):
            return mid
        else:
            if arr[mid] == 0:
                first = mid + 1
            else:
                last = mid - 1

    return -1

if __name__ == '__main__':
    inpt = [[0, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0]]

    print row_with_max_1s(inpt)
