"""
https://leetcode.com/problems/integer-to-roman/#/description

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

https://discuss.leetcode.com/topic/20821/python-simple-solution

Idea: Create an array of values and numerals. Values contain specific numbers and numerals contain corresponding roman numerals for these numbers.

Iterate through values. At each step (num // value) will give you the quotient. mutiply the quotient by the corresponding value's roman numeral in the numerals array. in the same step find the remainder for the next step by finding the num % v. Move to the next value in values and numerals array and try again
"""
def int_to_roman(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]

    res = ''

    for i, v in enumerate(values):
        res += (num // v) * numerals[i]
        num = num % v

    return res


if __name__ == '__main__':
    print int_to_roman(11)
    print int_to_roman(28)
