def frequency_sort(s)
  result = ''

  bucket = [nil] * (s.length + 1)

  hash_map = {}

  s.chars.each do |char|
    hash_map[char] = hash_map.fetch(char, 0) + 1
  end

  hash_map.each do |key, value|
    bucket[value] = [] if bucket[value].nil?

    bucket[value] << key
  end

  (0..bucket.length - 1).reverse_each do |i|
    if bucket[i]
      bucket[i].each do |char|
        result += char * i
      end
    end
  end

  result
end

if __FILE__ == $0
  puts frequency_sort('Aabb')
  puts frequency_sort('tree')
  puts frequency_sort('cccaaa')
end
