# assuming a_list is sorted by start time
def merge_overlapping_intervals(a_list):
    previous_meeting_start, previous_meeting_end = a_list[0]
    merged_meetings = []

    for current_meeting_start, current_meeting_end in a_list[1:]:
        if current_meeting_start <= previous_meeting_end:
            previous_meeting_end = max(current_meeting_end, previous_meeting_end)
        else:
            merged_meetings.append((previous_meeting_start, previous_meeting_end))
            previous_meeting_start, previous_meeting_end = current_meeting_start, current_meeting_end

    merged_meetings.append((previous_meeting_start, previous_meeting_end))

    return merged_meetings

print merge_overlapping_intervals([(1, 5), (3, 7), (4, 6), (6, 8), (10, 12), (11, 15)])
