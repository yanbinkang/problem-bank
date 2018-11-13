=begin
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

algo:

The basic idea is that we iterate through the input array and mark elements as negative using nums[nums[i] -1] = -nums[nums[i]-1]. In this way all the numbers that we have seen will be marked as negative. In the second iteration, if a value is not marked as negative, it implies we have never seen that index before, so just add it to the return list.

ref: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92956/Java-accepted-simple-solution
=end
def find_disappeared_numbers_1(nums)
  result = []

  nums.length.times do |i|
    idx = nums[i].abs - 1

    nums[idx] = -nums[idx] if nums[idx] > 0
  end

  nums.length.times do |i|
    result << i + 1 if nums[i] > 0
  end

  result
end

def find_disappeared_numbers(nums)
  nums.length.times do |i|
    index = nums[i].abs - 1
    nums[index] = -(nums[index]).abs
  end

  res = []
  nums.length.times do |i|
    res << i + 1 if nums[i] > 0
  end

  res
end

if $PROGRAM_NAME == __FILE__
  puts find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
end
