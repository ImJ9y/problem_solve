class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = [] #[temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = (i - stackIndex)
            stack.append([temp, i])
        
        return ans