class PriorityQueue:
    def __init__(self):
        self.heap_array = [(0, 0)]
        self.current_size = 0

    def build_heap(self, a_list):
        self.current_size = len(a_list)
        self.heap_array = [(0, 0)]
        for i in a_list:
            self.heap_array.append(i)
        i = len(a_list) // 2
        while (i > 0):
            self.perc_down(i)
            i -= 1

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_array[index][0] > self.heap_array[mc][0]:
                temp = self.heap_array[index]
                self.heap_array[index] = self.heap_array[mc]
                self.heap_array[mc] = temp
            index = mc

    def min_child(self, index):
        if index * 2 > self.current_size:
            return -1
        else:
            if index * 2 + 1 > self.current_size:
                return index * 2
            else:
                if self.heap_array[index * 2][0] < self.heap_array[index * 2 + 1][0]:
                    return index * 2
                else:
                    return index * 2 + 1

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_array[index][0] < self.heap_array[index // 2][0]:
                temp = self.heap_array[index // 2]
                self.heap_array[index // 2] = self.heap_array[index]
                self.heap_array[index] = temp
            index = index // 2

    def add(self, key):
        self.heap_array.append(key)
        self.current_size += 1
        self.perc_up(self.current_size)

    def del_min(self):
        ret_val = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size -= 1
        self.heap_array.pop()
        self.perc_down(1)
        return ret_val

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self, val, amt):
        done = False
        i = 1
        my_key = 0
        while not done and i <= self.current_size:
            if self.heap_array[i][1] == val:
                done = True
                my_key = i
            else:
                i = i + 1
        if my_key > 0:
            self.heap_array[my_key] = (amt, self.heap_array[my_key][1])
            self.perc_up(my_key)

    def __contains__(self, vtx):
        for pair in self.heap_array:
            if pair[1] == vtx:
                return True
        return False
