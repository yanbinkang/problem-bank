class HashTable
  attr_reader :size
  attr_accessor :slots, :data

  def initialize
    @size = 11
    @slots = [nil] * @size
    @data = [nil] * @size
  end

  def put(key, data)
    hash_value = hash_function(key, slots.length)

    if slots[hash_value].nil?
      self.slots[hash_value] = key
      self.data[hash_value] = data
    else
      if slots[hash_value] == key
        self.data[hash_value] = data
      else
        next_slot = rehash(hash_value, slots.length)

        while slots[next_slot] != nil && slots[next_slot] != key
          next_slot = rehash(next_slot, slots.length)
        end

        if slots[next_slot].nil?
          self.slots[next_slot] = key
          self.data[next_slot] = data
        else
          self.data[next_slot] = data
        end
      end
    end
  end

  def hash_function(key, size)
    key % size
  end

  def rehash(old_hash, size)
    (old_hash + 1) % size
  end

  def string_hash_function(str, size)
    str_sum = 0
    i = 0
    while i < str.length
      str_sum += (str[i].ord * (i + 1))
      i += 1
    end

    return str_sum % size
  end

  def get(key)
    start_slot = hash_function(key, slots.length)

    data = nil
    stop = false
    found = false
    position = start_slot

    while slots[position] != nil && !found && !stop
      if slots[position] == key
        found = true
        data = self.data[position]
      else
        position = rehash(position, slots.length)


        if position == start_slot
          stop = true
        end
      end
    end

    return data
  end

  def []=(key, data)
    put(key, data)
  end

  def [](key)
    get(key)
  end

  def delete(key)
    start_slot = hash_function(key, slots.length)
    position = start_slot
    stop = false
    found = false

    while slots[position] != nil && !stop && !found
      if slots[position] == key
        found = true
        self.slots[position] = nil
        self.data[position] = nil
      else
        position = rehash(position, slots.length)

        if position == start_slot
          stop = true
        end
      end
    end
  end
end

h = HashTable.new

h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"

p h.slots
p h.data
p h[44]
h.delete(44)
p h.slots
p h.data
