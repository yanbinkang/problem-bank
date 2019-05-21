# frozen_string_literal: true

=begin
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
=end

def longest_substring_with_k_distinct(str, k)
  window_start = 0
  max_length = 0
  char_frequency = {}

  str.size.times do |window_end|
    right_char = str[window_end]

    char_frequency[right_char] = char_frequency.fetch(right_char, 0) + 1

    # shrink the sliding wondow, until we are left with 'k'
    # distinct characters in the char_frequency
    while char_frequency.size > k
      left_char = str[window_start]
      char_frequency[left_char] -= 1

      char_frequency.delete(left_char) if char_frequency[left_char].zero?

      window_start += 1
    end

    # remember maximum length so far
    max_length = [max_length, window_end - window_start + 1].max
  end

  max_length
end

if $PROGRAM_NAME == __FILE__
  p longest_substring_with_k_distinct('araaci', 2)
  p longest_substring_with_k_distinct('araaci', 1)
  p longest_substring_with_k_distinct('cbbebi', 3)
end
