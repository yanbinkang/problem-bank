=begin
https://leetcode.com/problems/3sum-closest/#/description

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
=end
def three_sum_closest(nums, closest)
  nums.sort!

  closest_so_far = nums[0] + nums[1] + nums[2]

  (nums.size - 2).times do |i|
    left = i + 1
    right = nums.size - 1

    while left < right
      total = nums[i] + nums[left] + nums[right]

      return total if total == target

      if (total - target).abs < (closest_so_far - target).abs

        # there is a smaller difference between
        # the absolute value of (total - target)
        # than there is between (closest_so_far - target)

        # which means total is closer to target than closest_so_far
        closest_so_far = total
      end

      if total < target
        left += 1
      elsif total > target
        right -= 1
      end
    end
  end

  closest_so_far
end
