"""
Find all permutations of a given length N, of a string
"""

def print_permutations_recursion(n, a_list, i):
    if i == n:
        j = 0
        while j < n:
            print a_list[j]
            j += 1
        print("\n")
        return

    j = i
    while j < n:
        temp = a_list[j]
        a_list[j] = a_list[i]
        a_list[i] = temp

        print_permutations_recursion(n, a_list, i + 1)

        a_list[i] = a_list[j]
        a_list[j] = temp

        j += 1

def print_permutations(n):
    arr = [n] * n
    i = 0

    while i < n:
        arr[i] = i + 1
        i += 1
    print_permutations_recursion(n, arr, 0)

print_permutations(3)
