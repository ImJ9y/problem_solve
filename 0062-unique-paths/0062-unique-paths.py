class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = [1] * n

        for _ in range(m-1):
            NEW_ROWS = [1] * n

            for i in range(n-2,-1,-1):
                NEW_ROWS[i] = NEW_ROWS[i+1] + ROWS[i]
            
            ROWS = NEW_ROWS
        
        return ROWS[0]