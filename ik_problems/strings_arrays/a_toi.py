# Implement atoi to convert a string to an integer.

class Solution:
    def atoi(self, string):
        if string == None or string == '':
            return 0
        rs = string.strip()
        temp_i = 0

        for i in range(len(rs)):
            temp_i = i

            if i == 0 and rs[i] == '+':
                continue
            if i == 0 and rs[i] == '-':
                continue
            if i == 1 and (rs[0] == '+' or rs[0] == '-') and (rs[i] > '9' or rs[i] < '0'):
                return 0
            if rs[i] > '9' or rs[i] < '0':
                temp_i = i - 1
                break

        rs = rs[:(temp_i+1)]
        if rs == '':
            return 0
        if int(rs) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif int(rs) < (-2 ** 31):
            return -2 ** 31
        else:
            return int(rs)

s = Solution()
print s.atoi("-1b23")
