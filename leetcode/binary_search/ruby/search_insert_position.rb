=begin
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 => 2
[1,3,5,6], 2 => 1
[1,3,5,6], 7 => 4
[1,3,5,6], 0 => 0

But why return low?

(1) When we break out of the while loop we know that, low > high. That is, low >= high+1

(2) From the invariant, we know that the index is between [low, high+1], so low <= high+1. Follwing from (1), now we know low == high+1.

(3) Following from (2), the index is between [low, high+1] = [low, low], which means that low is the desired index
    Therefore, we return low as the answer. You can also return high+1 as the result, since low == high+1

ref: https://leetcode.com/problems/search-insert-position/discuss/15101/C++-O(logn)-Binary-Search-that-handles-duplicate

Rule of thumb: Always use below for binary search!
=end
def search_insert_1(nums, target)
  low = 0
  high = nums.length - 1

  while low <= high
    mid = (low + high) / 2

    if target > nums[mid]
      low = mid + 1
    else
      high = mid - 1
    end
  end

  low
end

=begin
note:

we're using hi = len(nums) because of the case of 1 element. Eg. searchInsert([1], 2). This makes sure initially lo=0 and hi=1.

When we're in the while loop mid becames 0 and we can safely jump into the first if statement which makes the invariant false.

But when we use hi = len(nums) - 1, lo=0 and hi=0 and the invariant is already false which makes returning lo the wrong answer.
=end
def search_insert(nums, target)
  lo = 0
  hi = nums.length

  while lo < hi
    mid = (lo + hi) / 2

    if nums[mid] < target
      lo = mid + 1
    else
      hi = mid
    end
  end

  lo
end

if $PROGRAM_NAME == __FILE__
  puts search_insert([1, 3, 5, 6], 5)
  puts search_insert([1, 3, 5, 6], 2)
  puts search_insert([1, 3, 5, 6], 7)
  puts search_insert([1, 3, 5, 6], 0)
  puts search_insert([1], 2)
  puts
  puts search_insert_1([1], 2)
end
