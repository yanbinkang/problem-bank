def has_palindrome_permutation(the_string):
    parity_map = {}

    for char in the_string:
        if char in parity_map:
            parity_map[char] = not parity_map[char]
        else:
            parity_map[char] = True

    odd_seen = False

    for has_odd_parity in parity_map.itervalues():
        if has_odd_parity:
            if odd_seen:
                return False
            else:
                odd_seen = True

    return True



# def permutation_palindrome(a_string):
#     stack = []
#     sorted_str = sorted(a_string)
#     pali = True
#     for char in sorted_str:
#         stack.append(char)

#     while len(stack) > 1:
#         first = stack.pop(0)
#         next_str = stack.pop(0)
#         if not first == next_str:
#             pali = False

#     return pali

print has_palindrome_permutation("ivicc")
print has_palindrome_permutation("civic")
print has_palindrome_permutation("livci")
print has_palindrome_permutation("civil")
print has_palindrome_permutation("anna")
print has_palindrome_permutation("mom")
