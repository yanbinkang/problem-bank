def toStr(n, base):
    convert_str = "0123456789ABCDEF"
    if n < base:
        return convert_str[n]
    else:
        return toStr(n // base, base) + convert_str[n % base]
