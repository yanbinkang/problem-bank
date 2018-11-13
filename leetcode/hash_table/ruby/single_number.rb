=begin
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
=end
def single_number(nums)
  dic = {}

  nums.each do |num|
    dic[num] = dic.fetch(num, 0) + 1
  end

  dic.each do |key, value|
    return key if value == 1
  end
end

# implemented without extra memory
def single_number_2(nums)
  res = 0

  nums.each do |num|
    res ^= num
  end

  res
end

if $PROGRAM_NAME == __FILE__
  puts single_number([2, 2, 1])
  puts single_number_2([4, 1, 2, 1, 2])
end
