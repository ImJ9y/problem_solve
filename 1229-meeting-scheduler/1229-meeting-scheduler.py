class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        n1 = len(slots1)
        n2 = len(slots2)

        i = j = 0

        while i < n1 and j < n2:
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            if min(e1, e2) - max(s1, s2) >= duration:
                return [max(s1,s2), max(s1,s2)+duration]
            
            if e1 > e2:
                j += 1
            else:
                i += 1
        
        return []