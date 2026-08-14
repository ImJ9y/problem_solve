class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = {i:[] for i in range(numCourses)}

        for cur, preq in prerequisites:
            preq_map[cur].append(preq)
        

        visit = set()
        res = []

        def dfs(cur):
            if cur in visit:
                return False
            if preq_map[cur] == []:
                return True
            
            visit.add(cur)
            for preq in preq_map[cur]:
                if not dfs(preq):
                    return False
            visit.remove(cur)
            preq_map[cur] = []
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        print(res)
        return True