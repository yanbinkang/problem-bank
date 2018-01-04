# https://leetcode.com/problems/repeated-dna-sequences/
def find_repeated_dna_sequences(s)
  s.chars.each_cons(10).group_by(&:join).select { |_, group| group.size > 1 }.keys
end

p find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
