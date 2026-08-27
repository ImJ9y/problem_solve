class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1))]

        #     a b c d e
        # a   1 1 0 0 0 
        # c   1 1 2 2 2
        # e   1 1 2 2 3  

        for i in range(len(text1)):
            for j in range(len(text2)):
                if i < len(text1) and text1[i] == text2[j]:
                    res[i][j] = 1 + res[i-1][j-1]
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        
        return res[len(text1)-1][len(text2)-1] if res else 0