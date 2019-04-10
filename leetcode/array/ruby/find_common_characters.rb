=begin
https://leetcode.com/problems/find-common-characters/description/

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:

    1. 1 <= A.length <= 100
    2. 1 <= A[i].length <= 100
    3. A[i][j] is a lowercase letter

ref: https://leetcode.com/problems/find-common-characters/discuss/247592/Java-Straight-Forward
=end
def common_chars(a)
  result = []

  global_histogram = [Float::INFINITY] * 26

  a.each do |word|
    temp = [0] * 26

    # convert char to integer between 1 - 26
    word.chars.each do |char|
      temp[char.ord - 'a'.ord] += 1
    end

    26.times do |j|
      # We're using min because we only care about
      # minimum number of chars that chow up in all strings
      global_histogram[j] = [global_histogram[j], temp[j]].min
    end
  end

  global_histogram.each_with_index do |val, i|
    val.times do
      result << (i + 'a'.ord).chr
    end
  end

  result
end

def common_chars1(a)
  result = []
  global_store = {}

  ('a'..'z').each do |char|
    global_store[char] = Float::INFINITY
  end

  a.each do |word|
    temp_store = {}
    word.chars.each do |char|
      temp_store[char] = temp_store.fetch(char, 0) + 1
    end

    global_store.each do |key, _value|
      # for cases where key exists in global_store but not temp_store
      temp_store_key = temp_store[key].nil? ? 0 : temp_store[key]

      global_store[key] = [global_store[key], temp_store_key].min
    end
  end

  global_store.each do |key, value|
    value = 0 if value == Float::INFINITY

    value.times do
      result << key
    end
  end

  result
end

if $PROGRAM_NAME == __FILE__
  p common_chars(["bella","label","roller"])
  p common_chars(["cool","lock","cook"])
  puts
  p common_chars1(["bella","label","roller"])
  p common_chars1(["cool","lock","cook"])
end
