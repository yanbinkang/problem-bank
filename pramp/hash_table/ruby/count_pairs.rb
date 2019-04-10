=begin
https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Count pairs with given sum

Given an array of integers, and a number 'sum', find the number of pairs of integers in the array whose sum is equal to 'sum'.

Examples:

Input  :  [1, 5, 7, -1],
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  [1, 5, 7, -1, 5],
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)

Input  :  [1, 1, 1, 1],
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1],
          sum = 11
Output :  9
=end
def get_pairs_count(arr, target)
  d = {}

  arr.each do |num|
    d[num] = d.fetch(num, 0) + 1
  end

  twice_count = 0

  arr.each do |num|
    twice_count += d.fetch(target - num, 0)

    # use arr= [1, 1, 1, 1], target = 2 example to understand this if branch
    twice_count += 1 if target - num == num
  end

  (twice_count / 2).to_i
end

if $PROGRAM_NAME == __FILE__
  p get_pairs_count([1, 5, 7, -1], 6)
end
