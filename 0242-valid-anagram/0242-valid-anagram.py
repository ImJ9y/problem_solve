class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #return sorted(s) == sorted(t)
        
        temp = []
        for c in s:
            temp.append(c)
        
        for c2 in t:
            if c2 in temp:
                temp.remove(c2)
            else:
                temp.append(c2)
        
        return not temp