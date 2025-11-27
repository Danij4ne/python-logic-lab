
"""
CH03 - Merge Intervals

Description:
    Given a list of intervals, merge all intervals that overlap
    and return a list of non-overlapping intervals.

Requirements:
    - Create a list of intervals (e.g., [(1, 3), (2, 6), (8, 10), (9, 12)]).
    - Sort the intervals by start time.
    - Merge overlapping intervals:
        - If the current interval overlaps with the previous one,
          combine them into a single interval.
        - Otherwise, add the current interval as a new entry.
    - Print the final merged list.

Notes:
    - Overlap occurs when the current start is <= previous end.
    - This is a common interview problem related to scheduling,
      time ranges, and data compression.

Example:
    Input:
    [(1, 3), (2, 6), (8, 10), (9, 12)]

    Output:
    [(1, 6), (8, 12)]
"""

# TODO:
# 1. Create a list of intervals.
# 2. Sort intervals by start time.
# 3. Merge overlapping intervals.
# 4. Print the merged result.
