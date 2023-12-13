class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
#       return sorted(s) == sorted(t)
        
    
        #or
    
    
#       temp = []
#       for c in s:
#           temp.append(c)
        
#       for c2 in t:
#           if c2 in temp:
#               temp.remove(c2)
#           else:
#               temp.append(c2)
        
#       return not temp
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #if hashmap doesn't have the value the default value = 0
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS:
            #order can be different so we need to use .get() for countT
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
                