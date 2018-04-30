def two_sum(numbers, target)
  first = 0
  last = numbers.length - 1

  while first < last

    if numbers[first] + numbers[last] == target
      return [first + 1, last + 1]
    elsif numbers[first] + numbers[last] > target
      last -= 1
    else
      first += 1
    end

  end
end

p two_sum([2, 7, 11, 15], 9)
