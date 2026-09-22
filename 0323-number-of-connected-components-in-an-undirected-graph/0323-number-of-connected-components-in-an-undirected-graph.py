class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1, n2):
            u1, u2 = find(n1), find(n2)
            
            if u1 == u2:
                return 0

            if u1 < u2:
                parent[u1] = u2
                rank[u2] += rank[u1]
            else:
                parent[u2] = u1
                rank[u1] += rank[u2]
            
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
