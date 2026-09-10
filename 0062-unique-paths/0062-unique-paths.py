class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n

        for _ in range(m-1):
            new_rows = [1] * n

            for i in range(n-2, -1,-1):
                new_rows[i] = new_rows[i+1] + rows[i]
            
            rows = new_rows
        
        return rows[0]