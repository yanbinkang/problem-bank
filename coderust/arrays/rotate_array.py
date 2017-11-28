def rotate_array(a_list, num):
    rev_array(a_list, 0, len(a_list)-1)
    rev_array(a_list, 0, num-1)
    rev_array(a_list, num, len(a_list)-1)
    return a_list



def rev_array(a_list, first, last):
    while first <= last:
        temp = a_list[first]
        a_list[first] = a_list[last]
        a_list[last] = temp
        first += 1
        last -= 1

print rotate_array([1, 10, 20, 0, 59], -1)
print rotate_array([1,2,3,4,5,6,7], 3)
