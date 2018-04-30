def sequential_search(a_list, item)
  pos = 0
  found = false

  while pos < a_list.length && !found
    if a_list[pos] == item
      found = true
    else
      pos = pos + 1
    end
  end

  return found
end

list = (1..10).to_a.shuffle
puts sequential_search(list, 5)
puts sequential_search(list, 20)
