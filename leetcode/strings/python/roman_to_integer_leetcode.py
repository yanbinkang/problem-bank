"""
https://leetcode.com/problems/roman-to-integer/#/description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9.

* X can be placed before L (50) and C (100) to make 40 and 90.

* C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


https://discuss.leetcode.com/topic/17110/my-straightforward-python-solution

Note: The trick is that the last letter's value is always added. Except the last one, if a letter is less than the one after it, it's value is subtracted.

O(n) time and O(k) space to store roman_map
"""
def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}

    result = 0

    for i in range(len(s) - 1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]

    return result + roman_map[s[-1]]




if __name__ == '__main__':
    print roman_to_int('IV') # 4
    print roman_to_int('VII') # 7
    print roman_to_int('IX') # 9
    print roman_to_int('XL') # 40
    print roman_to_int('XX') # 20
    print roman_to_int('MCMIV') # 1904
    print roman_to_int('MMXIV') # 2014
    print roman_to_int('XC') # 90
    print roman_to_int('DCXXI') # 621
    print roman_to_int('CD') # 621
