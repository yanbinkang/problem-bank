def even_odd(A):
    """
    Your input is an array of integers, and you have to reorder its entries so that even entries appear first
    """
    next_even, next_odd = 0, len(A) -  1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


if __name__ == '__main__':
    print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
