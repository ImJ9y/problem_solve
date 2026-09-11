class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = sorted(start for start, end in intervals)
        end_time = sorted(end for start, end in intervals)
        start_idx = len(end_time)-1
        # 0 5 15
        # 10 20 30

        room = 0
        for R in range(len(end_time)-1,-1,-1):
            if end_time[R] > start_time[start_idx]:
                room += 1
                R -= 1
            else:
                start_idx -= 1
        return room
            
