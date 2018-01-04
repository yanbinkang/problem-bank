# http://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
"""
1) Start with top right element
2) Loop: compare this element e with x
….i) if they are equal then return its position
…ii) e < x then move it to down (if out of bound of matrix then break return false)
..iii) e > x then move it to left (if out of bound of matrix then break return false)
3) repeat the i), ii) and iii) till you find element or return false
"""
def search(matrix, x):
    i = 0
    rows = len(matrix)
    cols = len(matrix[0]) - 1

    while i < rows and cols >= 0:
        if matrix[i][cols] == x:
            print("found at %s %s") % (i, cols)
            return 1
        if matrix[i][cols] > x:
            cols -= 1
        else:
            i += 1
    print("\n Element not found")
    return 0

arr = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

search(arr, 32)
