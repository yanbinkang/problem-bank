class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    def del_min(self):
        res = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.perc_down(1)
        return res

    def perc_down(self, index):
        while index * 2 <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc

    def min_child(self, index):
        if (index * 2 + 1) > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, a_list):
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self.perc_down(i)
            i -= 1


a_list = [[1, 3, 5, 7],[2, 4, 6, 8], [0, 9, 10, 11]]
s = [6, 5, 3, 1, 8, 7, 2, 4]
res = []
sorted_array = []
for arr in a_list:
    res += arr
bh = BinaryHeap()
bh.build_heap(res)

while bh.current_size > 0:
    sorted_array.append(bh.del_min())

print sorted_array

