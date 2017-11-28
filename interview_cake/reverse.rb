def reverse(a_string)
  left_pointer = 0
  right_pointer = a_string.length - 1

  while left_pointer < right_pointer
    temp = a_string[right_pointer]
    a_string[right_pointer] = a_string[left_pointer]
    a_string[left_pointer] = temp

    left_pointer =+ 1
    right_pointer -= 1
  end

  return a_string
end
