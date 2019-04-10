=begin
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.

Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
=end
def find_length_of_LCIS(nums)
  left = 0
  right = 0
  max_length = 1

  return 0 if nums.size.zero?

  (1...nums.size).each do |i|
    if nums[i - 1] < nums[i]
      right += 1

      max_length = [max_length, right - left + 1].max
    else
      left = right = i
    end
  end

  max_length
end

def find_length_of_LCIS_DP(nums)
  return 0 if nums.size.zero?

  dp = [0] * nums.size
  max_length = 1
  dp[0] = 1

  (1...nums.size).each do |i|
    dp[i] = if nums[i] > nums[i - 1]
              dp[i - 1] + 1
            else
              1
            end

    max_length = [max_length, dp[i]].max
  end

  max_length
end

if $PROGRAM_NAME == __FILE__
  puts find_length_of_LCIS([1, 3, 5, 4, 7])
  puts
  puts find_length_of_LCIS_DP([1, 3, 5, 4, 7])
end
