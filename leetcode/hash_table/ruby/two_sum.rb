def two_sum(nums, target)
  hash_map = {}

  nums.each_with_index do |num, i|
    if hash_map.include?(num)
      return [hash_map[num], i]
    else
      hash_map[target - num] = i
    end
  end
end

if __FILE__ == $0
  p two_sum([2, 7, 11, 15], 9)
  p two_sum([0, 4, 3, 0], 0)
  p two_sum([-1,-2,-3,-4,-5], -8)
end
