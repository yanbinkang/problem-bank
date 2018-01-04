# http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
"""
Given N find the numbers for N to (2**N) - 1 such that the numbers do not have consecutive 1's in their binary representation.
"""

def count_number_of_binary_without_consecutive_1s(n):
    a = [None for i in range(n)]
    b = [None for i in range(n)]

    a[0] = 1
    b[0] = 1

    for i in range(1, n):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]

    return a[n - 1] + b[n - 1]

print count_number_of_binary_without_consecutive_1s(4)
