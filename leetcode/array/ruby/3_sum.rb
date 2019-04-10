=begin
https://leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

algorithm: The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.

O(n^2) time O(n) space


# https://discuss.leetcode.com/topic/22619/python-easy-to-understand-solution-o-n-n-time

In the inner while loop why do we have to  do l += 1; r -= 1 after skipping duplicates?

If we didn't skip any duplicates, then we definitely have to move r and l.

If we skipped duplicates, why do we still have to move?

Imagine nums = [-4, -1, -1 ... 5]:

i is the element -4
l is the element -1
r is the element 5
s = 0

At this point the first l is part of the result we want and we've skipped l to the last -1 (using the first inner while loop: line 62). In the next iteration we still don't want to include -1 in the result (it'll result in a duplicate). So we need to move l again, and also move r as usual. That's why!

The same explanation works for r
=end
def three_sum(nums)
  result = []
  nums.sort!

  (nums.size - 2).times do |i|
    next if i > 0 && nums[i] == nums[i - 1]

    l = i + 1
    r = nums.size - 1

    while l < r
      total = nums[i] + nums[l] + nums[r]

      if total < 0
        l += 1
      elsif total > 0
        r -= 1
      else
        result << [nums[i], nums[l], nums[r]]

        l += 1 while l < r && nums[l] == nums[l + 1]

        r -= 1 while l < r && nums[r] == nums[r - 1]

        l += 1
        r -= 1
      end
    end
  end

  result
end

if $PROGRAM_NAME == __FILE__
  p three_sum([-1, 0, 1, 2, -1, -4])
  p three_sum([0, 0, 0, 0, 0, 0])
end
