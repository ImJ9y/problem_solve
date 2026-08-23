class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        res = []

        new_intervals = sorted(list(intervals))
        print(new_intervals)

        for interval in new_intervals:
            if res and res[-1][1] > interval[0]:
                return False
            else:
                res.append(interval)
            
        return True