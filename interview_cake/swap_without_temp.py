def swap_without_temp(a, b):
    print("before swapping a:%r b:%r" % (a, b))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("after swapping a:%r b:%r" % (a, b))

swap_without_temp(10, 6)
