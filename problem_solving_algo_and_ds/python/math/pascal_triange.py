# solution: http://www.geeksforgeeks.org/pascal-triangle/
# O(n^2) time and O(1) extra space
def print_pascal(n):
    for i in range(1, n+1):
        c = 1
        j = 1
        while j <= i:
            print c
            c = c * (i - j) / j
            j += 1
        print("\n")

print print_pascal(6)

# O(n^2) time and O(n^2) extra space
def print_pascal(n):
    arr = [[0 for i in range(n)] for k in range(n)]
    line = 0
    while line < n:
        i = 0
        while i <= line:
            # if we're at first or end of line
            if line == i or i == 0:
                arr[line][i] = 1
            else:
                # we're in between first and end of line
                arr[line][i] = arr[line-1][i-1] + arr[line-1][i]
            print arr[line][i]
            i += 1
        line += 1
        print "\n"

print print_pascal(4)
