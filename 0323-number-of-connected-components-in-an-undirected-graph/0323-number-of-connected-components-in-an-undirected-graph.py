class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(u1, u2):
            n1, n2 = find(u1), find(u2)

            if n1 == n2:
                return 0
            
            if n1 < n2:
                parent[n1] = n2
                rank[n2] += rank[n1]
            else:
                parent[n2] = n1
                rank[n1] += rank[n2]
        
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res