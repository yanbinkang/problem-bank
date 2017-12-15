require 'set'

class PhoneDirectory
  attr_reader :available

  def initialize(max_numbers)
    @available = Set.new (0...3).to_a
  end

  def get
    if available
      item = available.to_a.pop
      available.delete(item)

      item
    else
      -1
    end

  end

  def check(number)
    available.include?(number)
  end

  def release(number)
    available.add(number)
  end
end

s = PhoneDirectory.new(3)


p s.get
p s.get

s.release(2)
p s.check(2)
