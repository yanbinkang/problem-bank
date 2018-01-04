def alternate(a_list):
    for i in range(len(a_list)):
        j = 0
        while j + 2 < len(a_list):
            s = [a_list[j], a_list[j+1], a_list[j+2]]
            s = [1 if x >= 0 else -1 for x in s]

            if s[0] == s[1] and s[1] != s[2]:
                temp = a_list[j+1]
                a_list[j+1] = a_list[j+2]
                a_list[j+2] = temp
                # a_list[j+1], a_list[j+2] = a_list[j+2], a_list[j+1]
            j += 1
    return a_list

array = [2, 3, -4, -9, -1, -7, 1, -5, -6]
print alternate(array)
