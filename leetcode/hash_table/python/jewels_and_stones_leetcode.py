"""
https://leetcode.com/problems/jewels-and-stones/description/

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:

* S and J will consist of letters and have length at most 50.
* The characters in J are distinct.
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        d = {}

        for char in S:
            d[char] = d.get(char, 0) + 1

        for jewel in J:
            count += d.get(jewel, 0)

        return count


class Solution1(object):
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for jewel in J:
            count += S.count(jewel)

        return count


if __name__ == '__main__':
    res = Solution()
    print res.numJewelsInStones('aA', 'aAAbbbb')
