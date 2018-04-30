"""
https://leetcode.com/problems/integer-to-english-words/#/description

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2**31 - 1.

For example,

123 -> "One Hundred Twenty Three"

12345 -> "Twelve Thousand Three Hundred Forty Five"

1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

https://discuss.leetcode.com/topic/23054/my-clean-java-solution-very-easy-to-understand

https://discuss.leetcode.com/topic/39814/python-clean-solution
"""
class Solution(object):
    def __init__(self):
        self.less_than_20 = ['', 'One', 'Two', 'Three',
                            'Four', 'Five', 'Six', 'Seven',
                            'Eight', 'Nine', 'Ten', 'Eleven',
                            'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.tens = ['', 'Ten', 'Twenty', 'Thirty',
                    'Forty', 'Fifty', 'Sixty', 'Seventy',
                    'Eighty', 'Ninety']

        self.thousands = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    def number_to_words(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        word = ''
        i = 0

        while num > 0:
            if num % 1000 != 0:
                word = self.helper(num % 1000) + self.thousands[i] + ' ' + word

            num = num / 1000
            i += 1

        return word.strip()

    def helper(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.less_than_20[num] + ' '
        elif num < 100:
            return self.tens[num / 10] + ' ' + self.helper(num % 10)
        else:
            return self.less_than_20[num / 100] + ' Hundred ' + self.helper(num % 100)

if __name__ == '__main__':
    s = Solution()
    print s.number_to_words(34)
    print('\n')
    print s.number_to_words(123)
    print('\n')
    print s.number_to_words(12345)
    print('\n')
    print s.number_to_words(12345671111234)
    print('\n')
    print s.number_to_words(1500000)

