def plus_one(A):
    """
    Write an program which takes an input array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.

    Eg. [1, 2, 9] => [1, 3, 0]

    Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break

        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        """
        There is a carry-out, so we need one more digit to store the result.
        A slick way to do this is to append 0 at the end of the array,
        and update the first entry to 1.
        """
        A[0] = 1
        A.append(0)

    return A

if __name__ == '__main__':
    print plus_one([1, 9, 9])
