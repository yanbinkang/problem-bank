=begin
https://leetcode.com/problems/permutations/

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

read carefully:

https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning
=end
def permute(nums)
  result = [[]]

  nums.each do |num|
    temp = []

    result.each do |arr|
      (arr.length + 1).times do |i|
        temp << arr[0...i] + [num] + arr[i...arr.length]
      end
    end

    result = temp
  end

  result
end

def permute_backtracking(nums)
  result = []

  helper(nums, result, [])

  result
end

def helper(nums, result, temp_list)
  if temp_list.length == nums.length
    result << [] + temp_list
  else
    nums.length.times do |i|
      next if temp_list.include?(nums[i])

      temp_list << nums[i]
      helper(nums, result, temp_list)
      temp_list.pop
    end
  end
end

if __FILE__ == $0
  p permute([1, 2, 3])
  puts
  p permute_backtracking([1, 2, 3])
end
