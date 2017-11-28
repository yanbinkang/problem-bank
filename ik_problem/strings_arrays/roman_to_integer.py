def roman_to_integer(a_str):
    my_dict = {}
    my_dict["I"] = 1
    my_dict["V"] = 5
    my_dict["X"] = 10
    my_dict["L"] = 50
    my_dict["C"] = 100
    my_dict["D"] = 500
    my_dict["M"] = 1000

    a_str_length = len(a_str)

    # get value of last char in string
    total = my_dict[a_str[a_str_length - 1]]

    i = a_str_length - 2
    while i >= 0:
        if my_dict[a_str[i]] < my_dict[a_str[i+1]]:
            total -= my_dict[a_str[i]]
        else:
            total += my_dict[a_str[i]]

        i -= 1

    return total


print roman_to_integer("IV")                # 4
print roman_to_integer("VII")               # 7
print roman_to_integer("CLXXXIV")           # 184
print roman_to_integer("MMMMMMMMMCMXIX")    # 9919
