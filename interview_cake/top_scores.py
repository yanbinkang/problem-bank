def sort_score(unordered_scores, highest_possible_score):
    scores_to_counts = [0] * (highest_possible_score+1)

    for score in unordered_scores:
        scores_to_counts[score] += 1
    print scores_to_counts

    sorted_scores = []

    # i = 0
    # while i < len(scores_to_counts):
    #     j = 0
    #     while j < scores_to_counts[i]:
    #         sorted_scores.append(i)
    #         j += 1
    #     i += 1

    for score, count in enumerate(scores_to_counts):
        for time in range(count):
            sorted_scores.append(score)

    return sorted_scores

a_list = [5, 17, -1, 9, 5, 0, 30]
print sort_score(a_list, 30)
