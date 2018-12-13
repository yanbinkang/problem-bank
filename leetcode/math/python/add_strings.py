"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Solution ref -> https://leetcode.com/problems/add-strings/discuss/90474/straightforward-python-solution

Similar question: Add binary -> https://leetcode.com/problems/add-binary
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, result = 0, []

        while len(num1) > 0 or len(num2) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            result.append(temp % 10)
            carry = temp // 10

        if carry:
            result.append(carry)

        return ''.join([str(i) for i in result])[::-1]


if __name__ == "__main__":
    s = Solution()
    print s.addStrings('39', '12')
