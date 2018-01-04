from sys import maxint
def second_largest(a_list):
    second_largest = -maxint
    largest = a_list[0]

    for i in range(1, len(a_list)):
        if a_list[i] > largest:
            second_largest = largest
            largest = a_list[i]
        elif a_list[i] > second_largest:
            second_largest = a_list[i]

    return second_largest

a = [12, 13, 1, 10, 34, 1]
b = [1, 2, 3, 4, 5]
c = [5, 4, 2, 3, 1]
d = [1000, 2, 798, 5, 5, 6, 700, 8, 9, 10, 11, 103, 15]

print second_largest(a)
print second_largest(b)
print second_largest(c)
print second_largest(d)
