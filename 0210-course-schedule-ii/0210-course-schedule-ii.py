class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = {i:[] for i in range(numCourses)}

        for cur, preq in prerequisites:
            preq_map[cur].append(preq)
        
        res = []
        visit, cycle = set(), set()
        def dfs(cur):
            if cur in cycle:
                return False
            if cur in visit:
                return True
            
            cycle.add(cur)
            for preq in preq_map[cur]:
                if not dfs(preq):
                    return []
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
                
