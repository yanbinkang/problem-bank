=begin
wiki: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Video link - https://youtu.be/ID00PMy0-vE

Disjoint sets using path compression and union by rank
    Supports 3 operations
    1) makeSet
    2) union
    3) findSet

Space: O(n) where n is number of elements in the set

Time: For m operations and total n elements time complexity is O(m*f(n)) where f(n) is very slowly growing function. For most cases f(n) <= 4 so effectively total time will be O(m). Proof in Coreman book.
=end
class Node
  attr_accessor :data, :parent, :rank

  def initialize(data, parent = nil, rank = 0)
    @data = data
    @parent = parent
    @rank = rank
  end

  def to_s
    @data.to_s
  end
end

class DisjointSet
  def initialize
    @map = {}
    @num_sets = 0
  end

  def make_set(data)
    node = Node.new(data)
    node.parent = node
    @map[data] = node
    @num_sets += 1
  end

  def union(data1, data2)
    # gets nodes given data values
    node1 = @map[data1]
    node2 = @map[data2]

    # get parents given nodes
    parent1 = find_set_util(node1)
    parent2 = find_set_util(node2)

    return if parent1.data == parent2.data

    # else whoever's rank is higher becomes parent of other
    if parent1.rank >= parent2.rank
      if parent1.rank == parent2.rank
        parent1.rank = parent1.rank + 1
      end

      parent2.parent = parent1
    else
      parent1.parent = parent2
    end

    @num_sets -= 1
  end

  def find_set(data)
    find_set_util(@map[data]) # pass in the node
  end

  # Find the representative recursively and does path compression
  def find_set_util(node)
    parent = node.parent

    return parent if parent == node

    node.parent = find_set_util(node.parent) # path compression

    return node.parent
  end
end

if __FILE__ == $0
  ds = DisjointSet.new
  ds.make_set(1)
  ds.make_set(2)
  ds.make_set(3)
  ds.make_set(4)
  ds.make_set(5)
  ds.make_set(6)
  ds.make_set(7)

  ds.union(1,2)
  ds.union(2,3)
  ds.union(4,5)
  ds.union(6,7)
  ds.union(5,6)
  ds.union(3,7)

  (1...8).each do |i|
    puts ds.find_set(i)
  end
end
