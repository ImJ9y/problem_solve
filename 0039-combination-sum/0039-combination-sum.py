class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target+1)]
        
        for c in candidates:
            for i in range(1, target+1):
                if i < c: 
                    continue
                
                if i == c:
                    dp[i].append([c])
                
                else:
                    for secList in dp[i-c]:
                        dp[i].append(secList+[c])
        return dp[target]