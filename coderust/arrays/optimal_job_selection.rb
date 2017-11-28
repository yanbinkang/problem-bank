def optimal_job_selection(some_jobs)
  sorted_jobs = some_jobs.sort_by {|jobs| jobs[1]}

  current_job = sorted_jobs.first
  selected_jobs = [current_job]
  i = 1

  while i < sorted_jobs.length
    if sorted_jobs[i][0] > current_job[1]
      selected_jobs.push(sorted_jobs[i])
    end

    i += 1
  end

  selected_jobs
end

intervals = [[11, 14], [3, 12], [1, 4], [7, 10], [4, 10]]

p optimal_job_selection(intervals)
