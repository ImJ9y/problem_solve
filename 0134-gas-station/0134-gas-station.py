class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        cur = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            
            if cur < 0:
                cur = 0
                start = i + 1
        
        return start
            
            
                