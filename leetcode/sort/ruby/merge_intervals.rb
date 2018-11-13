=begin
https://leetcode.com/problems/merge-intervals/#/description

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
=end
# Definition for an interval.
class Interval
  attr_accessor :start, :end

  def initialize(s=0, e=0)
    @start = s
    @end = e
  end

  def to_s
    "#{@start} #{@end}"
  end
end

def merge(intervals)
  return intervals if intervals.length <= 1

  intervals = intervals.sort_by(&:start)

  result = []

  intervals.each do |interval|
    if !result.empty? && result.last.end >= interval.start
      result.last.end = [result.last.end, interval.end].max
    else
      result << interval
    end
  end

  result
end

if $PROGRAM_NAME == __FILE__
  intervals1 = [Interval.new(1, 3), Interval.new(2, 6),\
                Interval.new(8, 10), Interval.new(15, 18)]

  intervals2 = [Interval.new(1, 2), Interval.new(3, 5),\
                Interval.new(6, 7), Interval.new(8, 10), \
                Interval.new(12, 16)]

  puts merge(intervals1)
  puts
  puts merge(intervals2)
end
