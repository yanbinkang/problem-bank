"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false

ref: https://discuss.leetcode.com/topic/101041/python-solution-with-detailed-explanation

algo: count the number of L, R, U, D moves.

L, R should equal U, D moves
"""
def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
