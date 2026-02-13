class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i:[] for i in range(numCourses)}

        for cur, preq in prerequisites:
            pre_map[cur].append(preq)
        
        visited = set()
        def dfs(cur):
            if cur in visited: 
                return False

            if pre_map[cur] == []: 
                return True

            visited.add(cur)
            for preq in pre_map[cur]:
                if not dfs(preq): return False
            
            visited.remove(cur)
            pre_map[cur] = []
            return True
        
        for cur in range(numCourses):
            if not dfs(cur): return False
        
        return True

