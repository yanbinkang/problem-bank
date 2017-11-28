from sys import maxint
def max_product_subarray(a_list):
    max_prod = -maxint
    prod = 1

    for num in a_list:
        prod = prod * num
        max_prod = max(max_prod, prod)

        if num == 0:
            prod = 1

    prod = 1

    # below loop is the same as using a while loop
    # and starting from len(a_list)-1 and ending at i >= 0
    for i in reversed(range(len(a_list))):
        prod = prod * a_list[i]
        max_prod = max(max_prod, prod)

        if a_list[i] == 0:
            prod = 1

    return max_prod


arr_1 = [6, -3, -10, 2]
arr_2 = [-1, -3, -10, 60]
arr_3 = [-2, -3, -2, -40]
arr_4 = [5, 1, 2, -3, 7, -4]
arr_5 = [1, 1, 1, 1, 1, 1, 20, -1, 1]
arr_6 = [2, 3, -2, 4]

# print max_product_subarray(arr_1)
# print max_product_subarray(arr_2)
# print max_product_subarray(arr_3)
# print max_product_subarray(arr_4)
# print max_product_subarray(arr_5)
print max_product_subarray(arr_6)
