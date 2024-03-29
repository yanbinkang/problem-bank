=begin
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9

Output: index1=1, index2=2
=end
def two_sum(numbers, target)
  first = 0
  last = numbers.length - 1

  while first < last
    return [first + 1, last + 1] if numbers[first] + numbers[last] == target

    if numbers[first] + numbers[last] > target
      last -= 1
    else
      first += 1
    end
  end
end

if $PROGRAM_NAME == __FILE__
  puts two_sum([2, 7, 11, 15], 9)
end
