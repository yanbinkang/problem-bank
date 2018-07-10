"""
https://leetcode.com/problems/roman-to-integer/#/description

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

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
