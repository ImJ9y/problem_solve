class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = {i:[] for i in range(numCourses)}

        for cur, preq in prerequisites:
            preq_map[cur].append(preq)
        

        visit, cycle = set(), set()
        res = []

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in res:
                return True
            
            cycle.add(cur)
            for preq in preq_map[cur]:
                if not dfs(preq):
                    return False
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True