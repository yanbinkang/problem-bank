=begin
https://leetcode.com/problems/simplify-path/description/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

algorithm:
ref: https://discuss.leetcode.com/topic/28240/9-lines-of-python-code/6

1. Use a stack

2. split the given path by '/' and iterate through the tokens

3. If token is '..', meaning we have to go to the parent directory, check if the stack is not empty. If this is true pop the last item from the stack

4. If the token is not an empty string and token is not equal to '.' - meaning we're staying in the same directory - append the token to the stack.

5. Finally return '/' concatenated with '/' joined with the items in the stack.

        return '/' + '/'.join(stack)
=end
def simplify_path(path)
  stack = []

  path = path.split('/')

  path.each do |p|
    if p == '..'
      stack.pop unless stack.empty?
    elsif !p.empty? && p != '.'
      stack << p
    end
  end

  '/' + stack.join('/')
end

if $PROGRAM_NAME == __FILE__
  p simplify('/a/./b/../../c/')
  p simplify_path('/home/')
end
