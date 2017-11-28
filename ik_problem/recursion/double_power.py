def pow(base, power):
    if power < 0:
        if power == -1:
            return 1.0 / base
        res = base * pow(base, abs(power)-1)
        return 1.0 / res

    if power >= 0:
        if power == 0:
            return 1
        if power == 1:
            return base

        return base * pow(base, power-1)


# print pow(2, -1)
# print pow(2, -2)
# print pow(2, 0)
# print pow(2, 1)
# print pow(2, 2)
# print pow(2, 10)
# print pow(3, -1)
# print pow(3, -2)
# print pow(4, -5)
print pow(5, 5)
print pow(2, 3)
