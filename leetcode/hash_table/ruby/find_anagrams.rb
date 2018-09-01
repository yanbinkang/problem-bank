def find_anagrams(s, p)
  results = []

  return results if p.length > s.length

  d = {}

  p.chars.each do |char|
    d[char] = d.fetch(char, 0) + 1
  end

  count = p.length

  left, right = 0, 0

  while right < s.length
    if d.include?(s[right])
      count -= 1 if d[s[right]] > 0

      d[s[right]] -= 1
    end

    right += 1

    while count == 0
      if d.include?(s[left] )
        d[s[left]] += 1

        count += 1 if d[s[left]] > 0
      end

      results << left if right - left == p.length

      left += 1
    end
  end

  results
end

if __FILE__ == $0
  puts find_anagrams('cbaebabacd', 'abc').inspect
  p find_anagrams('abab', 'ab')
  p find_anagrams('aa', 'bb')
  p find_anagrams('baa', 'aa')
end
