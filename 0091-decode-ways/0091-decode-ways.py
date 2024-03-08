class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s):1}
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if(1+i < len(s) and (s[i] == "1" or s[i] == "2" and s[1+i] in "0123456")):
                dp[i] += dp[2+i]
        
        return dp[0]