def find_palindromes_in_sub_string(input, j, k):
    count = 0
    while j >= 0 and k < len(input):
        if input[j] != input[k]:
            break
        count += 1

        j -= 1
        k += 1

    return count

def find_all_palindrome_substrings(input):
    count = 0
    for i in xrange(0, len(input)):
        count += find_palindromes_in_sub_string(input, i - 1, i + 1)
        count += find_palindromes_in_sub_string(input, i, i + 1)
    return count

print find_all_palindrome_substrings('aabbbaa')


# def palindrome_substring(a_string):
#     mid_point = len(a_string) // 2

#     i = mid_point
#     j = mid_point
#     count = 0

#     middle_str = a_string[mid_point]

#     while i > 0 and j < len(a_string):
#         if a_string[i - 1] == a_string[j + 1]:
#             count += 1
#         i -= 1
#         j += 1

#     return count

# print palindrome_substring('aabbbaa')

# def palindrome_substring(a_string):
#     mid_point = len(a_string) // 2

#     i = mid_point
#     j = mid_point
#     result = []

#     middle_str = a_string[mid_point]

#     while i >= 0 and j < len(a_string):
#         if a_string[i - 1] == a_string[j + 1]:
#             result.append(a_string[i-1:j+2])
#         i -= 1
#         j += 1

#     return ' '.join(result)

# print palindrome_substring('aabbbaa')
