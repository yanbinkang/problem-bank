def print_count_of_bitset(int_arr):
    res = ""
    for num in int_arr:
        res += bin(num)
    return res.count("1")

if __name__ == '__main__':
    inp1 = [31, 51]
    inp2 = [2147483647, 3]

    print print_count_of_bitset(inp1)
    print print_count_of_bitset(inp2)
