=begin
https://leetcode.com/problems/search-in-rotated-sorted-array/#/description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Algo: Use Binary Search.

1. Find mid element.

2. If arr[mid] == target return mid.

 3. If above condition is false compare arr[mid] to first element in array. if the middle element is greater than or equal to the first element, you know the range from the first element to mid element is sorted.

    a. Check if the target is in this range. If so make high = mid - 1. else make low = mid + 1 meaning we'll search the other half of the array

2. If the middle element is not greater or equal to the first element, the range is not sorted and so we cannot perform binary search. So look at arr[mid:]

    a. Check if target is in this range. if so make low = mid + 1. else make high = mid - 1, meaning we need to look at lower half of array

3. If no result is found return -1
=end
def search(nums, target)
  return -1 if nums.empty?

  low, high = 0, nums.length - 1

  while low <= high
    mid = (low + high) / 2

    return mid if target == nums[mid]

    if nums[low] <= nums[mid]
      if nums[low] <= target && target <= nums[mid]
        high = mid - 1
      else
        low = mid + 1
      end
    else
      if nums[mid] <= target && target <= nums[high]
        low = mid + 1
      else
        high = mid - 1
      end
    end
  end

  -1
end

if __FILE__ == $0
  nums = [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  puts search(nums, 14)
  puts search([1], 1)
  puts search([1], 0)
end
