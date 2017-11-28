def find_range_overlap(point_1, length_1, point_2, length_2):
    highest_start_point = max(point_1, point_2)
    lowest_end_point = min(point_1 + length_1, point_2 + length_2)

    if highest_start_point >= lowest_end_point:
        return (None, None)

    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)


def find_rectangular_overlap(rect_1, rect_2):
    x_overlap_point, overlap_width = find_range_overlap(\
        rect_1['x'], rect_1['width'], rect_2['x'], rect_2['width'])
    y_overlap_point, overlap_height = find_range_overlap(\
        rect_1['y'], rect_1['height'], rect_2['y'], rect_2['height'])

    if not overlap_width or not overlap_height:
        return None

    return {
        'x': x_overlap_point,
        'y': y_overlap_point,
        'width': overlap_width,
        'height': overlap_height
    }
