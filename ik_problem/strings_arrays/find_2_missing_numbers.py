def missing_number(input_array):
    original_array = range(1, len(input_array)+3)

    for num in input_array:
        if num in original_array:
            original_array.remove(num)

    return original_array

print missing_number([4, 1, 2, 6, 5])
print missing_number([1, 3, 4, 5, 6, 7, 8, 9])
