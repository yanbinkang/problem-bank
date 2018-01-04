def palindromic_decomposition(s):
    res = []
    find_palindrome(s, [], res)

    return res

def find_palindrome(s, p_list, res):
    if len(s) == 0:
        res.append(p_list)

    for i in range(1, len(s)+1):
        if is_palindrome(s[:i]):
            find_palindrome(s[i:], p_list + [s[:i]], res)

def is_palindrome(s):
    return s == s[::-1]

print palindromic_decomposition("aab")

