=begin
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

ref: https://leetcode.com/problems/word-break/#/solution

Time complexity : O(n^2). For every starting index, the search can continue till the end of the given string.

Space complexity : O(n). Queue of at most n size is needed.

Algo: We use a queue and a visited array equal to the size of the string initialized with zero's

Before the process starts append 0 (which represents the start of the string) to the queue.

While the queue is not empty:
    1. look for substrings in string which is in the dictionary
    2. If we find such a substring, insert its last index into front of the queue.

    This means we've found one split. And the inserted index tells us that after the process we're running, check if there exist another substring (starting from where the previous substring ended to the end of the string) in the dictionary.

    We also need to check if the last substring we inserted into the queue marks the end of the string. If so, there is nothing more to do and return True.

    If we're not at the end if the string, keep checking if you can find another substring from start to end of string.

    Mark the index you just popped from the queue as visited:

        visited[start] = 1

    3. Once this is done, move to the next iteration, pop top of the queue and repeat.

    4. Once the queue is empty, it means we have no more indexes of subtrings to start checking in the string. retrun False

OPTIMIZATION: We can check the substrings upto the maximum length of the words in the the dictionary. In that case we need to add:

    if not string or not wordDict: return False
    max_len = len(max(word_dict, key=len))

i.e check for a base case and find the maximum length of the words in the dictionary.

Then we do:
    for i in range(start, start + max_len + 1):

in the for loop.

Note we add 1 to the loop termination condition because we're dealing with substrings. Example, even though 'leetcode' has length of 8, we have to do 'leetcode'[0...9] if we want to get a substring of the whole string in the inner if condition. Where the 9th index is non-inclusive.
=end

def word_break(s, word_dict)
  queue, visited = [], [0] * s.length
  queue << 0

  until queue.empty?
    start = queue.pop

    if visited[start].zero?
      (start + 1 ... s.length + 1).each do |i|
        if word_dict.include?(s[start...i])
          queue.unshift(i)

          return true if i == s.length
        end
      end

      visited[start] = 1
    end
  end

  false
end

if __FILE__ == $0
  puts word_break('leetcode', ['leet', 'code'])
end
