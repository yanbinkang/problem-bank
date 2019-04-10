=begin
https://leetcode.com/problems/search-in-rotated-sorted-array-ii

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

ref: https://discuss.leetcode.com/topic/20593/python-easy-to-understand-solution-with-comments

O(n) worst case. ref: https://discuss.leetcode.com/topic/310/when-there-are-duplicates-the-worst-case-is-o-n-could-we-do-better/2

Yes, when there could be duplicates in the array, the worst case is O(n).

To explain why, consider this sorted array 1111115, which is rotated to 1151111.

Assume left = 0 and mid = 3, and the target we want to search for is 5. Therefore, the condition A[left] == A[mid] holds true, which leaves us with only two possibilities:

    1. All numbers between A[left] and A[right] are all 1's.
    2. Different numbers (including our target) may exist between A[left] and A[right].

As we cannot determine which of the above is true, the best we can do is to move left one step to the right and repeat the process again. Therefore, we are able to construct a worst case input which runs in O(n), for example: the input 11111111...115.
=end
def search(nums, target)
  l = 0
  r = nums.size - 1

  while l <= r
    mid = (l + r) / 2

    return true if nums[mid] == target

    # at this point nums[mid] is not what we're searching for, so if there is a duplicate number thats the same as mid we want to exclude it from our search in the next iteration
    l += 1 while l < mid && nums[l] == nums[mid]

    if nums[l] <= nums[mid]
      if nums[l] <= target && target <= nums[mid]
        r = mid - 1
      else
        l = mid + 1
      end
    elsif nums[mid] <= target && target <= nums[r]
      l = mid + 1
    else
      r = mid - 1
    end
  end

  false
end
