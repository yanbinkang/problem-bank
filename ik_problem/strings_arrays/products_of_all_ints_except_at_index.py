"""Brute force
def product_at_index(a_list):
    i = 0
    res = []
    while i < len(a_list):
        j = 0
        product = 1
        while j < len(a_list):
            if i != j:
                product *= a_list[j]
            j += 1
        res.append(product)
        i += 1

    return res


print product_at_index([1, 7, 3, 4])
"""

def products_of_all_ints_except_at_index(int_array):

    # we make an array with the length of the input array to
    # hold our products
    products_of_all_ints_except_at_index = [1] * len(int_array)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product = 1
    i = 0
    while i < len(int_array):
        products_of_all_ints_except_at_index[i] = product
        product *= int_array[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product = 1
    i = len(int_array) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product
        product *= int_array[i]
        i -= 1

    return products_of_all_ints_except_at_index

print products_of_all_ints_except_at_index([1, 7, 3, 4])
print products_of_all_ints_except_at_index([1, 2, 3, 4, 5])
