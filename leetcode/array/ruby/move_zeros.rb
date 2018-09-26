=begin
https://leetcode.com/problems/move-zeroes/?tab=Description

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
=end
def move_zeros(nums)
  return if nums.empty?

  insert_pos = 0

  nums.each do |num|
    if !num.zero?
      nums[insert_pos] = num
      insert_pos += 1
    end
  end

  while insert_pos < nums.length
    nums[insert_pos] = 0
    insert_pos += 1
  end
end

if __FILE__ == $0
  nums = [0, 1, 0, 3, 12]
  move_zeros(nums) # [1, 3, 12, 0, 0]
  puts nums
end
