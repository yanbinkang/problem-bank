RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    """
    Problem:

    Write a program that takes an array A and and index i into A, and rearranges the elements such that all elements less than A[i] (the pivot) appear first, followed by elements equal to the pivot, followed by elements greater than the pivot

    Keep the following invariants during partitioning:
    bottom group: A[:smaller]
    middle group: A[smaller:equal]
    unclassified group: A[equal:larger]
    top group: A[larger:]

    # O(n) time O(1) space
    """
    pivot = A[pivot_index]

    smaller, equal, larger = 0, 0, len(A)

    # keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# O(n) time, O(1) space
def dutch_flag_partition_(pivot_index, A):
    pivot = A[pivot_index]

    # First pass: group elements smaller than pivot
    smaller = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# O(n^2)
def dutch_flag_partition__(pivot_index, A):
    pivot = A[pivot_index]

    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break

        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

if __name__ == '__main__':
    A = [0, 1, 2, 0, 2, 1, 1]
    pivot_index = 0
    print dutch_flag_partition.__doc__

    dutch_flag_partition(pivot_index, A)
    print A
