"""
https://leetcode.com/problems/add-binary/#/description

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

https://discuss.leetcode.com/topic/8981/short-code-by-c

algo: Initialize carry to 0. Start from the back and add the values from a and b to carry.

Note: wrt while i >= 0 or j >= 0 or carry == 1, we add carry == 1 condition to cater for situation where carry is 1 and we've iterated over both a and b; meaning we've finished addition elements of a and b.

We can also do:

        while i >= 0 or j >= 0:
            do stuff

        if carry != 0:
            result += str(carry)

        return ''.join(reversed(list(result)))

question similar to: https://leetcode.com/problems/add-two-numbers/#/description

O(n) time and space

Note: When dealing with any problem that has to do with division and remainder (modulo), we always append the remainder or modular. Then the carry is used again in the next loop if its greater than zero
"""
def add_binary(a, b):
    result = ''
    carry = 0

    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry == 1:

        if i >= 0:
            carry += int(a[i])
            i -= 1

        if j >= 0:
            carry += int(b[j])
            j -= 1

        carry, rem = divmod(carry, 2)

        result += str(rem)

    return ''.join(reversed(result))

if __name__ == '__main__':
    print add_binary('11', '1')

