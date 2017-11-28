def optimal_job_selection(sample_jobs):
    sorted_intervals = sorted(sample_jobs, key=lambda x:x[1])
    initial_job_start, initial_job_end = sorted_intervals[0]
    selected_jobs = [(initial_job_start, initial_job_end)]

    for current_job_start, current_job_end in sorted_intervals[1:]:
        if current_job_start > initial_job_end:
            selected_jobs.append((current_job_start, current_job_end))

    return selected_jobs

intervals = [(11, 14), (3, 12), (1, 4), (7, 10), (4, 10)]
print optimal_job_selection(intervals)
