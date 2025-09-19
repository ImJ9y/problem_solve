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
            if cur < 0:
                cur = 0
                start = i
            
            cur += gas[i] - cost[i]
        
        return start


