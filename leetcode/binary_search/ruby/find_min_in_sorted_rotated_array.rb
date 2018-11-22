=begin
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Algo:

Classic binary search problem.

Looking at subarray with index [start, end]. We can find out that if the first member is less than the last member, there's no rotation in the array. So we could directly return the first element in this subarray.

If the first element is larger than the last one, then we compute the element in the middle, and compare it with the first element.

If value of the element in the middle is larger than the first element, we know the rotation is at the second half of this array. Else, it is in the first half in the array.

https://discuss.leetcode.com/topic/4100/compact-and-clean-c-solution
=end
def find_min(nums)
  lo = 0
  hi = nums.length - 1

  while lo < hi
    return nums[lo] if nums[lo] < nums[hi]

    mid = (lo + hi) / 2

    if nums[mid] >= nums[lo]
      lo = mid + 1
    else
      hi = mid
    end
  end

  nums[lo]
end
