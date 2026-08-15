class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = [[grid[0][0], 0, 0]] #time, r, c
        directions = [(0,1),(1,0),(-1,0), (0,-1)]
        visit = set()
        visit.add((0,0))

        while minH:
            t, r, c = heapq.heappop(minH)
            visit.add((r,c))

            if r == n-1 and c == n-1:
                return t

            for dr, dc in directions:
                neiR = dr+r
                neiC = dc+c

                if neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in visit:
                    continue
                
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
                
