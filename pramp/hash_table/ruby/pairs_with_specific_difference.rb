=begin
Given an array arr of distinct integers and a nonnegative integer target, write a function findPairsWithGivenDifference that returns an array of all pairs [x, y] in arr, such that x - y = target. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], target = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], target = 17
output: []
"""
'''
Brute force:

def find_pairs_with_given_difference(arr, target):
    result = []

    if len(arr) <= 1: return result

    for y in arr:
        for x in arr:
            if x - y == target:
                result.append([x, y])

    return result
=end
def find_pairs_with_given_difference(arr, target)
  result = []
  d = {}

  arr.each do |x|
    # store compliment as key
    d[x - target] = x
  end

  arr.each do |y|
    result << [d[y], y] if d.key?(y)
  end

  result
end

if $PROGRAM_NAME == __FILE__
  p find_pairs_with_given_difference([0, -1, -2, 2, 1], 1)
end
