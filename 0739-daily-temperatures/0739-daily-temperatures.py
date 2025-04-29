class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = [] #i, temp

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIndex, stackTemp = stack.pop()
                ans[stackIndex] = i-stackIndex

            stack.append([i, temp])
            
        
        return ans