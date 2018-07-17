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
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

solution:

ref: https://leetcode.com/problems/implement-queue-using-stacks/discuss/64206/Short-O(1)-amortized-C++-Java-Ruby

I have one input stack, onto which I push the incoming elements, and one output stack, from which I peek/pop. I move elements from input stack to output stack when needed, i.e., when I need to peek/pop but the output stack is empty. When that happens, I move all elements from input to output stack, thereby reversing the order so it's the correct order for peek/pop.

The loop in peek does the moving from input to output stack. Each element only ever gets moved like that once, though, and only after we already spent time pushing it, so the overall amortized cost for each operation is O(1).
=end
class MyQueue

=begin
    Initialize your data structure here.
=end
    def initialize()
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
    def pop()
      peek
      @out.pop
    end


=begin
    Get the front element.
    :rtype: Integer
=end
    def peek()
      @out << @in.pop until @in.empty? if @out.empty?
      @out.last
    end


=begin
    Returns whether the queue is empty.
    :rtype: Boolean
=end
    def empty()
      @in.empty? && @out.empty?
    end


end

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue.new()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
