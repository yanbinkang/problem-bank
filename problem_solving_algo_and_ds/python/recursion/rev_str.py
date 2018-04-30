def revStr(my_string):
    if len(my_string) <= 1:
        return my_string
    else:
        return my_string[-1] + revStr(my_string[:-1])


print(revStr("albert"))
