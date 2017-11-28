def zero_subarray(arr)
  dict = {}
  sum = 0
  i = 0
  result = []

  while i < arr.length
    sum += arr[i]

    if dict.keys.include?(sum)
      sub_array = arr[dict[sum]+1..i]
      result.push(sub_array)

      if sub_array.size > 2 && sub_array.include?(0)
        result.push(sub_array[sub_array.index(0)+1..-1])
      end
    else
      dict[sum] = i
    end

    i += 1
  end

  output = ""

  if result
    for sub in result do
      output += sub.join(", ") + "\n"
    end
  end

  return output
end


arr_1 = [6, 0, 1, 2, 3, 4, -10]
arr_2 = [1, 0]
arr_3 = [4, 0, 1, 2, -3]
arr_4 = [3, 1, 2, 3]

puts zero_subarray(arr_1)
puts ""
puts zero_subarray(arr_2)
puts ""
puts zero_subarray(arr_3)
puts ""
puts zero_subarray(arr_4)
