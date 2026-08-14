class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        for i in range(len(gas)):
            target = gas[i] - cost[i]

            if target > start:
                start = target + i
        
        return start