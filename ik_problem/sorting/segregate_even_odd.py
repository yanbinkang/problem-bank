"""
solution: http://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
"""
def segregate_even_odd(a_list):
    left = 0
    right = len(a_list) - 1

    while left < right:
        while a_list[left] % 2 == 0 and left < right:
            left += 1

        while  a_list[right] % 2 == 1 and left < right:
            right -= 1

        if left < right:
            temp = a_list[left]
            a_list[left] = a_list[right]
            a_list[right] = temp

            left += 1
            right -= 1

    return a_list

# arr = [4, 1, 2, 3, 4]
arr = [1, 3, 5, 4, 6]
# arr = [12, 34, 45, 9, 8, 90, 3]
print segregate_even_odd(arr)
