class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        self.limit = 4

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
        if self.current_size > self.limit:
            self.del_min()

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        elif self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
            return index * 2
        else:
            return index * 2 + 1

bh = BinHeap()
bh.insert(9)
bh.insert(6)
bh.insert(5)
bh.insert(2)
bh.insert(3)
print bh.heap_list
