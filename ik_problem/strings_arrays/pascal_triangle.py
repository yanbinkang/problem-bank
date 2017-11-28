# solution: http://www.geeksforgeeks.org/pascal-triangle/
# O(n^2) time and O(1) extra space
# def print_pascal(n):
#     for i in range(1, n+1):
#         c = 1
#         j = 1
#         while j <= i:
#             print c
#             c = c * (i - j) / j
#             j += 1
#         print("\n")

# print print_pascal(6)

# O(n^2) time and O(n^2) extra space
def print_pascal(n):
    #auxiliary array to store generated pascal values
    arr = [[0 for i in range(n)] for k in range(n)]

    # iterate trough every line and print integers in it
    for line in range(n):
        # every line has number of integers equal to line number
        for i in range(line + 1):
            # first and last values in every row is 1
            if line == i or i == 0:
                arr[line][i] = 1
            else:
                # other values are sum of values just above and left of above
                arr[line][i] = arr[line-1][i-1] + arr[line-1][i]
            print arr[line][i]
        print "\n"

print print_pascal(4)


