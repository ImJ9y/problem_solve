class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        full_interval = [newInterval]

        for interval in intervals:
            full_interval.append(interval)
        

        full_interval = (sorted(full_interval))

        res = []
        for interval in full_interval:
            if not res:
                res.append(interval)
            
            elif res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res