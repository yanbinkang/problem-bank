=begin
https://leetcode.com/problems/majority-element/?tab=Description

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

read: https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

https://discuss.leetcode.com/topic/28601/java-solutions-sorting-hashmap-moore-voting-bit-manipulation

O(n) time O(1) space
=end
def majority_element(nums)
  major = 0
  count = 0

  nums.length.times do |i|
    major = nums[i] if count.zero?

    major == nums[i] ? count += 1 : count -= 1
  end

  major_count = nums.count(major)

  major if major_count > nums.length / 2
end

if $PROGRAM_NAME == __FILE__
  puts majority_element([1, 2, 3, 3, 3, 3, 3, 3, 10])
end
