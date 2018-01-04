def nuts_and_bolts_match(nuts_list, bolts_list, first, last):
    if first < last:
        pivot = partition(nuts_list, first, last, bolts_list[last])

        partition(bolts_list, first, last, nuts_list[pivot])

        nuts_and_bolts_match(nuts_list, bolts_list, first, pivot-1)
        nuts_and_bolts_match(nuts_list, bolts_list, pivot+1, last)

def partition(a_list, first, last, pivot_value):
    i = first
    j = first
    while j < last:
        if a_list[j] < pivot_value:
            temp = a_list[i]
            a_list[i] = a_list[j]
            a_list[j] = temp
            i += 1
        elif a_list[j] == pivot_value:
            temp = a_list[j]
            a_list[j] = a_list[last]
            a_list[last] = temp
            j -= 1
        j += 1
    temp = a_list[i]
    a_list[i] = a_list[j]
    a_list[last] = temp

    return i

def print_array(a_list):
    for ch in a_list:
        print ch,
    print "\n"

if __name__ == '__main__':
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']
    # nuts = ['n3', 'n2', 'n1', 'n4']
    # bolts = ['b4', 'b2', 'b3', 'b1']

    nuts_and_bolts_match(nuts, bolts, 0, 5)

    print "Matched nuts and bolts are: "
    print "\n"
    print_array(nuts)
    print_array(bolts)
