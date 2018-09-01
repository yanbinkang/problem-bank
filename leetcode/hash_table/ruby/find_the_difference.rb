def find_the_difference(s, t)
  d = {}

  t.chars.each do |char|
    d[char] = d.fetch(char, 0) + 1
  end

  s.chars.each do |char|
    d[char] -= 1 if d.include?(char)
  end

  d.each do |key, value|
    return key if value == 1
  end
end

puts find_the_difference('abcd', 'abcde')
