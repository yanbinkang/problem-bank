def find_duplicate(paths)
  d = Hash.new { |h, k| h[k] = [] }

  paths.each do |line|
    data = line.split
    root = data.first

    data[1..-1].each do |file|
      name, _, content = file.partition('(')
      d[content[0..-2]] << root + '/' + name
    end
  end

  results = []

  d.each do |k, v|
    results << v if v.length > 1
  end

  results
end

if __FILE__ == $0
  paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

  paths_1 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

  paths_2 = ["root/a 1.txt(abcd) 2.txt(efsfgh) 3.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]


  puts find_duplicate(paths).inspect
  puts find_duplicate(paths_1).inspect
  puts find_duplicate(paths_2).inspect
end
