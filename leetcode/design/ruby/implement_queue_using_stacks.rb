=begin
https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement the following operations of a queue using stacks.

  * push(x) -- Push element x to the back of queue.
  * pop() -- Removes the element from in front of queue.
  * peek() -- Get the front element.
  * empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

  * You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.

  * Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.

  * You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
=end
class MyQueue

=begin
    Initialize your data structure here.
=end
  def initialize
    @in, @out = [], []
  end


=begin
    Push element x to the back of queue.
    :type x: Integer
    :rtype: Void
=end
  def push(x)
    @in << x
  end


=begin
    Removes the element from in front of queue and returns that element.
    :rtype: Integer
=end
  def pop
    peek

    @out.pop
  end


=begin
    Get the front element.
    :rtype: Integer
=end
  def peek
    if @out.empty?
      @out << @in.pop until @in.empty?
    end

    @out.last
  end


=begin
    Returns whether the queue is empty.
    :rtype: Boolean
=end
  def empty
    @in.empty? && @out.empty?
  end
end

queue = MyQueue.new

queue.push(1)
queue.push(2)
queue.peek  # returns 1
queue.pop   # returns 1
queue.empty # returns false
