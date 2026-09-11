class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = sorted(start for start, end in intervals)
        end_time = sorted(end for start, end in intervals)
        
        end_idx = 0
        room = 0
    
        for start in start_time:
            if start < end_time[end_idx]:
                room += 1
            else:
                end_idx += 1
        
        return room
