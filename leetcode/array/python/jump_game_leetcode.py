"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

solution: https://discuss.leetcode.com/topic/4911/linear-and-simple-solution-in-c/10
"""
def can_jump(nums):
    max_jump_so_far = 0

    for i in range(len(nums)):
        if i > max_jump_so_far: return False

        if nums[i] + i > max_jump_so_far:
            max_jump_so_far = nums[i] + i

        if max_jump_so_far >= len(nums) - 1: return True

    # for i, num in enumerate(nums):
    #     # max_jump_so_far cannot reach index i
    #     if max_jump_so_far < i: return False

    #     max_jump_so_far = max(max_jump_so_far, i + num)

    #     # max_jump_so_far can reach the last index
    #     if max_jump_so_far >= len(nums) - 1: return True

def can_jump_2(nums):
    goal = len(nums) - 1

    for i in reversed(range(len(nums))):
        if i + nums[i] >= goal:
            goal = i

    return not goal

if __name__ == '__main__':
    print can_jump([2, 3, 1, 1, 4])
    print can_jump([3, 2, 1, 0, 4])
    print can_jump([1])
