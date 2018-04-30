def selection_sort(a_list)
  ((a_list.length) - 1).downto(1).each do |fill_slot|
    position_of_max = 0
    1.upto(fill_slot).each do |location|
      if a_list[location] > a_list[position_of_max]
        position_of_max = location
      end
    end

    temp = a_list[fill_slot]
    a_list[fill_slot] = a_list[position_of_max]
    a_list[position_of_max] = temp

  end

  return a_list
end

my_list = [54,26,93,17,77,31,44,55,20]
p selection_sort(my_list)
