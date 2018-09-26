=begin
https://leetcode.com/problems/longest-consecutive-sequence/#/description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Ref:
https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak

First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n)

Overall complexity: O(n) + O(1) * O(k) + O(n) = O(n)
=end
require 'set'
require_relative 'disjoint_set'
def longest_consecutive(nums)
  nums = Set.new(nums)
  best_so_far = 0

  nums.each do |x|
    if !nums.include?(x - 1)
      y = x + 1
      while nums.include?(y)
        y += 1
      end

      best_so_far = [best_so_far, y - x].max
    end
  end

  best_so_far
end

def longest_consecutive_1(nums)
  ds = DisjointSet.new

  nums, dic, count = Set.new(nums), {}, 0

  nums.each do |num|
    ds.make_set(num)
  end

  nums.each do |num|
    # union consecutive numbers together
    ds.union(num, num - 1) if nums.include?(num - 1)

    # union consecutive numbers together
    ds.union(num, num + 1) if nums.include?(num + 1)
  end

  nums.each do |num|
    set_rep = ds.find_set(num)
    dic[set_rep] = dic.fetch(set_rep, []) << num
  end

  dic.each_key do |key|
    count = [count, dic[key].length].max
  end

  count
end

if __FILE__ == $0
  puts longest_consecutive([100, 4, 200, 1, 3, 2])
  puts longest_consecutive([0, 0])
  puts longest_consecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645])
  puts longest_consecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7])
  puts
  puts longest_consecutive_1([100, 4, 200, 1, 3, 2])
  puts longest_consecutive_1([0, 0])
  puts longest_consecutive_1([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645])
  puts longest_consecutive_1([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7])
end
