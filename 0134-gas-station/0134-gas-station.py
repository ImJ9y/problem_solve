class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        curr = 0
        start = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                start = i + 1
        
        return start

        