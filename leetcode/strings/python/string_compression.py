"""
https://leetcode.com/problems/string-compression/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

solution ref: https://leetcode.com/problems/string-compression/discuss/122241/Python-solution-with-detailed-explanation
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rptr, wptr = 0, 0
        while rptr < len(chars):
            ch, counter = chars[rptr], 0
            while rptr < len(chars) and chars[rptr] == ch:
                rptr, counter = rptr + 1, counter + 1
            chars[wptr], wptr = ch, wptr + 1
            if counter > 1:
                for c in str(counter):
                    chars[wptr], wptr = c, wptr + 1

        return wptr


if __name__ == "__main__":
    s = Solution()
    print(
        s.compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
