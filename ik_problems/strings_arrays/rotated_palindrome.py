"""
solution: http://www.geeksforgeeks.org/check-given-string-rotation-palindrome/
"""
# O(n^2)
def is_rotated_palindrome(s):
    # if string itself is a palindrome
    if is_palindrome(s):
        return True
    n = len(s)

    # try all rotations one by one
    for i in range(n):
        # this is the same as array rotation by d elements
        # remember you can do this in-place. upper bound of d is 2 * d + 1
        # see below for implementation.
        # note in Python you have to convert string to list and convert back to string.
        str_1 = s[i+1:n-i-1]
        str_2 = s[0:i+1]

        if is_palindrome(str_1 + str_2):
            return True

    return False


def is_palindrome(s):
    return s == s[::-1]

print is_rotated_palindrome("aab")
print is_rotated_palindrome("abcde")
print is_rotated_palindrome("aaaad")
print is_rotated_palindrome("icciv")
print is_rotated_palindrome("nahhan")

"""
solution: http://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
1) reverse the whole collection
2) reverse first n - num chars of collection where n is size of collection
3) reverse last n - num chars of collection where n is size of collection
"""
def rotate(a_list, num):
    n = len(a_list)
    reverse(a_list, 0, n - 1)
    reverse(a_list, 0, n - num - 1)
    reverse(a_list, n - num + 1, n - 1)

    # return ''.join(a_list)
    return a_list


def reverse(a_list, first, last):
    while first < last:
        temp = a_list[first]
        a_list[first] = a_list[last]
        a_list[last] = temp

        first += 1
        last -= 1
    return a_list

# print rotate([1, 2, 3, 4, 5, 6, 7], 2)
# print rotate([1, 2, 3, 4, 5], 4)
