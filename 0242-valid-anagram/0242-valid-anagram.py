class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        s2 = []
        
        for c1 in s:
            s1.append(c1)
        
        for c2 in t:
            s2.append(c2)
        
        s1.sort()
        s2.sort()
        
        for i in range(len(t)):
            if len(s1) != len(s2):
                return False
            elif s1[len(s1)-1] != s2[len(s2)-1]:
                return False
            elif s1[i] != s2[i]:
                return False
            
        return True
        
        
        
        
        
                     
        
        