from binary_heap_min_heap import BinaryHeap

def heap_sort(a_list):
    sorted_array = []
    min_heap = BinaryHeap()
    min_heap.build_heap(a_list)

    while min_heap.current_size > 0:
        sorted_array.append(min_heap.del_min())

    return sorted_array


print heap_sort([1, 3, 5, 7, 2, 4, 6, 8, 0, 9, 10, 11])
