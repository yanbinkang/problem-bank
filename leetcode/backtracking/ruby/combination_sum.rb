=begin
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
=end
def combination_sum(candidates, target)
  result = []

  helper(candidates, target, 0, result, [])

  result
end

def helper(candidates, target, start, result, temp_array)
  return if target < 0

  if target.zero?
    result << ([] + temp_array)
  else
    (start...candidates.size).each do |i|
      temp_array << candidates[i]
      helper(candidates, target - candidates[i], i, result, temp_array)

      temp_array.pop
    end
  end
end

if $PROGRAM_NAME == __FILE__
  p combination_sum([2, 3, 5], 8)
  p combination_sum([2, 3, 6, 7], 7)
end
