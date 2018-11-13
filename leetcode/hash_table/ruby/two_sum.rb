=begin
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
=end
def two_sum(nums, target)
  hash_map = {}

  nums.each_with_index do |num, i|
    return [hash_map[num], i] if hash_map.include?(num)

    hash_map[target - num] = i
  end
end

if $PROGRAM_NAME == __FILE__
  p two_sum([2, 7, 11, 15], 9)
  p two_sum([0, 4, 3, 0], 0)
  p two_sum([-1, -2, -3, -4, -5], -8)
end
