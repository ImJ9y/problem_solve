class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start_time = sorted(start for start, end in intervals)
        end_time = sorted(end for start, end in intervals)

        idx = 0
        room = 0

        for start in start_time:
            if start < end_time[idx]:
                room += 1
            else:
                idx += 1
        
        return room