def binary_search(a_list, item)
  if a_list.length == 0
    return false
  else
    mid_point = a_list.length / 2
    if a_list[mid_point] == item
      return true
    else
      if item < a_list[mid_point]
        return binary_search(a_list[0...mid_point], item)
      else
        return binary_search(a_list[mid_point+1..-1], item)
      end
    end
  end
end

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
puts binary_search(testlist, 3)
puts binary_search(testlist, 13)
