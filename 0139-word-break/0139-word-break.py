class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

        # for i in range(len(s)-1, -1,-1):
        #     for w in wordDict:
        #         if i + len(w) <= len(s) and s[i : i+len(w)] == w:
        #             dp[i] = dp[i + len(w)]
        #         if dp[i]:
        #             break
        
        # return dp[0]
