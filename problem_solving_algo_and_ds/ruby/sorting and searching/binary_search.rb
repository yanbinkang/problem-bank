def binary_search(a_list, item)
  first = 0
  last = a_list.length - 1
  found = false

  while first <= last && !found
    mid_point = (first + last) / 2
    if a_list[mid_point] == item
      found = true
    else
      if item < a_list[mid_point]
        last = mid_point - 1
      else
        first = mid_point + 1
      end
    end
  end

  return found
end

a_list = [2, 3, 5, 8, 9, 12, 34, 56]
puts binary_search(a_list, 2)
