"""
https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        left, right = 0, len(S) - 1

        while left < right:
            if not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            elif S[left].isalpha() and S[right].isalpha():
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1

        return ''.join(S)


if __name__ == "__main__":
    s = Solution()
    print s.reverseOnlyLetters('Test1ng-Leet=code-Q!')
    print s.reverseOnlyLetters('Qedo1ct-eeLg=ntse-T!')
