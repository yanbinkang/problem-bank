class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, index):
        # while the left index below root is lte current_size of heap_list
        while (index * 2) <= self.current_size:
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

    def del_min(self):
        ret_val = self.heap_list[1] # set min to ret_val
        self.heap_list[1] = self.heap_list[self.current_size] # set first element in heap_list to last element in heap_list
        self.current_size = self.current_size - 1 # reduce size of current_size
        self.heap_list.pop() # remove last item from heap_list
        self.perc_down(1) # maintain heap order property
        return ret_val # return min

    def is_empty(self):
        return True if self.current_size == 0 else False

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
        # print(self.heap_list, i)

"""
bh = BinaryHeap()
bh.build_heap([9, 6, 5, 2, 3])
# print bh.heap_list
while bh.current_size > 0:
    print bh.del_min()
# print bh.heap_list
"""
