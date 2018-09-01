def least_bricks(wall)
  if wall.length == 0
    return 0
  end

  count, dic = 0, {}

  wall.each do |row|
    len = 0
    (row.length - 1).times do |i|
      len += row[i]
      dic[len] = dic.fetch(len, 0) + 1
      count = [count, dic[len]].max
    end
  end

  wall.length - count
end

wall = [[1,2,2,1],
         [3,1,2],
         [1,3,2],
         [2,4],
         [3,1,2],
         [1,3,1,1]]

puts least_bricks(wall)
