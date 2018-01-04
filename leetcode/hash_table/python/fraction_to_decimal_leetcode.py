"""
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
def fraction_to_decimal(numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''
    head, remainder = divmod(abs(numerator), abs(denominator))
    tail, seen = '', {}

    while remainder != 0:
        if remainder in seen:
            tail = tail[:seen[remainder]] + '(' \
                    + tail[seen[remainder]:] + ')'
            break
        seen[remainder] = len(tail)
        digit, remainder = divmod(remainder*10, abs(denominator))
        tail += str(digit)

    return sign + str(head) + (tail and '.' + tail)

def fraction_to_decimal_alt(numerator, denominator):
    n, remainder = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator * denominator < 0 else ''
    result = [sign + str(n), '.']
    stack = []

    while remainder not in stack:
        stack.append(remainder)
        n, remainder = divmod(remainder * 10, abs(denominator))
        result.append(str(n))

    idx = stack.index(remainder)
    result.insert(idx + 2, '(')
    result.append(')')

    return ''.join(result).replace('(0)', '').rstrip('.')

# https://discuss.leetcode.com/topic/9778/python-solution
def fraction_to_decimal_3(numerator, denominator):
    result = ''

    if numerator / denominator < 0:
        result += '-'
    elif numerator % denominator == 0:
        return str(numerator / denominator)

    numerator = abs(numerator)
    denominator = abs(denominator)

    result += str(numerator / denominator)

    result += '.'

    numerator = numerator % denominator

    i = len(result)

    table = {}

    while numerator != 0:
        if numerator not in table.keys():
            table[numerator] = i
        else:
            i = table[numerator]
            result = result[:i] + '(' + result[i:] + ')'

            return result
        numerator = numerator * 10
        result += str(numerator / denominator)
        numerator = numerator % denominator

        i += 1

    return result

if __name__ == '__main__':
    print fraction_to_decimal(2, 3)
    print fraction_to_decimal_alt(2, 3)
    print fraction_to_decimal_3(2, 3)

