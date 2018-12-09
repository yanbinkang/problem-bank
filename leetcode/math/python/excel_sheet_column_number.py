"""
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

ref: https://leetcode.com/problems/excel-sheet-column-number/discuss/52289/Explanation-in-Python
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        total = 0

        for exp, char in enumerate(s):
            total += (ord(char) - 65 + 1) * (26**exp)
            # (ord(char) - 65 + 1) =>  change char to integer and add 1 because we want A to equal 1

            # (26**exp) => [A..Z] covers first 26 letters in Alphabet == 26 ** 0 == 1. i.e A = 1, B = 2 etc.
            # For AB, the first A means we've moved into the next set of 26 characters.
            # So 26**exp == (26 ** 1) will give us start of the column. Then we just add B == 2 to get the answer
            # i.e 26 + 2 == 28
            # WHEN IN DOUBT OPEN EXCEL AND CHECK OUT THE COLUMNS!

        return total


if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber('AB')
    print s.titleToNumber('YZ')
    print s.titleToNumber('CAA')
