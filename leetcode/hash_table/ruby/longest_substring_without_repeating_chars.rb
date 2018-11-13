=begin
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest
substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.

https://discuss.leetcode.com/topic/25499/share-my-java-solution-using-hashset

https://discuss.leetcode.com/topic/11632/a-python-solution-85ms-o-n

https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
=end
def length_of_longest_substring(s)
  dic = {}
  left = 0
  right = 0
  count = 0
  max_length = 0

  while right < s.length
    char = s[right]

    dic[char] = dic.fetch(char, 0) + 1

    count += 1 if dic[char] > 1

    right += 1

    while count > 0
      if dic.key?(s[left])
        count -= 1 if dic[s[left]] > 1

        dic[s[left]] -= 1
      end

      left += 1
    end

    max_length = [max_length, right - left].max
  end

  max_length
end

=begin
ref: https://leetcode.com/articles/longest-substring-without-repeating-characters/#approach-2-sliding-window-accepted

By using a Set as a sliding window, checking if a character in the current can be done in O(1)

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually is defined by the start and end indices, i.e. [i, j) (left-closed, right-open).

A sliding window is a window that "slides" its two boundaries to the certain direction. For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1) (left-closed, right-open).

Back to our problem. We use a Set to store the characters in current window [i, j) (j = i initially).

Then we slide the index j to the right. If it is not in the Set, we slide j further. Doing so until s[j] is already in the HashSet.

At this point, we found the maximum size of substrings without duplicate characters start with index i. We remove string indexed at i from set and now close the window by increasing i (the else part of the code). If we do this for all i, we get our answer.

Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j

Space complexity : O(min(m, n))
=end

require 'set'
def length_of_longest_substring_1(s)
  i = 0
  j = 0
  s_max = 0

  set = Set.new

  while j < s.length
    if !set.include?(s[j])
      set << s[j]
      j += 1
      s_max = [s_max, set.length].max
    else
      set.delete(s[i])
      i += 1
    end
  end
end

def length_of_longest_substring_2(s)
  left = max_length = 0
  used = {}

  s.chars.each_with_index do |char, i|
    if used.key?(char) && left <= used[char]
      left = used[char] + 1
    else
      max_length = [max_length, i - left + 1].max
    end

    used[char] = i
  end

  max_length
end

if $PROGRAM_NAME == __FILE__
  # puts length_of_longest_substring('abcabcbb')
  # puts length_of_longest_substring('bbbbb')
  # puts length_of_longest_substring('pwwkew')
  # puts
  # puts length_of_longest_substring_1('abcabcbb')
  # puts
  puts length_of_longest_substring_2('abcabcbb')
end
