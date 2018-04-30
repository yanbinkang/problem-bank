class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def append(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[index // 2]
                self.heap_list[index // 2] = temp
            index = index // 2

    def del_max(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            mc = self.max_child(index)
            if self.heap_list[index] < self.heap_list[mc]:
                temp = self.heap_list[mc]
                self.heap_list[mc] = self.heap_list[index]
                self.heap_list[index] = temp
            index = mc

    def max_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        elif self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
            return index * 2
        else:
            return index * 2 + 1

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.heap_list = [0] + a_list[:]
        self.current_size = len(a_list)

        while i > 0:
            self.perc_down(i)
            i -= 1

bh = BinaryHeap()
bh.build_heap([6, 5, 3, 1, 8, 7, 2, 4])
print bh.heap_list
