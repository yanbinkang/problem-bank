"""
solution: http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""
def longest_palindromic_substr(string):
    max_length = 1
    start = 0
    str_len = len(string)

    # one by one consider every character as center point of even and length palindromes
    for i in range(1, str_len):
        low = i - 1
        high = i
        while (low >= 0 and high < str_len and string[low] == string[high]):
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    # find the longest odd length palindrome with center as i
    low = i - 1
    high = i + 1
    while (low >= 0 and high < str_len and string[low] == string[high]):
        if (high - low + 1 > max_length):
            start = low
            max_length = high - low + 1
        low -= 1
        high += 1

    lps = string[start:start+max_length]
    print "Longest palindrome substring is: %s" % (lps)

    return max_length

if __name__ == '__main__':
    string = 'forgeeksskeegfor'
    print "Length is %r" % (longest_palindromic_substr(string))



"""
# brute force solution
# O(n^3) time
# O(1) space

def longest_palindromic_substring(string):
    i = 0
    max_size = 0
    while i < len(string):
        j = 0
        while j < len(string):
            if i != j and i < j:
                sub_str = string[i:j+1]
            if is_palindrome(sub_str) and len(sub_str) > max_size:
                max_size = len(sub_str)
                longest_pali = sub_str
            j += 1
        i += 1

    return longest_pali


def is_palindrome(string):
    return string == string[::-1]

inp = 'forgeeksskeegfor'
print longest_palindromic_substring(inp)

"""
