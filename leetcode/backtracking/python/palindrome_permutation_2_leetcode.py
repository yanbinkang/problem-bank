"""
https://leetcode.com/problems/palindrome-permutation-ii/

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be formed.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

hint:
    1 .If a palindromic permutation exists, we just need to generate the first half of the string.

    2. To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II

https://discuss.leetcode.com/topic/22210/my-readable-python-solution-with-comments
"""
def generate_palindromes(s):
    if len(s) == 0:
        return []

    if len(s) == 1:
        return [s]

    # put the characters that have been seen twice in chars list
    chars = []
    char_set = set()

    # check for palindrome permutations; see https://leetcode.com/problems/palindrome-permutation/
    for char in s:
        if char in char_set:
            chars.append(char)
            char_set.remove(char)
        else:
            char_set.add(char)

    # none of the permutations can be palindromic
    if len(char_set) > 1:
        return []

    mid = '' if not char_set else char_set.pop()

    # put the permutations of chars into the list result
    result = []

    helper(result, [], [False]*len(chars), chars)

    return [x + mid + x[::-1] for x in result]

def helper(result, temp_list, used, chars):
    if len(temp_list) == len(chars):
        result.append(''.join(temp_list))
    else:
        for i in range(len(chars)):
            if used[i]:
                continue

            if i > 0 and chars[i - 1] == chars[i] and not used[i - 1]:
                continue

            used[i] = True
            temp_list.append(chars[i])
            helper(result, temp_list, used, chars)
            used[i] = False
            temp_list.pop()


if __name__ == '__main__':
    print generate_palindromes('aabb')
