"""
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
def restore_ip_addresses(s):
    if not s:
        return ['']

    result = []

    helper(s, 0, 0, result, [])

    return result

def helper(s, start, count, result, temp_list):
    if start == len(s) and count == 4:
        temp = str(temp_list[0])
        for i in range(1, len(temp_list)):
            temp += '.'
            temp += temp_list[i]

        result.append(temp)
    elif start == len(s) or count == 4:
        return
    else:
        for i in range(start, len(s)):
            if i != start and s[start] == '0':
                break
            ip = s[start:i + 1]
            if int(ip) > 255:
                continue
            temp_list.append(ip)
            helper(s, i + 1, count + 1, result, temp_list)
            temp_list.pop()


import re
def restore_ip_addresses_alt(s):
    result = []

    _helper(s, result, [])

    return result

def _helper(s, result, temp_list):
    if len(temp_list) == 4:
        if s:
            return
        else:
            result.append('.'.join(temp_list))
            return

    for i in range(1, 4):
        if i > len(s) or re.findall('^0\d+', s[:i]) or int(s[:i]) > 255:
            return

        temp_list.append(s[:i])
        _helper(s[i:], result, temp_list)
        temp_list.pop()


if __name__ == '__main__':
    print restore_ip_addresses('25525511135')
    print restore_ip_addresses('0000')
    print restore_ip_addresses('127000')
    print restore_ip_addresses('1111')
    print restore_ip_addresses('10001')

    print('\n')
    print restore_ip_addresses_alt('25525511135')



