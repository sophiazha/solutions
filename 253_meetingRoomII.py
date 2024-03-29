import heapq
from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRoomsL(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append([start, 1])
            time.append([end, -1])
        time.sort()
        count = 0
        res = 0
        for timing, n in time:
            count += n
            res = max(res, count)
        return res

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
       # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        #intervals.sort(key=lambda x: x[0])   No need lambda as this is default column anyway
        intervals.sort()

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms

    def minMeetingRoomsL(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        res, rooms = 0, 0
        for a, z in intervals:
            heappush(minHeap, [a, 1])
            heappush(minHeap, [z, -1])
        while minHeap:
            t, s = heappop(minHeap)
            rooms += s
            res = max( rooms, res)
        return res

sol = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
print(sol.minMeetingRooms(intervals))


"""
    253. Meeting Rooms II
Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

 

Constraints:

    1 <= intervals.length <= 104
    0 <= starti < endi <= 106

Accepted
716,555
Submissions
1,422,739
"""