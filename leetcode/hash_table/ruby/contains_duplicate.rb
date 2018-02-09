require 'set'

def contains_duplicate(nums)
  hash_map = {}

  nums.each do |num|
    hash_map[num] = hash_map.fetch(num, 0) + 1
  end

  hash_map.each do |key, value|
    return true if value > 1
  end

  false
end

def contains_duplicate_alt(nums)
  num_set = Set.new

  nums.each do |num|
    if num_set.include?(num)
      return true
    else
      num_set.add(num)
    end
  end

  false
end


if __FILE__ == $0
  nums = [*1..10]
  nums1 = [*1..10] + [10]

  p contains_duplicate(nums)
  p contains_duplicate_alt(nums)
  puts
  p  contains_duplicate(nums1)
  p contains_duplicate_alt(nums1)
end
