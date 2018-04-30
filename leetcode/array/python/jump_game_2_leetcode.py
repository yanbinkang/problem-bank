"""
https://leetcode.com/problems/jump-game-ii/#/description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""


"""
i like this solution

https://discuss.leetcode.com/topic/80392/python-solution-with-detailed-explanation

Greedy Approach which uses "Ladder Idea from Ideserve"

- https://www.youtube.com/playlist?list=PLamzFoFxwoNgG0Q5rqfTY6ovWSTAC9mbz

- The invariant is that at a start index, we already know the maximum jump index that can be reached.

- We therefore move from index start to current_max_index and test whether we can reach further than current_max_index. Infact, we try to be greedy - we want to pick the next start point which would make us reach the farthest from current_max_index.

- Once we update the next start point, we recognize that we took a single jump.

- Take special note of initial conditions: current_max_index, start, jumps = 0, 0, 0. This initialization helps us to tackle cases likes nums = [1]. Other when length of nums is more than 1, the first jump takes us to start index 0 and sets current_max_index to nums[0].

"""
def jump_3(nums):
    current_max_index, start, jumps = 0, 0, 0

    while start < len(nums):
        if current_max_index >= len(nums) - 1:
            return jumps

        for i in range(start, current_max_index + 1):
            if nums[i] + i > current_max_index:
                start = i
                current_max_index = nums[i] + i

        jumps += 1

        if jump > current_max_index:
            break


def jump(nums):
    n, left, right, step = len(nums), 0, 0, 0

    while right < n - 1:
        step += 1
        max_end = right + 1

        for i in range(left, right + 1):
            if i + nums[i] >= n - 1:
                return step
            max_end = max(max_end, i + nums[i])

        left, right = right + 1, max_end

    return step

def jump_2(nums):
    n, step, end, maxend = len(nums), 0, 0, 0

    while end < n - 1:
        step += 1

        for i in range(end + 1):
            if i + nums[i]  >= n - 1:
                return step
            maxend = max(maxend, i + nums[i])

        if end == maxend:
            break

        end = maxend

    return 0 if n == 1 else -1


def jump_white_pages(nums):
    if not nums or len(nums) == 1:
        return 'failure'

    left, right, current_max_index = 0, 0, 0
    result = []

    i = 0

    while i < len(nums):
        if i > current_max_index: break

        if i > right:
            right = current_max_index
            result.append(left)

        if nums[i] + i > current_max_index:
            current_max_index = nums[i] + i
            left = i

        i += 1

    if i > right and result and result[-1] != right:
        result.append(right)

    if left >= len(nums) - 1:
        return ', '.join([str(num) for num in result]) + ', out'
    else:
        return 'failure'


if __name__ == '__main__':
    print jump([2, 3, 1, 1, 4])
    print jump([4, 1, 1, 3, 1, 1, 1])
    print('\n')
    print jump_2([2, 3, 1, 1, 4])
    print jump_2([2, 0, 0, 1, 4])
    print jump_2([2])
    print('\n')
    print jump_3([2, 3, 1, 1, 4])
    print jump_3([2, 0, 0, 1, 4])
    print('\n')
    print jump_white_pages([2, 0, 0, 1, 4])
    print jump_white_pages([4, 1, 1, 3, 1, 1, 1])
    print jump_white_pages([1, 4, 3, 7, 1, 2, 6, 7, 6, 10])
    print jump_white_pages([5, 6, 0, 4, 2, 4, 1, 0, 0, 4])
    print jump_white_pages([0])



