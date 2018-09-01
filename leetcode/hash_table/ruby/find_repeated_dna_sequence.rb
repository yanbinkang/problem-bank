require 'set'
def find_repeated_dna_sequences(s)
  repeat, seen = Set.new, Set.new

  i = 0

  while i + 9 < s.length
    substring = s[i..i + 9]

    if seen.include?(substring)
      repeat << substring
    else
      seen << substring
    end

    i += 1
  end

  repeat.to_a
end

if __FILE__ == $0
  s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
  p find_repeated_dna_sequences(s)
end
