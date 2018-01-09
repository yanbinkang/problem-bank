"""
https://leetcode.com/problems/multiply-strings/#/description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

    1. The length of both num1 and num2 is < 110.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

Algorithm:

Remember how we do multiplication?

Start from right to left, perform multiplication on every pair of digits, and add them together. Let's draw the process! From the following draft, we can immediately conclude:

    num1[i] * num2[j] will be placed at indices [i + j, i + j + 1]

O(m + n) time and sapce

READ: https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
"""
def multiply(num1, num2):
    m, n = len(num1), len(num2)

    pos = [0] * (m + n)

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            mul = int(num1[i]) * int(num2[j])
            p1 = i + j
            p2 = i + j + 1

            total = mul + pos[p2]

            pos[p1] += total // 10  # carry

            pos[p2] = (total) % 10

    result = ''

    for p in pos:
        if len(result) == 0 and p == 0:
            continue

        result += str(p)

    return '0' if len(result) == 0 else result

if __name__ == '__main__':
    print multiply('123', '45')

