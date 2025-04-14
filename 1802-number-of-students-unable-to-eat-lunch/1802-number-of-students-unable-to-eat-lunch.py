class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        q = collections.deque(students)

        for sandwich in sandwiches:
            if sandwich in q:
                while q[0] != sandwich:
                    temp = q.popleft()
                    q.append(temp)
                
                q.popleft()
            else:
                return len(q)
            
        return len(q)