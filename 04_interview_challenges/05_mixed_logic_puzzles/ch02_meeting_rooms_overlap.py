

"""
CH02 - Meeting Rooms Overlap

Description:
    Given a list of meeting time intervals, determine whether any
    two meetings overlap. Each interval has a start time and an end time.

Requirements:
    - Create a list of meeting intervals (e.g., [(1, 3), (2, 4), (5, 7)]).
    - Check whether any two intervals overlap.
    - Print True if there is an overlap, otherwise False.

Notes:
    - A simple approach is to:
        - sort the intervals by start time
        - compare each meeting's start with the previous meeting's end
    - This problem is common in scheduling and calendar systems.

Example:
    Input:
    [(1, 3), (2, 4), (5, 7)]

    Output:
    True   (because (1, 3) overlaps with (2, 4))
"""

# TODO:
# 1. Create a list of meeting intervals.
# 2. Sort intervals by start time.
# 3. Check if any interval overlaps with the previous one.
# 4. Print True if overlap exists, otherwise False.
