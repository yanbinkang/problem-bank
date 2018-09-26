=begin
https://leetcode.com/problems/remove-invalid-parentheses/#/description

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

https://discuss.leetcode.com/topic/28827/share-my-java-bfs-solution

The idea is straightforward, with the input string s, we generate all possible states by removing one ( or ), check if they are valid, if found valid ones on the current level, put them to the final result list and we are done, otherwise, add them to a queue and carry on to the next level.

The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal, also no recursion call is needed in BFS.

My explanation:
For each input string s, we first check if it valid. If so add to result array, set found to true and we are done.

If its not valid, we generate all possible states of s by removing one ( or ) add to the front of the queue and move on to the next level (which is to process the validity or not of the items on the queue, depending upon which we generate all possible states of that s popped off the queue). We continue until we done with all possible states of the input s.

We use the set to make sure we're not processing a possible state more than once.

Question: Doesn't "found" variable have to be reset to "false"?

Answer: Once an answer is found, there will never be any answer shorter than it. So there is no need to iterate down (by generating all possible states), until now there are all possible candidates in queue.
=end
require 'set'
def remove_invalid_parentheses(s)
  result = []

  return result if s.empty?

  visited = Set.new
  queue = []

  # initalize
  queue << s
  visited << s
  found = false

  until queue.empty?
    s = queue.pop

    if is_valid?(s)
      result << s
      found = true
    end

    next if found

    # generate all possible states
    s.length.times do |i|
      # we only try to remove left or right paren
      next if s[i] != '(' && s[i] != ')'

      candidate = s[0 ... i] + s[i + 1 ... s.length]

      unless visited.include?(candidate)
        # for each state, if its not in visited, add to queue
        queue.unshift(candidate)
        visited << candidate
      end
    end
  end

  return result
end

def is_valid?(s)
  count = 0

  s.length.times do |i|
    char = s[i]

    count += 1 if char == '('

    if char == ')'
      return false if count == 0

      count -= 1
    end
  end

  count == 0
end

if __FILE__ ==  $0
  puts remove_invalid_parentheses('()())()')
end
