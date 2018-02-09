def contains_nearby_duplicate(num, k)
  dic = {}

  nums.each_with_index do |num, i|
    if dic.include?(num) && i - dic[num] <= k
      return true
    end

    dic[num] = i
  end

  return false
end
