"""
solution: http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
"""
def longest_pal_substr(string):
    n = len(string)

    table = [[None for i in range(n+1)] for j in range(n+1)]

    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        table[i][i] = True

    # check for sub-string of length 2
    start = 0
    for i in range(n-1):
        if string[i] == string[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2

    # check for lengths greater than 2. k is the length of substring
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i + k - 1
            if table[i + 1][j - 1] and string[i] == string[j]:
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    lps = string[start:start+max_length]
    print "Longest palindrome substring is: %s" % (lps) + "\n"

    # print_substr(string, start, start + max_length - 1)

    return max_length


def print_substr(string, low, high):
    for  i in range(low, high+1):
        print string[i]


if __name__ == '__main__':
    print "Length is: %r" % (longest_pal_substr('agbdba'))
    print "\n"
    print "Length is: %r" % (longest_pal_substr('forgeeksskeegfor'))


