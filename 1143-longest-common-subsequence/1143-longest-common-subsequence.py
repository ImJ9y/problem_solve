class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    ans[i][j] = 1 + ans[i-1][j-1]
                else:
                    ans[i][j] = max(ans[i-1][j], ans[i][j-1])
        print(ans)
        return ans[len(text1)-1][len(text2)-1]