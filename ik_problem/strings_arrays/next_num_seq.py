# also known as look and say

def look_and_say(num, input):

    output = []
    result = [input]

    while num > 0:
        count = 1
        i = 1

        while i <= len(input):
            if i < len(input) and input[i] == input[i-1]:
                count += 1
            else:
                output.append(str(count) + input[i-1])
                count = 1
            i += 1

        input = "".join(output)
        result.append(input)
        output = []
        num -= 1
    return result[-2]


# print look_and_say(4, "1")
# print look_and_say(2, "2")
print look_and_say(3, "22")
