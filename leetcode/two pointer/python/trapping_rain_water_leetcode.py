"""
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

solution: O(n) time O(1) space

https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c++-code:-O(n)-time-O(1)-space?page=4

Here is my idea: instead of calculating area by height*width, we can think it in a cumulative way. In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water from the lower part. For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.

WHEN IN DOUBT LOAD CODE IN PYTHON TUTOR AND STEP THOUGH CODE!!

Keep two pointers, call them left and right. Also keep track of two maximum heights, call them max_left and max_left.

0. While left is less than or equal to right

1. If height of bar on left is less than or equal to height of bar on far left, find check if the max_left has changed. If so update it. If it hasn't changed, we on a bar that is shorter than the max_left, which means water can be stored there so update the result. Then move the left pointer

2. If the height of the right bar is greater than that of the left, shift focus to the far right and follow steps as given above (1).

3. If condition in step zero becomes false, break out of the loop.

4. Finally, return the result.
"""
def trap(height):
    left, right, result = 0, len(height) - 1, 0
    max_left, max_right = 0, 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                result += max_left - height[left]

            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                result += max_right - height[right]

            right -= 1

    return result


if __name__ == '__main__':
    print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
