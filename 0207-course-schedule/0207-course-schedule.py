class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i:[] for i in range(numCourses)}

        for cur,preq in prerequisites:
            course_map[cur].append(preq)
        
        visit, cycle = set(), set()
        res = []

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in visit:
                return True
            
            cycle.add(cur)
            for preq in course_map[cur]:
                if not(dfs(preq)):
                    return False
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True