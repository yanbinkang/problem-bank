def remove_duplicates(A, key):
    """
    Implement a function which takes as input an array and a key and updates the array such that all occurances of the input key have been removed and the remaining elements have been shifted to fill the emptied indices.

    Return the number of remaining elements. There are no requirements as to the values stored beyond the last valid element.
    """
    if not A or key not in A: return

    insert_pos = 0

    for num in A:
        if num != key:
            A[insert_pos] = num
            insert_pos += 1

    return insert_pos

if __name__ == '__main__':
    print(remove_duplicates([0, 1, 0, 3, 12], 0)) #3
