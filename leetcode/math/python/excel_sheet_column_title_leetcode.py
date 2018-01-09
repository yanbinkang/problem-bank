"""
https://leetcode.com/problems/excel-sheet-column-title/#/description

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

algo: When we generate the letters in the alphabet from A-Z, with zero-based indexing we have 0-25. But we're being told that 26 -> Z. Clearly we need to subtract 1 from 26 to the Z in the zero-based alphabet we've generated. Then find modulo of that.

If we have to go again, make sure the number we're going to work on also has 1 subtracted.

Do this until n gets to 0. return the joined reversed string.

Note: When dealing with any problem that has to do with division and remainder (modulo), we always append the remainder or modular. Then the carry is used again in the next loop if its greater that zero
"""
import string
def convert_to_title(n):
    capitals = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    while n > 0:
        # n, carry = divmod(n - 1, 26)
        # result += capitals[carry]

        result += capitals[ (n - 1) % 26 ]
        n = (n - 1) // 26

    return ''.join(reversed(result))

if __name__ == '__main__':
    print convert_to_title(12)
    print convert_to_title(30)
