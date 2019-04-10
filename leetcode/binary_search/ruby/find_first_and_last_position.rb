=begin
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

ref: https://discuss.leetcode.com/topic/6327/a-very-simple-java-solution-with-only-one-binary-search-algorithm

ref: https://discuss.leetcode.com/topic/16486/9-11-lines-o-log-n

Algo:

The function is a simple binary search, telling me the first index where I could insert a number n into nums to keep it sorted.

Thus, if nums contains target, I can find the first occurrence with search(target). I do that, and if target isn't actually there, then I return [-1, -1].

Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1, which of course is one index behind the last index containing target, so all I have left to do is subtract 1
=end
def search_range(nums, target)
  first = first_target_index(nums, target)

  # nums is empty or index isn't where target is located in nums
  return [-1, -1] if first == nums.size || nums[first] != target

  [first, first_target_index(nums, target + 1) - 1]
end

def first_target_index(nums, target)
  lo = 0
  hi = nums.size - 1

  while lo <= hi
    mid = (lo + hi) / 2

    if target > nums[mid]
      lo = mid + 1
    else
      hi = mid - 1
    end
  end

  lo
end

if $PROGRAM_NAME == __FILE__
  p search_range([5, 7, 7, 8, 8, 10], 8)
  p search_range([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20], 5)
  p search_range([], 0)
end
