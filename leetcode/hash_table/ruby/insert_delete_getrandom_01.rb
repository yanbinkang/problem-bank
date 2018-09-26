=begin
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.

2. remove(val): Removes an item val from the set if present.

3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

read this: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
=end
require 'set'
class RandomizedSet
  def initialize
    @store = Set.new
  end

  def insert(val)
    if @store.include?(val)
      false
    else
      @store.add(val)
      true
    end
  end

  def remove(val)
    if @store.include?(val)
      @store.delete(val)
      true
    else
      false
    end
  end

  def get_random
    @store.to_a.sample
  end
end
