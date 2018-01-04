# solution: http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/
def box_stacking(boxes):
    # box dimentions are in h w d
    # h -> height, w -> width, d -> depth
    m = len(boxes)

    # generate rotations
    rot = [[None for i in range(3)] for j in range(m)*3]
    idx = 0
    for i in range(m):

        # cpoy the original box
        rot[idx] = boxes[i]

        idx += 1

        rot[idx][0] = boxes[i][1]
        rot[idx][1] = min(boxes[i][0], boxes[i][2])
        rot[idx][2] = max(boxes[i][0], boxes[i][2])

        idx += 1

        rot[idx][0] = boxes[i][2]
        rot[idx][1] = min(boxes[i][0], boxes[i][1])
        rot[idx][2] = max(boxes[i][0], boxes[i][1])

        idx += 1

    # sort rotations in decreasing order of base arad (w & d)
    sorted_rot = sorted(rot, key=lambda x:x[1] * x[2], reverse=True)

    # create array to store max height and store heights as initial values
    max_height = [0 for i in range(len(sorted_rot))]
    for i in range(len(sorted_rot)):
        max_height[i] = sorted_rot[i][0]

    # # create array to store final result and store indices as initial values
    result = [0 for i in range(len(sorted_rot))]
    for i in range(len(sorted_rot)):
        result[i] = i


    i = 0
    while i < len(sorted_rot):
        j = 0
        while j < i:
            if sorted_rot[i][1] < sorted_rot[j][1] and sorted_rot[i][2] < sorted_rot[j][2]:
                max_height[i] = max(max_height[i], max_height[j] + sorted_rot[i][0])
                result[i] = j
            j += 1
        i += 1

    # print actual boxes
    print "\n"
    print "Printing actual boxes..."
    new_t = max_height.index(max(max_height))
    while True:
        t = new_t
        print str(sorted_rot[t]) + " "
        new_t = result[t]

        if t == new_t:
            break

    return "Maximum height is %s" % max(max_height)

print box_stacking([[1, 2, 4], [3, 2, 5]])
print box_stacking([[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]])
