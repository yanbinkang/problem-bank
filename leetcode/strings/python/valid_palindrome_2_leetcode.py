"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

O(n) time O(1) space
"""
# ref: https://discuss.leetcode.com/topic/103910/consice-java-solution
"""
algo: Follow normal way (two pointers) to check if s is palindrome. When two chars are not equal, try to skip (pseudo delete) either left one or right one and continue checking.
"""
def valid_palindrome_1(s):
    if not s: return True

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # delete one character to the left or to the right
            # 'abca' becomes 'aca' or 'aba'
            if is_pal(s[:i] + s[i + 1:]) or is_pal(s[:j] + s[j + 1:]):
                return True
            else:
                return False

    return True


def is_pal(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l]  == s[r]:
            l += 1
            r -= 1
        else:
            return False

    return True

# ref: https://discuss.leetcode.com/topic/103941/java-solution-ispalindrome
def valid_palindrome(s):
    i, j = 0, len(s) - 1

    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    if i >= j: return True

    if is_palin(s, i + 1, j) or is_palin(s, i, j - 1):
        return True
    else:
        return False


def is_palin(s, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False

    return True




if __name__ == '__main__':
    print valid_palindrome('aba')
    print valid_palindrome('abca')
