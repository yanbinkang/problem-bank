"""
https://leetcode.com/problems/reverse-integer/#/description

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if not x or x == 0: return 0

    x = list(str(x))

    sign = None

    # '-' is the first char, reverse the rest
    if x[0] == '-':
        sign = x[0]

        reverse_char(x, 1, len(x) - 1)
    else:
        # reverse the whole string
        reverse_char(x, 0, len(x) - 1)

    x = ''.join(x)

    result = int(sign + x[1:]) if sign else int(x)

    return 0 if abs(result) > 2**31 else result


def reverse_char(a_list, first, last):
    while first < last:
        temp = a_list[first]
        a_list[first] = a_list[last]
        a_list[last] = temp

        first += 1
        last -= 1


if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(901000))
