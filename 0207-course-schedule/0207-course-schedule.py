class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = { i : [] for i in range(numCourses)}

        for cur, preq in prerequisites:
            preq_map[cur].append(preq)
        
        visited = set()
        def dfs(cur):
            if cur in visited: return False
            if preq_map[cur] == []: return True

            visited.add(cur)
            for preq in preq_map[cur]:
                if not dfs(preq): return False
            
            visited.remove(cur)
            preq_map[cur] = []
            return True
        
        for cur in range(numCourses):
            if not dfs(cur): return False
        
        return True