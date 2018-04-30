def rev_str(a_string)
  if a_string.length <= 1
    return a_string
  else
    return a_string[-1] + rev_str(a_string[0..-2])
  end
end

puts rev_str("albert")
