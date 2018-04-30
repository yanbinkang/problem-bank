def longest_subarray_all_equal(A):
    """
    Write a program that takes an array of integers and finds the length of a longest subarray whose entries are equal
    """
    left, right, max_length = 0, 0, 1

    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            right += 1

            max_length = max(max_length, right - left + 1)
        else:
            left = right = i

    return max_length

if __name__ == '__main__':
    print(longest_subarray_all_equal([1, 2, 3, 3, 3, 5, 78, 0]))
