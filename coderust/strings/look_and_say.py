def look_and_say(input, num):
    output = []

    while num > 0:
        i = 1
        count = 1
        while i <= len(input):
            if i < len(input) and input[i] == input[i - 1]:
                count += 1
            else:
                output.append(str(count) + str(input[i - 1]))
                count = 1
            i += 1

        input = ''.join(output)
        print input

        output = []
        num -= 1

print look_and_say("1", 5)
