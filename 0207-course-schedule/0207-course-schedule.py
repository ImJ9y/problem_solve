class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}

        for cur, preq in prerequisites:
            pre_map[cur].append(preq)
        
        visit, cycle = set(), set()
        res = []

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in res:
                return True
            
            cycle.add(cur)
            for pre in pre_map[cur]:
                if not dfs(pre):
                    return False
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
