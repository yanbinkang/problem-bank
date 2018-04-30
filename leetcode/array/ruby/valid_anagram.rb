def is_anagram1(s, t)
  s.chars.sort == t.chars.sort
end

def is_anagram2(s, t)
  h1, h2 = {}, {}

  s.each_char do |char|
    h1[char] = h1.fetch(char, 0) + 1
  end

  t.each_char do |char|
    h2[char] = h2.fetch(char, 0) + 1
  end

  h1 == h2
end

def is_anagram3(s, t)
  dic1, dic2 = [0] * 26, [0] * 26

  s.each_byte do |byte|
    dic1[byte - 'a'.ord] += 1
  end

  t.each_byte do |byte|
    dic2[byte - 'a'.ord] += 1
  end

  dic1 == dic2
end


p is_anagram1('anagram', 'nagaram')
p is_anagram2('rat', 'car')
puts
p is_anagram2('anagram', 'nagaram')
p is_anagram2('rat', 'car')
puts
p is_anagram3('anagram', 'nagaram')
p is_anagram3('rat', 'car')
