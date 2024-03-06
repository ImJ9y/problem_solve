class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for i in range(target+1)]
        
        for c in candidates:
            for i in range(target + 1):
                if i < c: continue
                
                if i == c:
                    dp[i].append([c])
                else:
                    for secondList in dp[i-c]:
                        dp[i].append(secondList + [c])
        
        return dp[target]