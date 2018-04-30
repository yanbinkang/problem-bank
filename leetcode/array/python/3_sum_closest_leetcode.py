"""
https://leetcode.com/problems/3sum-closest/#/description

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def threeSumClosest(nums, target):
    nums.sort()

    closest_so_far = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                return total

            if abs(total - target) < abs(closest_so_far - target):
                # total is closer to target than closest_so_far
                closest_so_far = total

            if total < target:
                # since array is sorted, get closer to target
                left += 1
            elif total > target:
                right -= 1

    return closest_so_far

if __name__ == '__main__':
    print threeSumClosest([-1, 2, 1, -4], 1)

