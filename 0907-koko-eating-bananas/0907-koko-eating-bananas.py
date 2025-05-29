class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        L, R = ceil(sum(piles) / h), max(piles)
        res = R

        while L <= R:
            M = (L+R)//2
            if M == 0:
                break
                
            hours = 0
            for p in piles:
                hours += ceil((p/M))

            if hours <= h:
                res = min(res, M)
                R = M -1
            else:
                L = M + 1

        return int(res)

