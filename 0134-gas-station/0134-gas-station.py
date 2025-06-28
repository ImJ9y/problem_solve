class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        cur = 0
        start = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]

            if cur < 0:
                cur = 0
                start = i + 1
        
        return start

        # n = len(gas)

        # if n == 1:
        #     if gas[0] > cost[0]:
        #         return 0
        #     else:
        #         return -1
        
        # for i in range(n):
        #     cur = 0
        #     for j in range(n + 1):
                
        #         if (i + j) > n-1 :
        #             k = i + j - n 
        #         else: 
        #             k = i + j
                
        #         cur = cur + gas[k]

        #         if cur < cost[k]:
        #             break
        #         else:
        #             cur = cur - cost[k]
        #         if cur > 0 and j == n:
        #             return i   
        # return -1



