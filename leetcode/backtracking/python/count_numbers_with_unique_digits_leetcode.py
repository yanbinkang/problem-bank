"""
https://leetcode.com/problems/count-numbers-with-unique-digits/

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x <= 100, excluding [11,22,33,44,55,66,77,88,99])

https://discuss.leetcode.com/topic/47983/java-dp-o-1-solution
"""
def count_numbers_with_unique_digits(n):
    if n == 0: return 1

    result = 10
    unique_digits = 9
    available_number = 9

    while n > 1 and available_number > 0:
        unique_digits = unique_digits * available_number
        result += unique_digits
        available_number -= 1
        n -= 1

    return result

if __name__ == '__main__':
    print count_numbers_with_unique_digits(0)
    print('\n')
    print count_numbers_with_unique_digits(1)
    print('\n')
    print count_numbers_with_unique_digits(2)
    print('\n')
    print count_numbers_with_unique_digits(3)
    print('\n')
    print count_numbers_with_unique_digits(4)

