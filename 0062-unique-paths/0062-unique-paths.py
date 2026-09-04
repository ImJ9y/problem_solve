class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m-1):
            new_row = [1] * n
            for i in range(n-2,-1,-1):
                new_row[i] = new_row[i+1] + row[i]
            row = new_row
        
        return row[0]


