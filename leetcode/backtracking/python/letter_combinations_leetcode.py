"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

https://discuss.leetcode.com/topic/3396/my-iterative-sollution-very-simple-under-15-lines

Time complexity: Assuming the average number of letters on every number is m and the length of digits string is n, then the time complexity is O(m^n) [exponential]
"""
def letter_combinations(digits):
    result = []

    if not digits:
        return result

    result.append('')

    char_map = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for digit in digits:
        letters = char_map[int(digit)]
        temp = []

        for _str in result:
            for char in letters:
                temp.append(_str + char)
        result = temp

    return result

"""
https://discuss.leetcode.com/topic/19124/python-easy-to-understand-backtracking-solution
"""
def letter_combinations_1(digits):
    result = []

    if len(digits) == 0:
        return result

    dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

    helper(digits, dic, 0, '', result)

    return result

def helper(digits, dic, start, temp_char, result):
    if len(temp_char) == len(digits):
        result.append(temp_char)
        # return

    for i in range(start, len(digits)):
        for j in dic[digits[i]]:
            helper(digits, dic, i + 1, temp_char + j, result)


if __name__ == '__main__':
    print letter_combinations('23') # ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
    print letter_combinations('')

    print('\n')
    print letter_combinations_1('23') # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print letter_combinations_1('')

