class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([meeting[0] for meeting in intervals])
        ends = sorted([meeting[1] for meeting in intervals])
        end_point = 0
        rooms_need = 0

        for start in starts:
            if start < ends[end_point]:
                rooms_need += 1
            else:
                end_point += 1
        
        return rooms_need
        